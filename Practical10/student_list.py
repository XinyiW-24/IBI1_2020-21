class Student(object):
    def __init__(self,first_name, last_name, undergraduate_programme):#https://blog.csdn.net/pdstar/article/details/90900944?utm_term=python%E4%B8%ADclass%E5%AE%9A%E4%B9%89&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-4-90900944&spm=3001.4430
        self.first_name=first_name#initialize first name
        self.last_name=last_name#initialize last name
        self.undergraduate_programme=undergraduate_programme##initialize undergraduate programme
    def attribute(self):  #print out first name, last name and undergraduate programme into one line
        print(self.first_name, self.last_name, self.undergraduate_programme)

#example 
student=Student('a','b','c')
student.attribute()
