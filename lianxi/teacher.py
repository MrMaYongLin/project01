

"""
属性有：姓名，年龄，课程
方法有：教育
"""
class Teacher():
    def __init__(self, name, sex, course):
        self.name = name
        self.sex = sex
        self.course = course

    def teach(self):
        print(f'{self.name}老师，性别是{self.sex},教{self.course}课程')

tea = Teacher("门", "女", "生物")
tea.teach()
