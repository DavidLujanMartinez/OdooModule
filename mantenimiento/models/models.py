# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mantenimiento(models.Model):
#     _name = 'mantenimiento.mantenimiento'
#     _description = 'mantenimiento.mantenimiento'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



from odoo import models, fields, api
from datetime import datetime

class departamento(models.Model):
    _name = "mantenimiento.departamento"
    name = fields.Char(string="Nombre",required=True)
    numero = fields.Integer(string="Numero de departamento",required=True)
    productos = fields.One2many("mantenimiento.producto","ubicacion",string="Productos en este departamento")
    empleados = fields.One2many("mantenimiento.empleado","departamento",string="Empleados de este departamento")




class producto(models.Model):
    _name = "mantenimiento.producto"
    name = fields.Char(string="Nombre",required=True)
    fecha_compra = fields.Date(string="Fecha de compra",default = fields.Date.today,required=True)
    ubicacion = fields.Many2one("mantenimiento.departamento",string="departamento",required=True,ondelete="cascade")
    reparaciones = fields.Many2many("mantenimiento.reparacion","produc",string="Reparaciones")



class empleado(models.Model):
    _name = "mantenimiento.empleado"
    DNI = fields.Char(string="DNI",required=True)
    name = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="apellidos",required=True)
    departamento = fields.Many2one("mantenimiento.departamento",string="departamento",required=True,ondelete="cascade")
    emple_reportes = fields.One2many("mantenimiento.reparacion","emple",string="Reportes realizados")
    emple_reparaciones = fields.Many2many("mantenimiento.reparacion","emple_repara",string="Reparaciones realizadas")




class reparacion(models.Model):
    _name = "mantenimiento.reparacion"
    _order = "estado desc"
    produc = fields.Many2many("mantenimiento.producto",string="producto",required=True,ondelete="cascade")
    fecha_ini = fields.Date(string="Fecha de inicio",default = fields.Date.today,required=True)
    emple = fields.Many2one("mantenimiento.empleado",string="Empleado que reporta la reparacion reparacion",ondelete="cascade")
    #Esta asi para que sea posible que una reparacion se lleve a cabo entre mas de una persona
    emple_repara = fields.Many2many("mantenimiento.empleado",string="Empleado encargado de la reparacion",ondelete="cascade")
    descripcion = fields.Text(string="Informacion necesario para la reparacion")
    estado = fields.Selection([ ('pendiente', 'Pendiente'),('proceso', 'En proceso'),('completado', 'Completado'),],'Type', default='pendiente')
    horas = fields.Float(string="Horas totales de la reparacion")
    fecha_fin = fields.Date(string="Fecha de finalizacion",default = fields.Date.today)
    totaldias = fields.Text(string="Numero de dias", compute ="_calculadias")



    #Restricciones SQL
    _sql_constraints=[('emple_uniq','unique(DNI)','Ya existe un empleado con ese DNI'),('depar_uniq','unique(numero)','Ya existe un departamento con ese numero')]


    #comprobar la fecha de inicio y finalizacion
    @api.depends('fecha_ini','fecha_fin')
    def _compruebadias(self):
        for r in self:
            if r.fecha_fin < r.fecha_ini:
                raise ValidationError('La fecha de fin no puede ser inferior a la de inicio')


    #Metodo para calcular el numero de dias que a llevado la reparacion
    @api.depends('fecha_ini','fecha_fin')
    def _calculadias(self):
        for r in self:
            r.totaldias= r.fecha_fin - r.fecha_ini
