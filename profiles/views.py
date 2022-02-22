from django.shortcuts import render
from .models import Professor,Department
# Create your views here.


def professor(request):
    departments = Department.objects.all()
    context = {
        "title": "الاستاذة",
        "departments": departments,
    }
    return render(request,"profiles/professor.html",context)