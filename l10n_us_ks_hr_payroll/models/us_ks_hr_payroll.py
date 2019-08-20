from odoo import models, fields, api


class USKSHrContract(models.Model):
    _inherit = 'hr.contract'

    ks_k4_filing_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('head_household', 'Head of Household'),
        ('exempt', 'Exempt'),
    ], string='Kansas K-4 Filing Status')
    ks_k4_allowances = fields.Integer(string="Kansas K-4 Allowances",
                                      help="Allowances claimed on K-4")
    ks_additional_withholding = fields.Float(string="Kansas K-4 Additional Withholding",
                                             help='Additional withholding from line 5 of form K-4')

    # TODO - Can this be deleted as well?
    @api.multi
    def ks_unemp_rate(self, year):
        self.ensure_one()
        if self.futa_type == self.FUTA_TYPE_BASIC:
            return 0.0

        if hasattr(self.employee_id.company_id, 'ks_unemp_rate_' + str(year)):
            return self.employee_id.company_id['ks_unemp_rate_' + str(year)]

        raise NotImplemented('Year (' + str(year) + ') Not implemented for US Kansas.')


class KSCompany(models.Model):
    _inherit = 'res.company'

    ks_unemp_rate_2018 = fields.Float(string="Kansas Unemployment Insurance Rate 2018", default=2.7)
