from django.db import models

# Create your models here.
'''
定义和数据库表映射的类

在应用中的models.py文件中定义class
所有需要使用ORM的class都必须是 models.Model 的子类
class中的所有属性对应表格中的字段
字段的类型都必须使用 modles.xxx 不能使用python中的类型
字段常用参数

max_length : 规定数值的最大长度
blank : 是否允许字段为空,默认不允许
null : 在DB中控制是否保存为null, 默认为false
default : 默认值
unique : 唯一
verbose_name : 假名

'''
class myapp(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=200)
    # 定义后默认返回所有列表中的name值
    def __str__(self):
        return self.name

class school(models.Model):
    school_name = models.CharField(max_length=12)
    school_id = models.IntegerField()

    def __str__(self):
        return self.school_name

# 一对一的例子
class manager(models.Model):
    manager_id = models.IntegerField()
    manager_name = models.CharField(max_length=12)
#     建立一对一的关系，on_delete必须有值
    my_school = models.OneToOneField(school,on_delete=models.CASCADE)

    def __str__(self):
        return self.manager_name

# 一对多的例子
class teacher(models.Model):
    teacher_id = models.IntegerField()
    teacher_name =models.CharField(max_length=10)
#     建立一对多，一个school对应多个老师
    teacher_school = models.ForeignKey(school,on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher_name

#     多对多的例子
class student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=10)
#     建立多对多，多个学生多个老师
    stu_teacher = models.ManyToManyField(teacher)


    def __str__(self):
        return self.student_name





