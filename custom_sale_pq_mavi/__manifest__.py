{
    'name': 'custom_sale_pq_mavi',
        "summary": "Modulo para mejorar la gestion de Ventas",
    "description": """
Modulo para mejorar la gestion de Ventas..
""",
    "author": "Jairon Bravo Segura",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    "license": "AGPL-3",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "sale",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "report/product_report.xml",
        "report/product_report_template.xml",
        "views/product_view.xml",
        "views/product_label_wizard_view.xml",
        "views/menus.xml",
    ],
}