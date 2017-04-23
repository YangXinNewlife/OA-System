from src.opt.query import Query
class Delete():
    def delete(self, sid, E_list):
        for i in E_list:
            if i.sid == sid:
                print "deleteing"
                print " Y or N:"
                y_n_sure = raw_input()
                if y_n_sure == 'Y':
                    E_list.remove(i)


