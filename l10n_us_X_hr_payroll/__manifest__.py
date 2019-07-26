{
    'name': 'USA - X - Payroll',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'license': 'AGPL-3',
    'category': 'Localization',
    'depends': ['l10n_us_hr_payroll'],
    'version': '11.0.2019.0.0',
    'description': """
USA - X Payroll Rules
=============================

* Contribution register and partner for X Department of Revenue (X DOR) - Unemployment Taxes, Income Tax Withholding
* Contract level X Exemptions
* Company level X Unemployment Rate

    """,
    'website': 'https://hibou.io/',
    'data': [
        'views/hr_payroll_views.xml',
        'data/base.xml',
        'data/rates.xml',
        'data/rules.xml',
        'data/final.xml',
    ],
    'auto_install': False,
    'installable': True,
}
