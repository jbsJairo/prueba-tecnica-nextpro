from odoo import models, fields

class ProductLabelWizard(models.TransientModel):
    _name = 'product.label.wizard'
    _description = 'Asignar etiqueta a productos'

    product_ids = fields.Many2many('product.template', string='Productos')
    label_id = fields.Many2one('product.label', string='Etiqueta', required=True)

    def action_assign_label(self):
        for product in self.product_ids:
            product.write({
                'label_ids': [(4, self.label_id.id)]
            })
