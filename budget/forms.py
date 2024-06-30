from django import forms

from budget.models import Expense,Income

from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):

    class Meta:

        model=Expense

        exclude=("id","created_date","user_object")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control border-info"}),

            "amount":forms.NumberInput(attrs={"class":"form-control border-info"}),

            "category":forms.Select(attrs={"class":"form-control form-select border-info"}),

            # "owner":forms.TextInput(attrs={"class":"form-control border-info"}),

            "priority":forms.Select(attrs={"class":"form-control form-select border-info"})

          }
        

        

class IncomeForm(forms.ModelForm):

    class Meta:

        model=Income

        exclude=("id","created_date","user_object")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control border-info"}),

            "amount":forms.NumberInput(attrs={"class":"form-control border-info"}),

            "category":forms.Select(attrs={"class":"form-control form-select border-info"}),

            # "owner":forms.TextInput(attrs={"class":"form-control border-info"})

        }            
  


class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","password"]   

        widgets={

           "username":forms.TextInput(attrs={"class":"form-control border-info"}),

            "email":forms.EmailInput(attrs={"class":"form-control border-info"}),

            "password":forms.PasswordInput(attrs={"class":"form-control border-info"})


        }



class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border-info"}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border-info"}))       


class summaryForm(forms.Form):

    start_date=forms.DateTimeField(widget=forms.DateInput(attrs={"class":"form-control border-info mb-4","type":"date"}))    

    end_date=forms.DateTimeField(widget=forms.DateInput(attrs={"class":"form-control border-info mb-4","type":"date"}))  
