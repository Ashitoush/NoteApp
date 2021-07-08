from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from noteData.models import NoteData
from noteData.forms import NoteDataSave


# Create your views here

def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('signin')
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def signin(request):
    form = LoginForm()
    context = {
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'signin.html', context)
    else:
        email_ = request.POST['email']
        password_ = request.POST['password']
        user = authenticate(request, email=email_, password=password_)
        if user is not None:
            login(request, user)
            return redirect('userProfile')
        else:
            messages.add_message(request, messages.ERROR, "Username and password does not match")
        return render(request, 'signin.html', context)


@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def userProfile(request):
    note = NoteData.objects.filter(user=request.user)
    context = {
        'note': note
    }
    return render(request, 'userProfile.html', context)


@login_required(login_url='signin')
def addNote(request):
    form = NoteDataSave(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.user = request.user
        data.save()
        messages.add_message(request, messages.SUCCESS, "Added Successfully!")
        return redirect('userProfile')
    context = {
        'form': form
    }
    return render(request, 'addNote.html', context)


@login_required(login_url='signin')
def edit(request, id):
    pass


@login_required(login_url='signin')
def readmore(request, id):
    data = get_object_or_404(NoteData, id=id)
    context = {
        'data': data
    }
    return render(request, 'details.html', context)


@login_required(login_url='signin')
def delete(request, id):
    data = NoteData.objects.filter(id=id)
    data.delete()
    messages.add_message(request, messages.SUCCESS, "Deleted Sucessfully!")
    return redirect('userProfile')


@login_required(login_url='signin')
def edit(request, id):
    data = NoteData.objects.get(id=id)
    form = NoteDataSave(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Updated Successfully!")
        return redirect('userProfile')

    context = {
        'form': form
    }
    return render(request, 'edit.html', context)
