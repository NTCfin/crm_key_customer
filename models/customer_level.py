from openerp import api, fields, models, _


class CustomerLevel(models.Model):
		_name='crm_keycustomer.customer_level'
		_description = 'Customer Level'
		

		name = fields.Char('Name', help='e.g. bronze or silver')
		description = fields.Text('Description')