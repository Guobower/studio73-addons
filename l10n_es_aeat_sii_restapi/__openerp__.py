# -*- coding: utf-8 -*-
# (c) 2017 Studio73 - Pablo Fuentes <pablo@studio73>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Suministro Inmediato de Información RESTAPI",
    "version": "8.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://odoo-community.org/",
    "author": "Consultoría Informática Studio 73 S.L., "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "l10n_es_aeat_sii",
    ],
    "data": [
        'views/account_invoice_import_view.xml',
        'security/ir.model.access.csv',
    ],
    "application": False,
    "installable": True,
}