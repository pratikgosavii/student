from django.db import models

# Create your models here.



class addteacher(models.Model):
    Teacher_Name=models.CharField(max_length=50, default='sd')
    Teacher_Subjects=models.ForeignKey('subjects', on_delete=models.CASCADE, default=1)
    Teacher_Subjects_Code=models.CharField(max_length=50, default='sd')
    Teacher_Username=models.CharField(max_length=50, default='sd')
    Teacher_Password=models.CharField(max_length=50, default='sd')

    

class addcourse(models.Model):
    Student_Name=models.CharField(max_length=50)
    Course_Name=models.CharField(max_length=50)


class addstudent(models.Model):
    Student_Registerd_No=models.CharField(max_length=50)
    Student_Name=models.CharField(max_length=50)
    Student_Roll_NO=models.CharField(max_length=50)
    Student_Mobile_No=models.CharField(max_length=50)

class Add_Student_Registerd_Cources(models.Model):
    Student_Roll_No=models.CharField(max_length=50)
    Student_Registerd_Subject=models.CharField(max_length=50)

class subjects(models.Model):
    Subject_Name=models.CharField(max_length=50)


    def __str__(self):
        return self.Subject_Name
