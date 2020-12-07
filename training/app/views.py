from django.shortcuts import render
from app.models import User
from app.forms import NewUser

# Create your views here.

def fun(request):
    dict = {'text':'go to /page'}
    return  render(request,'app/page1.html',context = dict)

# def fun2(request):
#     table = User.objects.all()
#     dict = {'table': table}
#     return render(request,'app/page2.html',context= dict)


def fun2(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return fun(request)
        else:
            print("error from invalid")
    return render(request,'app/page2.html',context = {'form':form})
