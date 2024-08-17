# -*- coding: utf-8 -*-
{
    'name': "Cyb Web Customization",
    'summary': "",
    'description': """""",
    'author': "",
    'website': "",
    'category': '',
    'version': '0.1',
    'depends': ['web','crm_iap_mine'],
    'data': [
        'views/templates_view.xml',
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'cyb_web_customization/static/src/js/cyb_user_men_items.js',
        ],
        'web._assets_primary_variables': [
            'cyb_web_customization/static/src/scss/custom.scss',
        ],
    },
    'demo': [
        'demo/demo.xml',
    ],
}
