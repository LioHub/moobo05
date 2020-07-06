# /usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from .models import Project, Statement


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('city', 'number', 'job', 'quantity_of_workers')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # fields = ('user', 'name', 'location', 'name_of_customer', 'email_of_customer',
        #           'number_of_customer', 'price_of_project')
        fields = ('user', 'name')


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ('project', 'room', 'images', 'product_name', 'link', 'unit', 'retail_price', 'qty',
                  'total_client_price', 'file_3dmax', 'file_revit', 'file_technical_instruction')
        # fields = ('project', 'room', 'images', 'product_name', 'product_type', 'application_room', 'link',
        #           'model', 'retail_price', 'client_discount', 'designer_discount', 'qty', 'total_client_price',
        #           'supplier', 'aviability_of_stock', 'file_3dmax', 'file_revit', 'file_technical_instruction',
        #           'client_approved')