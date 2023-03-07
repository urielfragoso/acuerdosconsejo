
from odoo import models,fields, api
from odoo.exceptions import UserError
from datetime import datetime


class registroacuerdos(models.Model):
    _name = 'consejo.acuerdos'
    _description = 'Tabla donde se guardaran los acuerdos registrados por sesion'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'noacuerdo'
    _order = 'noacuerdo'


    refid_sesion = fields.Many2one(comodel_name='consejo.sesiones',tracking=1)
    noacuerdo = fields.Char(tracking=1)
    refid_tipoacuerdo = fields.Many2one(comodel_name='consejo.tipo.acuerdo',tracking=1)
    usuario_asignado = fields.Many2many(related="refid_tipoacuerdo.usuarios_id")
    acuerdo = fields.Text(tracking=1)
    acuerdoiap = fields.Selection([('SI','SI'),
                                   ('NO','NO')], default='NO',tracking=1)

    refid_iap = fields.Many2one(comodel_name='res.partner', domain=[('is_IAP','=',True),('estatus_id','in',[1,2,4,5])],tracking=1)

    estatus = fields.Selection([('pendiente','Pendiente'),
                                        ('asignado','Asignado')],  default='pendiente')

    estatus_acuerdo = fields.Selection([('pendiente','Pendiente'),
                                        ('terminado','Terminado'),
                                        ('retrazoama','Retrazo Amarillo'),
                                        ('retrazorojo','Retrazo Rojo'),
                                        ('consejo','Autorizado consejo')], default='pendiente')
    fecha_asignacion = fields.Date()


    @api.model
    def create(self, vals):
        filtro_acuerdo = [('noacuerdo','=',vals['noacuerdo'])]
        acuerdo_registrado = self.env['consejo.acuerdos'].sudo().search(filtro_acuerdo)

        if not acuerdo_registrado:
            return super(registroacuerdos, self).create(vals)
        else:
            raise UserError('El acuerdo ya existe')


    def btn_asignar(self):
        for record in self:
            for usuario_asignado in record.usuario_asignado:
                usuarios = usuario_asignado.id
                filtro_usuario_asigando = [('RefIdUsuario','=',usuarios),
                                           ('refid_acuerdo','=',record.id)]
                usuario_asignado = self.env['consejo.seguimiento.acuerdos'].sudo().search(filtro_usuario_asigando)

                if not usuario_asignado:
                    record.fecha_asignacion = datetime.now()
                    record.estatus = 'asignado'

                    nuevo_registro = {'refid_acuerdo': record.id,
                                      'RefIdUsuario': usuarios,
                                      'estatus': 'asignado',
                                      'estatus_acuerdo': 'pendiente'
                                      }
                    usuario_asignado.create(nuevo_registro)
                else:
                    raise UserError('El acuerdo: '+record.noacuerdo+' ya fue asignado, verifique nuevamente')



