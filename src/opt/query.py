class Query(object):
    def query(self, sid, E_list):
        for i in E_list:
            if i.sid == sid:
                print ("SID : " + i.sid)
                print ("Name : " + i.name)
                print ("Sex : " + i.sex)
                print ("Salary : " + i.salary)



    def queryAll(self, E_list):
        if len(E_list) == 0:
            print "now don't have any employee"
        else:
            print "now Total Employees: " + str(len(E_list))
            for i in E_list:
                print "====================="
                print ("| SID : " + i.sid)
                print ("| Name : " + i.name)
                print ("| Sex : " + i.sex)
                print ("| Salary : " + i.salary)
                print "======================="




