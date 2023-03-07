{
    'name': 'ACUERDOS DE CONSEJO',
    'version': '1.0',
    'category': 'ACUERDOS DE CONSEJO - JAPCDMX',
    'sequence': 15,
    'author': 'DTIC JAPCDMX',
    'summary': 'ACUERDOS DE CONSEJO',
    'description': 'CAPTURA Y SEGUIMIENTO DE ACUERDOS DE CONSEJO',
    'depends': ['base', 'mail', 'registroiap', 'web', 'report_py3o'],

    'data': [
        'security/acuerdos_security.xml',
        'security/ir.model.access.csv',
        'views/acuerdos_seguimiento_view.xml',
        'views/acuerdos_captura_view.xml',
        'views/acuerdos_responsables_view.xml',
        'views/acuerdos_sesiones_view.xml',
        'views/acuerdos_menu_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}