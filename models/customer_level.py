from openerp import api, fields, models, _


class CustomerLevel(models.Model):
		_name='crm_key_customer.customer_level'
		_description = 'Customer Level'
		

		name = fields.Char('Name', help='e.g. bronze or silver')
		description = fields.Text('Description')
		partner_ids = fields.One2many('res.partner','customer_level_id','Customers on this level')