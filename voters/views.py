from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from voters.forms import ProfileForm, UpdateProfileForm
from .models import *

# Create your views here.


@login_required(login_url="/accounts/login/")
def index(request):
    return render(request, 'all-votes/index.html')

@login_required(login_url="/accounts/login/")
def FAQ(request):
    if 'FAQ' in request.GET and request.GET["FAQ"]:
        FAQ = request.GET.get("FAQ")
        
        message = f"Here are the FAQs"

        return render(request, "all-votes/FAQ.html", {"message": message, "FAQ": FAQ})
    # else:
    #     message = "You haven't searched for any term"
    #     return render(request, "search.html", {"message": message})
    
@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
     

    return render(request, "all-votes/profile.html")

@login_required(login_url="/accounts/login/")
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'all-votes/create_profile.html', {"form": form, "title": title})

@login_required(login_url="/accounts/login/")
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'all-votes/update_profile.html', ctx)