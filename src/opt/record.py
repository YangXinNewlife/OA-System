from src.employee.employee import Employee
class Record(object):
    def record(self, sid, name, sex, salary, E_list):
        employee_obj = Employee(sid, name, sex, salary)
        E_list.append(employee_obj)



