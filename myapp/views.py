from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    date = datetime.datetime.now()
    isActive=True
    name="VimalKuamr"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Rahul",
        'student_college':"ZYZ",
        'student_city':'LUCKNOW'
    }
    # return HttpResponse("<h1>Hello this is index page  </h1> "+str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    # print("test function is called from views")
    return render(request, "home.html", {})
    # return HttpResponse("<h1>Hello is index pages</h1>" +str(date))

def about(request):
    # return HttpResponse("<h1>this is about page</h1>")
    return render(request, "about.html", {})


def service(request):
    return render(request, "service.html", {})

    # return HttpResponse("<h1>this is service page</h1>")