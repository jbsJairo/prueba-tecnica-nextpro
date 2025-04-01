from odoo import fields, models

class ProductLabel(models.Model):
    _name = 'product.label'
    _description = 'Etiqueta para productos'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    product_ids = fields.Many2many(
        'product.template',
        'product_label_product_rel',
        'label_id',
        'product_id',
        string='Productos'
    )
