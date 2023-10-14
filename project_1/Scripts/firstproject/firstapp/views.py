from django.shortcuts import render,HttpResponse

# Create your views here.

ulist=[]

def home(request):
    return render(request,'home.html')

def first_page(request):
    return render(request,'first.html')

def second_page(request):
    return render(request,'second.html')

def adduser(request):
    return render(request,'adduser.html')

def Add_User(request):
    id=request.GET.get('id')
    name=request.GET.get('name')
    email=request.GET.get('email')
    contact=request.GET.get('contact')
    address=request.GET.get('address')
    t=(id,name,email,contact,address)
   # return HttpResponse('<h1>Success'+str(t)+'</h1>')
    ulist.append(t)
    return render(request,'home.html')


def adduser1(request):
    return render(request,'adduser1.html')

def Add_User1(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    address=request.POST.get('address')
    t=(id,name,email,contact,address)
    # return HttpResponse('<h1>Success'+str(t)+'</h1>')
    ulist.append(t)
    return render(request,'home.html')

def User_list(request):
    return render(request, 'ulist.html',{'l':ulist})
