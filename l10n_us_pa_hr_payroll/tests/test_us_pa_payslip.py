from odoo.addons.l10n_us_hr_payroll.tests.test_us_payslip import TestUsPayslip, process_payslip


class TestUsPAPayslip(TestUsPayslip):
    # Taxes and Rates
    PA_UNEMP_MAX_WAGE = 10000.0
    ER_PA_UNEMP = -3.6890 / 100.0
    EE_PA_UNEMP = -0.06 / 100.0
    PA_INC_WITHHOLD = -3.07 / 100

    def test_taxes_under_cap(self):
        salary = 1500

        employee = self._createEmployee()
        contract = self._createContract(employee,
                                        salary,
                                        struct_id=self.ref('l10n_us_pa_hr_payroll.hr_payroll_salary_structure_us_pa_employee'))

        self._log('2019 Pennsylvania tax first payslip:')

        payslip = self._createPayslip(employee, '2019-01-01', '2019-01-31')
        payslip.compute_sheet()

        cats = self._getCategories(payslip)

        self.assertPayrollEqual(cats['WAGE_ER_US_PA_UNEMP'], salary)  # Under Cap so should be equal
        self.assertPayrollEqual(cats['EE_US_PA_UNEMP'], cats['BASIC'] * self.EE_PA_UNEMP)
        self.assertPayrollEqual(cats['ER_US_PA_UNEMP'], round(cats['WAGE_ER_US_PA_UNEMP'] * self.ER_PA_UNEMP, 2))
        # self.assertPayrollEqual(cats['EE_US_PA_INC_WITHHOLD'], wh)

    def test_taxes_over_cap(self):
        salary = 20000

        employee = self._createEmployee()
        contract = self._createContract(employee,
                                        salary,
                                        struct_id=self.ref('l10n_us_pa_hr_payroll.hr_payroll_salary_structure_us_pa_employee'))

        self._log('2019 Pennsylvania tax first payslip:')
        payslip = self._createPayslip(employee, '2018-01-01', '2018-01-31')
        payslip.onchange_contract()
        payslip.compute_sheet()

        cats = self._getCategories(payslip)

        self.assertPayrollEqual(cats['WAGE_ER_US_PA_UNEMP'], self.PA_UNEMP_MAX_WAGE)
        self.assertPayrollEqual(cats['EE_US_PA_UNEMP'], cats['BASIC'] * self.EE_PA_UNEMP)
        self.assertPayrollEqual(cats['ER_US_PA_UNEMP'], cats['WAGE_ER_US_PA_UNEMP'] * self.ER_PA_UNEMP)

