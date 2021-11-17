# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date




class propietario  (models.Model):
    _name = 'competicion.propietario'
    _description = 'Permite añadir propietarios de animales'

    
    name = fields.Char('Nombre', required=True)
    lastname = fields.Char('Apellido', required=True)
    age = fields.Date(string='Edad')

    #Relaciones entre tablas 
    dog_ids  = fields.One2many('competicion.dog', 'propietario_id')
    
    

class participante (models.Model):
    _name = 'competicion.participante'
    _inherit = 'competicion.propietario'
    _description = "Permite añadir informacion de agility a los propietarios"


    licencia = fields.Integer(string="Numero de licencia", required=True)


    #Relaciones entre tablas
    dog_id = fields.Many2many('competicion.dog')



    
class dog (models.Model):
    _name = 'competicion.dog'
    _description = 'Permite añadir un perro'
    
    name = fields.Char('Nombre del perro', required=True)
    microchip = fields.Integer(string='Numero de microchip', required=True)  
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True)
    edad = fields.Integer(string='Edad del perro', compute = '_get_anos')
    raza = fields.Selection(string='Raza del perro', selection=[('b', 'Border Collie'),('s', 'Shetland'), ('c', 'Cocker')])
    
    #Relacion entre tablas
    propietario_id = fields.Many2one('competicion.propietario', 'Propietario') 
    prueba_ids = fields.Many2many('competicion.prueba')
    participante_id = fields.Many2many('competicion.participante')
    
    
    @api.depends('fecha_nacimiento')
    def  _get_anos(self): #puede dar error por el self que coge un conjunto de datos
        for perro in self:
            hoy = date.today()
            perro.edad = relativedelta(hoy, perro.fecha_nacimiento).years
        
        
        
        
class prueba  (models.Model):
    _name= 'competicion.prueba'
    _description = 'Permite añadir competiciones'
    _order = 'club'
    
    club = fields.Char('Club')
    place = fields.Char('Place')
    date = fields.Date(string='Fecha')
    
    
    #Realacion entre tablas
    dog_ids = fields.Many2many('competicion.dog')    



'''class LibraryBook(models.Model):
 _name = 'library.book'
 name = fields.Char('Title')
 isbn = fields.Char('ISBN')
 author_ids = fields.Many2many('res.partner', 'Authors')
 @api.multi
 def name_get(self):
 result = []
 for book in self:
 authors = book.author_ids.mapped('name')
 name = '%s (%s)' % (book.name, ', '.join(authors))
 result.append((book.id, name))
 return result>'''
