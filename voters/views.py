from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/accounts/login/")
def index(request):
    return render(request, 'all-votes/index.html')