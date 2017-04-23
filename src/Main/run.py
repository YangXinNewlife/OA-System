import time
from src.opt.query import Query
from src.opt.record import Record
from src.opt.delete import Delete
from src.opt.update import Update
class Run(object):
    def run(self):
        print "================================="
        print "=====      OA System        ====="
        print "=====           V1.0        ====="
        print "================================="
        print "                                 "
        time.sleep(2)
        print "Loding....."
        print "---------------------------------"
        time.sleep(2)
        print "Finish!"
        E_list = []
        print "Prepare DataBase Finish"
        print "---------------------------------"
        print "-- query     ## Show someone employee"
        print "-- queryAll  ## Show all employees"
        print "-- delete    ## Delete someone employee"
        print "-- record    ## Add a new employee"
        print "-- update    ## Update employee information"
        print "-- quit      ## Exit system"
        print "Please Type parameter :"
        while 1:
            type_content = raw_input()
            if type_content == "quit":
                print "You will quit System"
                print "Yes or No :"
                y_n_sure = raw_input()
                if y_n_sure == "Yes" or y_n_sure == 'Y' or y_n_sure == 'yes' or y_n_sure == 'y':
                    break
                print "Please Type parameter :"
            elif type_content == "queryAll":
                query_obj = Query()
                query_obj.queryAll(E_list)
                print "Please Type parameter :"
            elif type_content == "query":
                print "Employee SID: "
                sid = raw_input()
                query_one_obj = Query()
                query_one_obj.query(sid, E_list)
                print "Please Type parameter :"
            elif type_content == "record":
                record_obj = Record()
                print "please type employ sid:"
                E_sid = raw_input()
                print "please type employ name:"
                E_name = raw_input()
                print "please type employ sex:"
                E_sex = raw_input()
                print "please type employ salary:"
                E_salary = raw_input()
                record_obj.record(E_sid, E_name, E_sex, E_salary, E_list)
                print "Please Type parameter :"
            elif type_content == "delete":
                delete_obj = Delete()
                print "please type employ sid:"
                sid = raw_input()
                delete_obj.delete(sid, E_list)
                print "Please Type parameter :"
            elif type_content == "update":
                update_obj = Update()
                print "please type employ sid:"
                sid = raw_input()
                print "please type update content_type: "
                content_type = raw_input()
                print "please type update content: "
                content = raw_input()
                update_obj.update(sid, content_type, content, E_list)
                print "Please Type parameter :"

run1 = Run()
run1.run()

