
from odoo import models,fields, api
from odoo.exceptions import UserError



class seguimientocuerdos(models.Model):
    _name = 'consejo.seguimiento.acuerdos'
    _description = 'Tabla donde se guardaran el registro del seguimiento de acuerdos'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'noacuerdo'
    _order = 'noacuerdo'


    refid_acuerdo = fields.Many2one(comodel_name='consejo.acuerdos',tracking=1)
    noacuerdo = fields.Char(related="refid_acuerdo.noacuerdo")
    refid_tipoacuerdo = fields.Many2one(related='refid_acuerdo.refid_tipoacuerdo',tracking=1)
    acuerdo = fields.Text(related="refid_acuerdo.acuerdo", tracking=1)

    refid_iap = fields.Many2one(related="refid_acuerdo.refid_iap")

    estatus = fields.Selection([('pendiente','Pendiente'),
                                ('asignado','Asignado')],  default='asignado')

    estatus_acuerdo = fields.Selection([('pendiente','Pendiente'),
                                        ('terminado','Terminado'),
                                        ('retrazoama','Retrazo Amarillo'),
                                        ('retrazorojo','Retrazo Rojo'),
                                        ('consejo','Autorizado consejo')], default='pendiente')
    fecha_asignacion = fields.Date(related="refid_acuerdo.fecha_asignacion")

    nooficio = fields.Char(tracking=1)
    existe_tramita = fields.Selection([('SI','SI'),
                                       ('NO','NO')], default='NO')
    folio_tramita = fields.Integer(tracking=1)
    tramite = fields.Many2one(comodel_name='cf.tipos.tramites')

    RefIdUsuario = fields.Many2one(comodel_name='res.users', string='Asesor Asignado', domain=[("id", '=', 'env.uid')])

