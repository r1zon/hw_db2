from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    student_list = Student.objects.prefetch_related('teacher')
    context = {'student_list': student_list}
    return render(request, template, context)
