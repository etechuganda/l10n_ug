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
        'region_id' :fields.selection((('C','Central'), ('N','Northern') ,('E','Eastern'),('W','Western')),'Region',help="Administrative Region",required=False),
        'name': fields.char('District Name', size=64, required=True),
        'code': fields.char('District Code', size=3, help='The district code in three chars.\n', required=True),
    }
CountryDistrict()

class DistrictCounty(osv.osv):
    _description='District County'
    _name = 'res.district.county'
    _columns = {
        'district_id': fields.many2one('res.country.district', 'District',  required=True),
        'name': fields.char('County Name', size=64, required=True),
        'code': fields.char('County Code', size=3, help='The county code in three chars.\n', required=True),
    } 
DistrictCounty()

class CountyConstituency(osv.osv):
    _description='Constituency County'
    _name = 'res.county.constituency'
    _columns = {
        'county_id': fields.many2one('res.district.county', 'County', required=True),
        'name': fields.char('Constituency Name', size=64, required=True),
        'code': fields.char('Constituency Code', size=3, help='The constituency code in three chars.\n', required=True),
                }
CountyConstituency()

class ConstituencySubCounty(osv.osv):
    _description='Constituency County'
    _name = 'res.constituency.subcounty'
    _columns = {
        'constituency_id': fields.many2one('res.county.constituency', 'Constituency', required=True),
        'name': fields.char('SubCounty Name', size=64, required=True),
        'code': fields.char('SubCounty Code', size=3, help='The constituency code in three chars.\n', required=True),
                }
ConstituencySubCounty()


class SubCountyParish(osv.osv):
    _description='SubCounty Parish'
    _name = 'res.subcounty.parish'
    _columns = {
        'subcounty_id': fields.many2one('res.constituency.subcounty', 'Subcounty', required=True),
        'name': fields.char('Parish Name', size=64, required=True),
        'code': fields.char('Parish Code', size=3, help='The parish code in three chars.\n', required=True),
    }
SubCountyParish()

class ParishVillage(osv.osv):
    _description='Parish Village'
    _name = 'res.parish.village'
    _columns = {
        'parish_id': fields.many2one('res.subcounty.parish', 'Parish', required=True),
        'name': fields.char('Village Name', size=64, required=True),
        'code': fields.char('Village Code', size=3, help='The village code in three chars.\n', required=False),
    }
ParishVillage()


class res_partner_address(osv.osv):
    _name = 'res.partner.address'
    _inherit = 'res.partner.address'
    _columns = {
        'landmark' : fields.char('Closest Landmark', size=64),
        'district_id' : fields.many2one('res.country.district', 'District', domain="[('country_id','=',country_id)]"),
        'county_id': fields.many2one('res.district.county', 'County', domain="[('district_id','=',district_id)]"),
        'constituency_id': fields.many2one('res.county.constituency', 'Constituency', domain="[('county_id','=',county_id)]"),
        'subcounty_id': fields.many2one('res.constituency.subcounty', 'Subcounty', domain="[('constituency_id','=',constituency_id)]"),
        'parish_id': fields.many2one('res.subcounty.parish','Parish', domain="[('subcounty_id','=',subcounty_id)]"),
        'village_id': fields.many2one('res.parish.village','Village', domain="[('parish_id','=',parish_id)]"),
                }
res_partner_address()

class res_partner(osv.osv):
   
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'tin' : fields.char("Taxpayer Identification No.",size=10),
                }
res_partner()

