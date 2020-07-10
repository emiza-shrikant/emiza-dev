{
        "name" : "College Management",
        "version" : "1.1",
        "depends" : ['base','sale','crm'],
        "author" : "PalnetOdoo",
        "description": """
        managing college daily activities
        """,
        "website" : "www.planetodoo.net",
        'images': [],
        "category" : "college management",
        'summary': 'Base Module For All E-Commerce Modules-v13',
        "demo" : [],
        "data" : [
        'security/ir.model.access.csv',
        'data/bonus_line.xml',
        'data/pipeline_stages.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/department_view.xml',
        # 'views/library_view.xml',
        'views/book.xml'
                ],
        'auto_install': False,
        "installable": True,
}