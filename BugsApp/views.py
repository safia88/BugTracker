from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from . import forms
from . models import Ticket
# Create your views here.

@login_required
def home(request):
    ticket_new=Ticket.objects.filter(status='FIRST')
    ticket_inprogress=Ticket.objects.filter(status='SECOND')
    ticket_done=Ticket.objects.filter(status='THIRD')
    context={'first':ticket_new,'second':ticket_inprogress,'third':ticket_done}
    return render(request,'home.html',context)

@login_required
def inserticket(request):
    form=forms.Ticketform()
    if request.method=='POST':
        form=forms.Ticketform(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.filed_by=request.user
            post.save()
            return redirect('home')
    return render(request,'insert.html',{'form':form})

@login_required
def ticket_edit(request,id):
    ticket=Ticket.objects.get(id=id)
    if request.method=='POST':
        form=forms.EditForm(request.POST,instance=ticket)
        if form.is_valid():
            post=form.save(commit=False)
            if post.assigned_to==None and post.completed_by==None and post.filed_by!=None:
                post.status='FIRST'
                post.save()
                return redirect(home)
            elif post.assigned_to!=None and post.completed_by==None:
                post.status='SECOND'
                post.save()
                return redirect(home)
            elif post.assigned_to!=None and post.completed_by!=None:
                post.status = 'THIRD'
                post.save()
                return redirect(home)
            post.save()
            return redirect(home)
    form=forms.EditForm(instance=ticket)
    return render(request,'ticket_edit.html',{'form':form})

@login_required
def set_invalid(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.status='FOURTH'
    ticket.save()
    return redirect(home)

@login_required
def assigned_you(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned_to=request.user
    ticket.status='SECOND'
    ticket.save()
    return redirect(home)

@login_required
def completed_you(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.completed_by=request.user
    ticket.status='THIRD'
    ticket.save()
    return redirect(home)

@login_required
def ticket_detail(request,id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'details.html', {'ticket': ticket})

@login_required
def signup(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_action(request):
    logout(request)
    return redirect(request.GET.get("next", reverse('login')))






















