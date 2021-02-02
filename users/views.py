from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm # from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Tweet, Profile # Importing tweet model
from django.contrib.auth.models import User # Import User model to display users in 'alluser' view
from django.views.generic import ListView, DetailView, CreateView, DeleteView # Importing Django's create, delete, update views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# User registration view
def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'title': 'Register', 'form': form})

def allusers(request):
    return render(request, 'users/allusers.html', {'users': User.objects.all()})

# Class based views
class Dashboard(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'users/dashboard.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.all().order_by('-date_posted')

class ComposeTweet(LoginRequiredMixin, CreateView):
    model = Tweet
    template_name = 'users/compose.html'
    fields = ['message']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TweetDetail(LoginRequiredMixin, DetailView):
    template_name = 'users/tweet_detail.html'
    context_object_name = 'tweet'
    model = Tweet

@login_required
def profile(request, **kwargs):
    user_profile = User.objects.get(username=kwargs['username'])
    tweets = Tweet.objects.all().order_by('-date_posted')

    context = {
        'title': user_profile.username, 
        'tweets': tweets,
        'user_profile': user_profile
    }

    return render(request, 'users/profile.html', context)
        
@login_required
def settings(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # return redirect('profile', kwargs={'username': request.user.username})
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'settings',
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/settings.html', context)


