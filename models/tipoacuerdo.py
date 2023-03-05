
from odoo import models,fields



class responsablesacuerdos(models.Model):
    _name = 'consejo.tipo.acuerdo'
    _description = 'Catalogo de responsables por tipo de acuerdo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'asunto'


    asunto = fields.Char(tracking=1)
    usuarios_id = fields.Many2many('res.users', 'usuarios_id',
                                    required=1, tracking=1,
                                    help="Usuarios responsbles de dar seguimiento")


    tipoasunto = fields.Selection([('IAP','IAP'),
                                   ('JAP','JAP')], tracking=1, default='IAP')

    seguimiento = fields.Selection([('SI', 'SI'),
                                   ('NO', 'NO')], tracking=1, default='SI')