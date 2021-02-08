from django.shortcuts import render
from sw_app.models import Story
# Create your views here.

def index(request):
    all_story = Story.objects.all()
    return render(
        request,
        'display.html',
        context={},
    )
