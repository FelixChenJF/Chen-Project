from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import Course, Title, Label

def homePage(request):
    latest_course_list = Course.objects.all()
    template = loader.get_template("courses/homePage.html")
    context = {
        "latest_course_list": latest_course_list,
    }
    return HttpResponse(template.render(context, request))

def SEPage(request):

    return render(request, 'courses/detailedCourse/SEPage.html')

def CEPage(request):

    return render(request, 'courses/detailedCourse/CEPage.html')

def DSPage(request):

    return render(request, 'courses/detailedCourse/DSPage.html')

def SPPage(request):

    return render(request, 'courses/detailedCourse/SPPage.html')

def OSPage(request):

    return render(request, 'courses/detailedCourse/OSPage.html')

def EDPage(request):

    return render(request, 'courses/detailedCourse/EDPage.html')

def technical_terms(request):
    
    return render(request, 'courses/detailedCourse/technical_terms.html')

def daily_vocabulary(request):
    latest_Title_list = Title.objects.all()
    latest_Label_list = Label.objects.all()
    template = loader.get_template("courses/detailedCourse/daily_vocabulary.html")
    context = {
        "latest_Title_list": latest_Title_list,
        "latest_Label_list": latest_Label_list
    }
    return HttpResponse(template.render(context, request))


def custom_page(request):
    label = request.GET.get('label', '')
    content = get_content_based_on_label(label)
    template = loader.get_template("courses/detailedCourse/custom_page.html")
    context = {
        "label_content": content
    }
    return HttpResponse(template.render(context, request))

def get_content_based_on_label(label):
    return f"{label}"
