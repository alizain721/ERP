from rolepermissions.roles import AbstractUserRole


class Employee(AstractUserRole):
    '''This is the role class for normal users'''

    available_permissions = {
        'get_projects': True,
    }
