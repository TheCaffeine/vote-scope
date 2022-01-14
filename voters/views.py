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
    voters=Profile.objects.all().order_by('-id')
    


    return render(request, 'all-votes/index.html',{'profiles':profiles, voters:voters })

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

@login_required(login_url='/accounts/login/')
def create_form(request):
    current_user = request.user
    title = "Create vote"
    if request.method == 'POST':
        form = VotersForm(request.POST, request.FILES)
        if form.is_valid():
            voters = form.save(commit=False)
            voters.user = request.user
            voters.save()
        return HttpResponseRedirect('/')

    else:
            form = VotersForm()
    return render(request, 'all-votes/voters_form.html', {'form': form})


@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    voter=Votes.objects.filter(user_id=current_user.id).first()
    voters=Profile.objects.all().order_by('-id')

    ctx = {"profile": profile, 'profiles':profiles, 'voter':voter}
    return render(request, "all-votes/profile.html", ctx)

@login_required(login_url="/accounts/login/")
def voters_member(request):
    voters_id=request.user.id
    location = request.user.profile.location
    print(location)
    # vote_count=Votes.objects.all().count()
    
    votes=Votes.objects.all()
    # voters=Profile.objects.get(voters_id=voters_id)
    
    # county=Votes.objects.filter(votes=voters)
    return render(request,'all-votes/voter.html', { 'votes':votes, 'vote_count':votes.count()})
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
