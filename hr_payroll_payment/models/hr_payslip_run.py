# Part of Hibou Suite Professional. See LICENSE_PROFESSIONAL file for full copyright and licensing details.

from odoo import api, fields, models, _

class HrPayslipRun(models.Model):
    _inherit = 'hr.payslip.run'

    @api.depends('slip_ids.is_paid')
    def _is_paid(self):
        for run in self:
            run.is_paid = all(run.slip_ids.mapped('is_paid'))

    is_paid = fields.Boolean(string="Payslips Paid", compute='_is_paid', store=True)
    date = fields.Date('Date Account', states={'draft': [('readonly', False)], 'verify': [('readonly', False)]},
                       readonly=True,
                       help="Keep empty to use the period of the validation(Payslip) date.")
    batch_payment_id = fields.Many2one('account.batch.payment', string='Payment Batch')

    def action_register_payment(self):
        action = self.mapped('slip_ids').action_register_payment()
        payments = self.env['account.payment'].browse(action['res_ids'])
        batch_action = payments.create_batch_payment()
        self.write({'batch_payment_id': batch_action['res_id']})
        return batch_action

    def write(self, values):
        if 'date' in values:
            slips = self.mapped('slip_ids').filtered(lambda s: s.state in ('draft', 'verify'))
            slips.write({'date': values['date']})
        return super().write(values)