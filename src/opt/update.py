class Update(object):
    def update(self, sid, content_type, content, E_list):
        for i in E_list:
            if i.sid == sid:
                if content_type == "name":
                    i.name = content
                elif content_type == "sex":
                    i.sex = content
                elif content_type == "salary":
                    i.salary = content

