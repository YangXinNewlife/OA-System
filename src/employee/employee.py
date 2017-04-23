class Employee(object):
    sid = None
    name = None
    sex = None
    salary = None

    def __init__(self, E_SID, E_name, E_sex, E_salary):
        self.sid = E_SID
        self.name = E_name
        self.sex = E_sex
        self.salary = E_salary
