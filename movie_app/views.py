from django.shortcuts import render,redirect
from . models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    visited_movies = request.session.get('visited_movies',[])
    recently_visited = visited_movies[-3:]
    recently_visited_movies = Movies.objects.filter(id__in=recently_visited)

    visit = int(request.COOKIES.get('visit',0))
    visit = visit+1
    movies = Movies.objects.all()
    respons = render(request,'home.html',{'movies':movies,'visit':visit,'recently_visited_movies':recently_visited_movies})
    respons.set_cookie('visit',visit)
    return respons

@login_required(login_url='login')
def edit(request,pk):
    visited_movies = request.session.get('visited_movies',[])
    if pk in visited_movies :
        visited_movies.remove(pk)
        visited_movies.append(pk)
    else:
        visited_movies.append(pk)
    request.session['visited_movies'] = visited_movies
    movie = Movies.objects.get(pk=pk)
    form = MovieForm(instance=movie)
    if request.POST:
        form = MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'edit.html',{'form':form})
    return render(request,'edit.html',{'form':form})

@login_required(login_url='login')
def delete(request,pk):
    movie = Movies.objects.get(pk=pk)
    movie.delete()
    return redirect('home')

@login_required(login_url='login')
def create(request):
    form = MovieForm()
    if request.POST:
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("heil")
            print(form)
            print(form.errors)
            return redirect('home')
    return render(request,'create.html',{'form':form})

@login_required(login_url='login')    
def add_censor_info(request, pk):
    form = CensorInfoForm()
    movie = Movies.objects.get(pk=pk)
    if request.POST:
        form = CensorInfoForm(request.POST)
        if form.is_valid():
            info = form.save()
            movie.censor_details=info
            movie.save()
            return redirect('home')
    return render(request,'add_censor_info.html',{'form':form})

@login_required(login_url='login')
def add_director_name(request):
    directors = Director.objects.all()
    if request.POST:
        name = request.POST.get("name")
        director_obj = Director.objects.create(name=name)
        director_obj.save()
        return redirect('home')
    return render(request,'add_director_name.html',{'directors':directors})

@login_required(login_url='login')
def add_actor_name(request):
    actors = Actor.objects.all()
    if request.POST:
        name = request.POST.get('name')
        actor = Actor.objects.create(name=name)
        actor.save()
        return redirect('home')
    return render(request,'add_actor_name.html',{'actors':actors})


@never_cache
def sign_up(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
            login(request,user)
            return redirect('home')
        except :
            error = "username already taken."
            return render(request,'sign_up.html',{'error':error})
    return render(request,'sign_up.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user :
            login(request,user)
            return redirect('home')
        else :
            error = "Incorrect username or password."
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')