{
    'name': 'USA - Pennsylvania - Payroll',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'license': 'AGPL-3',
    'category': 'Localization',
    'depends': ['l10n_us_hr_payroll'],
    'version': '11.0.2019.0.0',
    'description': """
USA::Pennsylvania Payroll Rules.
================================

* Partners for Pennsylvania Department of Labor and Industry (PDLI) and
* Pennsylvania Department of Treasury (PDOT)
* Contribution register for Pennsylvania Department of Labor and Industry (PDLI) - Unemployment Tax
* Contribution register for Pennsylvania Department of Treasury (PDOT) - State Income Tax
* Contract level Pennsylvania Unemployment Rate
* Company level Pennsylvania Unemployement Rate
    """,

    'auto_install': False,
    'website': 'https://hibou.io/',
    'data': [
        'views/hr_payroll_views.xml',
        'data/base.xml',
        'data/rates.xml',
        'data/rules.xml',
        'data/final.xml',
    ],
    'installable': True
}
