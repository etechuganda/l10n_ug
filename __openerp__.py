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
    'name': 'Uganda - Chart of Accounts',
    'description': 'Uganda Localization',
    'category': 'Localization/Account Charts',
    'author': 'ICT Association Uganda (ICTAU)',
    'website': 'http://ictau.ug',
    'version': '2.0',
    'depends': ['account','account_chart'],
    'data': [
        'data/account.account.type.csv',
        'data/account.account.template.csv',
        'data/account.tax.code.template.csv',
        'data/account.chart.template.csv',
        'data/account.tax.template.csv',
        'data/res.country.district.csv',
        'data/res.district.county.csv',
        'data/res.county.constituency.csv',
        'data/res.constituency.subcounty.csv',
        'data/res.subcounty.parish.csv',
        'data/res.parish.village.csv',
        'l10n_chart_ug_wizard.xml',
        'partner_view.xml'
    ],
    'installable': True,
    'images': ['images/config_chart_l10n_ug.jpeg','images/l10n_ug_chart.jpeg'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
