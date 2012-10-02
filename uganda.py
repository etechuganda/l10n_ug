#!/usr/bin/env python
# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

import time
import datetime
import pooler
from osv import osv
from osv import fields
from datetime import date


class CountryDistrict(osv.osv):
    _description='Country District'
    _name = 'res.country.district'
    _columns = {
        'country_id': fields.many2one('res.country', 'Country', required=True),
        'region_id' :fields.selection((('C','Central'), ('N','Northern') ,('E','Eastern'),('W','Western')),'Region',required=True),
        'name': fields.char('District Name', size=64, required=True),
        'code': fields.char('District Code', size=3, help='The district code in three chars.\n', required=False),
    }
CountryDistrict()

class DistrictCounty(osv.osv):
    _description='District County'
    _name = 'res.district.county'
    _columns = {
        'district_id': fields.many2one('res.country.district', 'District',  required=True),
        'name': fields.char('County Name', size=64, required=True),
        'code': fields.char('County Code', size=3, help='The county code in three chars.\n', required=False),
    } 
DistrictCounty()

class CountySubCounty(osv.osv):
    _description='County subcounty'
    _name = 'res.county.subcounty'
    _columns = {
        'county_id': fields.many2one('res.district.county', 'County', required=True),
        'name': fields.char('Subcounty Name', size=64, required=True),
        'code': fields.char('Subcounty Code', size=3, help='The subcounty code in three chars.\n', required=False),
    }
CountySubCounty()


class res_partner_address(osv.osv):
    _name = 'res.partner.address'
    _inherit = 'res.partner.address'
    _columns = {
        'village' : fields.char('Village', size=64,required=True),
        'landmark' : fields.char('Closest Landmark', size=64,required=True),
        'district_id' : fields.char('District', size=64,required=True),
        'county_id' : fields.char('County', size=64,required=True),
        'sub_county_id' : fields.char('Sub-County', size=64,required=True),
        'new_district_id' : fields.many2one('res.country.district', 'District', domain="[('country_id','=',country_id)]"),
        'new_county_id': fields.many2one('res.district.county', 'County', domain="[('district_id','=',district_id)]"),
        'new_sub_county_id': fields.many2one('res.county.subcounty','Sub-County', domain="['county_id','=',county_id)]"),
                }
res_partner_address()

class res_partner(osv.osv):
   
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'tin' : fields.char("Taxpayer Identification No.",size=10),
                }
res_partner()

