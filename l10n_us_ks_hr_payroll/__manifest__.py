{
    'name': 'USA - Kansas - Payroll',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'license': 'AGPL-3',
    'category': 'Localization',
    'depends': ['l10n_us_hr_payroll'],
    'version': '11.0.2018.0.1',
    'description': """
USA::Kansas Payroll Rules.
===========================

    * Partner and Contribution Register for Kansas Department of Labor (KDOL)
    * Partner and Contribution Register for Kansas Department of Labor (KDOR)
    * Company level Kansas Unemployment Rate
    """,
    'auto_install': False,
    'website': 'https://hibou.io/',
    'data':[
        'views/us_ks_hr_payroll_views.xml',
        'data/base.xml',
        'data/rates.xml',
        'data/rules.xml',
        'data/final.xml',
    ],
    'installable': True
}