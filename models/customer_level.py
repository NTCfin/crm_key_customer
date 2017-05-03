from openerp import api, fields, models, _


class CustomerLevel(models.Model):
		_name='crm_key_customer.customer_level'
		_description = 'Customer Level'
		
		def get_partner_count(self):
			for level in self:
				number_of_partners = len(level.partner_ids)
				level.partner_count = number_of_partners
				

		name = fields.Char('Name', help='e.g. bronze or silver')
		description = fields.Text('Description')
		partner_ids = fields.One2many('res.partner','customer_level_id','Customers on this level')
		partner_count = fields.Integer(compute='get_partner_count', string="Number of customers')