from odoo import models, fields, api


class USXHrContract(models.Model):
    _inherit = 'hr.contract'

    x_w4_allowances = fields.Integer(string="X Allowances")
    x_w4_additional_wh = fields.Float(string="X Additional Withholding")
    x_w4_tax_exempt = fields.Boolean(string="MN Tax Exempt")
    x_w4_filing_status = fields.Selection([
        # ('exempt', 'Exempt'),
        ('single', 'Single'),
        ('married', 'Married'),
    ], string='X Filing Status', default='single')
