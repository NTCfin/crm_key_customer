from openerp import api, fields, models, _


class ResPatrner(models.Model):
		_inherit='res.partner'

		is_key_customer = fields.Boolean('Key customer', help='Indicates that the partener is a key customer')
		customer_level_id = fields.Many2one('crm_key_customer.customer_level', 'Customer level')
