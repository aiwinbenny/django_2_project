from django.shortcuts import render

# Create your views here.

def fun(request):
    dict = {'text':'go to /page'}
    return  render(request,'app/page1.html',context = dict)
