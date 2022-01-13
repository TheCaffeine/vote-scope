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
    
