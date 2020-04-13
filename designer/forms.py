from django.contrib.auth.models import User
from django import forms
# from authapp.models import PizzaShop
from .models import Profile, Project, Statement


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'number', 'job', 'quantity_of_workers')


class ProjectForm(forms.ModelForm):
    # user = forms.IntegerField(required=True, initial='')
    #
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("request")
    #     super(ProjectForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].label = "Пользователь:"
    #     self.fields['user'].initial = self.request.user

    class Meta:
        model = Project
        fields = ('user', 'name', 'location', 'name_of_customer', 'email_of_customer',
                  'number_of_customer', 'price_of_project')


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ('project', 'room', 'images', 'product_name', 'product_type', 'application_room', 'link',
                  'model', 'retail_price', 'client_discount', 'designer_discount', 'qty', 'total_client_price',
                  'supplier', 'aviability_of_stock', 'file_3dmax', 'file_revit', 'file_technical_instruction',
                  'client_approved')