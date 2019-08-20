from odoo.addons.l10n_us_hr_payroll.tests.test_us_payslip import TestUsPayslip, process_payslip


class TestUsKSPayslip(TestUsPayslip):
    KS_UNEMP_MAX_WAGE = 14000.0
    KS_UNEMP_RATE = - (2.70 / 100.00)

    def test_2019_taxes_weekly(self):
        salary = 5000.00
        schedule_pay = 'weekly'
        allowances = 2
        # Amount of each withholding allowance for weekly from Withholding Allowance Amounts Table
        # https://www.ksrevenue.org/pdf/kw100.pdf
        withholding_allowance = 43.27 * allowances
        taxable_pay = salary - withholding_allowance

        # Tax Percentage Method for Single, taxable pay over $58, under $346
        # This bracket is used in the rule:
        #             (float('inf'), 0.057, 24.09),
        wh = ((taxable_pay - 635) * 0.057) + 24.09
        wh = -round(wh)

        employee = self._createEmployee()
        contract = self._createContract(employee,
                                        salary,
                                        struct_id=self.ref('l10n_us_ks_hr_payroll.hr_payroll_salary_structure_us_ks_employee'),
                                        schedule_pay=schedule_pay)
        contract.ks_k4_allowances = allowances
        contract.ks_k4_filing_status = 'single'

        self.assertEqual(contract.schedule_pay, 'weekly')

        self._log('2018 Kansas tax first payslip:')
        payslip = self._createPayslip(employee, '2019-01-01', '2019-01-31')

        payslip.compute_sheet()
        cats = self._getCategories(payslip)

        self.assertPayrollEqual(cats['WAGE_US_KS_UNEMP'], salary)
        self.assertPayrollEqual(cats['ER_US_KS_UNEMP'], cats['WAGE_US_KS_UNEMP'] * self.KS_UNEMP_RATE)
        self.assertPayrollEqual(cats['KS_INC_WITHHOLD'], wh)

        process_payslip(payslip)

        self._log('2018 Kansas tax second payslip:')
        payslip = self._createPayslip(employee, '2019-02-01', '2019-02-28')

        payslip.compute_sheet()
        cats = self._getCategories(payslip)

        self.assertPayrollEqual(cats['WAGE_US_KS_UNEMP'], salary)
        self.assertPayrollEqual(cats['ER_US_KS_UNEMP'], salary * self.KS_UNEMP_RATE)

    def test_2018_taxes_with_state_exempt(self):
        salary = 210
        schedule_pay = 'weekly'
        allowances = 2
        # Tax Exempt
        wh = 0

        employee = self._createEmployee()
        contract = self._createContract(employee,
                                        salary,
                                        struct_id=self.ref('l10n_us_ks_hr_payroll.hr_payroll_salary_structure_us_ks_employee'),
                                        schedule_pay=schedule_pay)
        contract.ks_k4_allowances = allowances
        contract.ks_k4_filing_status = 'exempt'

        payslip = self._createPayslip(employee, '2019-02-01', '2019-02-28')
        payslip.compute_sheet()

        cats = self._getCategories(payslip)

        self.assertEqual(cats.get('KS_INC_WITHHOLD', 0.0), wh)
