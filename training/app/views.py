from django.shortcuts import render
from app.models import User

# Create your views here.

def fun(request):
    dict = {'text':'go to /page'}
    return  render(request,'app/page1.html',context = dict)

def fun2(request):
    table = User.objects.all()
    dict = {'table': table}
    return render(request,'app/page2.html',context= dict)
