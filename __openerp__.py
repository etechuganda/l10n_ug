# -*- encoding: utf-8 -*-
#################################################################################
#
#    Copyright (C) 2012 E-Tech Uganda Ltd
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    'name': 'Uganda Localization',
    'description': 'Uganda Localization',
    'category': 'Localisation/Account Charts',
    'author': 'E-Tech Uganda',
    'website': 'http://etech.ug',
    'version': '1.0',
    'depends': ['account','account_chart'],
    'init_xml': [],
    'update_xml': [
        'data/account.account.type.csv',
        'data/account_tax_code_template.xml',
        'data/account.account.template.csv',
        'data/l10n_uganda_account_chart_template.xml',
        'data/account_tax_template.xml',
        'data/res_country_district.xml',
        'partner_view.xml'
    ],
    'installable': True,
    'active': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
