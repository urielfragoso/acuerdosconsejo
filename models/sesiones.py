
from odoo import models,fields



class altasesionesconsejo(models.Model):
    _name = 'consejo.sesiones'
    _description = 'Catalogo de sesiones de consejo'
    _rec_name = 'nosesion'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'nosesion'


    nosesion = fields.Char(tracking=1)
    fechasesion = fields.Date(tracking=1)
    fechalimite = fields.Date(tracking=1)
    tiposesion = fields.Selection([('ORD','Ordinaria'),
                                   ('EXT','Extraordinaria')], tracking=1, default='ORD')
