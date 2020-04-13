from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from designer.forms import UserForm, ProfileForm, ProjectForm, StatementForm
from .models import Project, Statement

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def home(request):
    # return render(request, 'designer/sign_in.html', {})
    print(request.POST)
    print(request.GET)
    return redirect(authapp_home)


@login_required(login_url='/designer/sign_in')
def authapp_home(request):
    print(request.POST)
    print(request.GET)
    return render(request, 'designer/projects.html', {})


def authapp_sign_up(request):
    print(request.POST)
    user_form = UserForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        print('user_form.is_valid()', user_form.is_valid())
        print('profile_form.is_valid()', profile_form.is_valid())

        if user_form.is_valid() and profile_form.is_valid():
            print(' i m here')
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            )

            login(request, user)

            return redirect(authapp_home)

    return render(request, 'designer/sign_up.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


def new_project(request):
    print(request.POST)

    if request.method == 'POST':
        user = {'user': str(request.user.pk)}
        response = request.POST.copy()
        response.update(user)

        print('res', response)
        project_form = ProjectForm(response)

        print('project_form.is_valid', project_form.is_valid())

        if project_form.is_valid():
            # new_project = project_form.save(commit=False)
            # creator = request.user
            # new_project.user = creator
            project_form.save()
            statement_form = StatementForm()
            return render(request, 'designer/statement.html', {
                'statement_form': statement_form,
            })
        else:
            print(project_form.errors)

    project_form = ProjectForm()
    return render(request, 'designer/newproject.html', {
        'project_form': project_form,
    })


def statement(request):

    if request.method == 'POST':
        print(request.POST)

        statement_form = StatementForm(request.POST)
        print('statement_form.is_valid()', statement_form.is_valid())
        if statement_form.is_valid():
            print('here')

    statement_form = StatementForm()
    return render(request, 'designer/statement.html', {
        'statement_form': statement_form,
    })