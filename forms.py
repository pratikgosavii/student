from django import forms
from .models import addteacher,addstudent,subjects








class addstudent_form(forms.ModelForm):
    Student_Registration_no=forms.CharField(widget=forms.TextInput())
    Student_Name=forms.CharField(widget=forms.TextInput())
    Student_roll_no=forms.CharField(widget=forms.TextInput())
    Student_mobile_no=forms.CharField(widget=forms.TextInput())
   
    
    class Meta():
        model = addstudent
        fields = ['Student_Registration_no','Student_Name','Student_roll_no','Student_mobile_no']


class addsubject_form(forms.ModelForm):
    Subject_Name=forms.CharField(widget=forms.TextInput(),required=True)

    class Meta():
        model=subjects
        fields = ['Subject_Name']
   



class addteacher_form(forms.ModelForm):
    Teacher_Name = forms.CharField(widget=forms.TextInput())
    Teacher_Subjects = forms.ModelChoiceField(queryset=subjects.objects.all())
    Teacher_Subjects_Code = forms.CharField(widget=forms.TextInput())
    Teacher_Username = forms.CharField(widget=forms.TextInput())
    Teacher_Password = forms.CharField(widget=forms.TextInput())


    class Meta():
        model=addteacher
        fields = ['Teacher_Name','Teacher_Subjects','Teacher_Subjects_Code','Teacher_Username','Teacher_Password']
        
          
