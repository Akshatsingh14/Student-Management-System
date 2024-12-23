from django.shortcuts import render, redirect
from .models import Sdata
from django.http import HttpResponse

# Create your views here.

details = Sdata.objects.all()

def index(request):
    query = request.GET.get('search','')
    if query :
        details = Sdata.objects.filter(Name__icontains=query)
    else:
        details = Sdata.objects.all()

    context = {
        'student': details
    }
    return render(request,'index.html',context)

def pyspiders(request):
    
    context = {
        'student' : details
    }
    return render(request,'pyspiders.html',context)

def qspiders(request):
    
    context = {
        'student' : details
    }
    return render(request,'qspiders.html',context)

def jspiders(request):
    
    context = {
        'student' : details
    }
    return render(request,'jspiders.html',context)

def prospiders(request):
    
    context = {
        'student' : details
    }
    return render(request,'prospiders.html',context)

# def sngdetail(request, pk):
#     data = Sdata.objects.get(id = pk)
#     context = {
#         'data' : data
#     }
#     return render(request,'sng.html',context)

def sngdetail(request,pk):
    try:
        data = Sdata.objects.get(id = pk)
    except Sdata.DoesNotExist:
        return HttpResponse("Student data not present", status=404) 
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    context = {
        'data' : data
    }
    return render(request,'sng.html',context)

def update(request, pk2):
    data1 = Sdata.objects.get(id = pk2)
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Qualification = request.POST.get('Qualification')
        Gender = request.POST.get('Gender')
        YOP = request.POST.get('YOP')
        Age = request.POST.get('Age')
        Skills = request.POST.get('Skills')
        Address = request.POST.get('Address')
        Mock_Rating = request.POST.get('Mock_Rating')
        Department = request.POST.get('Department')
        
        data1.Name = Name
        data1.Qualification = Qualification
        data1.Gender = Gender
        data1.YOP = YOP
        data1.Age = Age
        data1.Skills = Skills
        data1.Address = Address
        data1.Mock_Rating = Mock_Rating
        data1.Department = Department
        data1.save()
        return redirect("index")

    context = {
        'data1' : data1
    }
    return render(request,'edit.html',context)

def create(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Qualification = request.POST.get('Qualification')
        Gender = request.POST.get('Gender')
        YOP = request.POST.get('YOP')
        Age = request.POST.get('Age')
        DOB = request.POST.get('DOB')
        Skills = request.POST.get('Skills')
        Address = request.POST.get('Address')
        Mock_Rating = request.POST.get('Mock_Rating')
        Department = request.POST.get('Department')
        a = Sdata.objects.create(Name = Name, Qualification = Qualification, Gender = Gender, 
        YOP = YOP, Age = Age, DOB = DOB, Skills = Skills, Address = Address, Mock_Rating = Mock_Rating, Department = Department)
        print(Name,Gender,YOP,Address,Department)
        return redirect("index")

    return render(request,'add.html')