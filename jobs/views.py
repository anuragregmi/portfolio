from django.shortcuts import render
from .models import Job

# Create your views here.
def homepage(request):
    jobs = Job.objects.all()
    return render(request, "./jobs/index.html", {"jobs": jobs})