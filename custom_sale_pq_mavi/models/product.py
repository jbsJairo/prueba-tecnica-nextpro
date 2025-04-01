from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sale_count = fields.Integer(
        string='Sales', compute='_compute_sale_count'
    )
    label_ids = fields.Many2many(
        'product.label',
        'product_label_product_rel',
        'product_id',
        'label_id',
        string='Etiquetas'
    )

    def _compute_sale_count(self):
        for product in self:
            product.sale_count = self.env['sale.order.line'].search_count(
                [('product_id.product_tmpl_id', '=', product.id)]
            )
