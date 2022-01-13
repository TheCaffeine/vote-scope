from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

# Create your views here.


def index(request):
    return render(request, 'all-votes/index.html')

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    


    return render(request, 'all-votes/index.html',{'profiles':profiles, })

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        
        
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('index')
        
        else:
            form = ProfileForm()
    return render(request, 'all-votes/create_profile.html', {'form': form})

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    profiles = Profile.objects.filter(user_id = current_user.id).all()

    ctx = {"profile": profile, 'profiles':profiles}
    return render(request, "all-votes/profile.html", ctx)

# def FAQ(request):
#     if 'FAQ' in request.GET and request.GET["FAQ"]:
#         FAQ = request.GET.get("FAQ")
        
#         message = f"Here are the FAQs"

#         return render(request, "all-votes/FAQ.html", {"message": message, "FAQ": FAQ})
#     # else:
#     #     message = "You haven't searched for any term"
#     #     return render(request, "search.html", {"message": message})


# def votes(request):
   
#     votes = Votes.objects.all().order_by('-id')

#     context ={'votes':Votes}
#     return render(request, 'all-votes/voters.html', context)


# def create_vote(request):
#     current_user = request.user
#     if request.method == 'POST':
#         vote_form = votersForm(request.POST, request.FILES)
#         if vote_form.is_valid():

#             vote = vote_form.save(commit=False)
#             vote.user = current_user
#             vote.save()
        
#         return HttpResponseRedirect('/votes')

#     else:
#         vote_form = votersForm()


#     context = {'vote_form':vote_form}
#     return render(request, 'allcreate_vote.html',context)
