# -*- coding: utf-8 -*-
{
    'name': "Solcitudes de Vacaciones",

    'summary': """
       Solcitudes de Vacaciones""",

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Human Resources',
    'version': '0.1',
    'depends': [
                'base',
                'base_automation',
                'hr',
                ],

    'data': [
        'security/ir.model.access.csv',
        'data/template_mail.xml',
        'data/base_automation.xml',
        'views/employee_holidays_leave_views.xml',
        
    ],
}
