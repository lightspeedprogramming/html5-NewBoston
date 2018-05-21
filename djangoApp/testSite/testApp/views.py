from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    groupDict = {}
    for grp in group.objects.all():
        groupDict[grp.num] = machine.objects.filter(myGroup=grp)
    return render(request, 'testApp/index.html', {'machines': machine.objects.all(),
                                                  'groupDict': groupDict,
                                                   })
