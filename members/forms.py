from django import forms
from .models import Member,Admin

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'



class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'