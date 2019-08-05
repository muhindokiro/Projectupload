from django.shortcuts import render,redirect
import datetime as dt
from .models import Project
from .email import send_welcome_email
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,NewsLetterForm,RegisterForm


# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# @login_required(login_url='/accounts/login/')
def project_today(request):
    projecthub = Project.todays_project()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            send_welcome_email(name,email)
            HttpResponseRedirect('project_today')
    else:
        form = NewsLetterForm()
    return render(request, 'all-projects/today-project.html', {"projecthub":projecthub,"letterForm":form})


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Project.search_by_project_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message})

# @login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('projectToday')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

def register(request):
   if request.method == "POST":
       form = UserRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           email = form.cleaned_data['email']
           send_welcome_email(username,email)
           return redirect('all_posts/today_ig.html')
   else:
       form =RegisterForm()
   return render(request,'registration/registration_form.html',{'form':form})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
  