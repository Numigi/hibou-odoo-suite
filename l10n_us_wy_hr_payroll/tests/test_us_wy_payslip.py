from odoo.addons.l10n_us_hr_payroll.tests.test_us_payslip import TestUsPayslip, process_payslip
from odoo.addons.l10n_us_hr_payroll.models.l10n_us_hr_payroll import USHrContract


class TestUsWYPayslip(TestUsPayslip):

    # TAXES AND RATES
    WY_UNEMP_MAX_WAGE = 25400
    WY_UNEMP = -2.10 / 100.0

    def test_2019_taxes(self):
        salary = 15000.00

        employee = self._createEmployee()
        contract = self._createContract(employee,
                                        salary,
                                        struct_id=self.ref('l10n_us_wy_hr_payroll.hr_payroll_salary_structure_us_wy_employee'))

        self._log('2019 Wyoming tax first payslip:')
        payslip = self._createPayslip(employee, '2019-01-01', '2019-01-31')

        payslip.compute_sheet()
        cats = self._getCategories(payslip)

        self.assertPayrollEqual(cats['WAGE_US_WY_UNEMP'], salary)
        self.assertPayrollEqual(cats['ER_US_WY_UNEMP'], cats['WAGE_US_WY_UNEMP'] * self.WY_UNEMP)

        process_payslip(payslip)

        # Make a new payslip, this one will have maximums

        remaining_wy_unemp_wages = self.WY_UNEMP_MAX_WAGE - salary if (self.WY_UNEMP_MAX_WAGE - 2*salary < salary) \
            else salary

        self._log('2019 Wyoming tax second payslip:')
        payslip = self._createPayslip(employee, '2019-02-01', '2019-02-28')
        payslip.compute_sheet()
        cats = self._getCategories(payslip)

        self.assertPayrollEqual(cats['WAGE_US_WY_UNEMP'], remaining_wy_unemp_wages)
        self.assertPayrollEqual(cats['ER_US_WY_UNEMP'], remaining_wy_unemp_wages * self.WY_UNEMP)

    def test_2019_taxes_with_external(self):
        # Wage is the cap itself, 25400
        # so salary is equal to self.WY_UNEMP
        salary = 25400
        external_wages = 6000.0

        employee = self._createEmployee()
        contract = self._createContract(employee,
                                        salary,
                                        external_wages=external_wages,
                                        struct_id=self.ref('l10n_us_wy_hr_payroll.hr_payroll_salary_structure_us_wy_employee'))

        self._log('2019 Wyoming External tax first payslip:')
        payslip = self._createPayslip(employee, '2019-01-01', '2019-01-31')
        payslip.compute_sheet()
        cats = self._getCategories(payslip)

        self.assertPayrollEqual(cats['WAGE_US_WY_UNEMP'], self.WY_UNEMP_MAX_WAGE - external_wages)
        self.assertPayrollEqual(cats['ER_US_WY_UNEMP'], cats['WAGE_US_WY_UNEMP'] * self.WY_UNEMP)
