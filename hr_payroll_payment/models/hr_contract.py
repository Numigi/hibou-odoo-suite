# Part of Hibou Suite Professional. See LICENSE_PROFESSIONAL file for full copyright and licensing details.

from odoo import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    payroll_fiscal_position_id = fields.Many2one(
        'account.fiscal.position',
        'Payroll Fiscal Position',
        domain="[('company_id', '=', company_id)]",
        help="Used for mapping accounts when processing payslip journal entries."
    )
