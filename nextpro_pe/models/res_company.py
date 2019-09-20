# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    razon_social = fields.Char(string="Razon social", required=True)
    ruc = fields.Char(string="R.U.C.", required=True)
    agente_retencion = fields.Boolean(string="Agente de retencion")
    buen_contribuyente = fields.Boolean(string="Buen contribuyente")
    plan_contable = fields.Selection(
        string= "Plan contable", 
        selection=[("01", "General empresarial"), 
                    ("02", "Por definir")]     
    )
    
# FIN ResCompany
