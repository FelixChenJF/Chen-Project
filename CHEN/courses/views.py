from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .forms import CustomForm, TitleForm
from .models import Course, CustomData, Title, Label

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
    if request.method == 'POST':
        if 'delete' in request.POST:
            titles_to_delete = request.POST.getlist('titles_to_delete')
            if titles_to_delete:
                Title.objects.filter(id__in=titles_to_delete).delete()
            return redirect('courses:daily_vocabulary')
        
        title_form = TitleForm(request.POST)
        if title_form.is_valid():
            title_form.save()
            return redirect('courses:daily_vocabulary')
    else:
        title_form = TitleForm()

    latest_Title_list = Title.objects.all()
    latest_Label_list = Label.objects.all()
    
    context = {
        "latest_Title_list": latest_Title_list,
        "latest_Label_list": latest_Label_list,
        "title_form": title_form
    }
    
    return render(request, 'courses/detailedCourse/daily_vocabulary.html', context)

def custom_page(request):
    label_name = request.GET.get('label')

    if label_name:
        label = Label.objects.get(label=label_name)
        latest_CustomData_list = label.custom_data.all()
    else:
        latest_CustomData_list = CustomData.objects.all()

    context = {
        "latest_CustomData_list": latest_CustomData_list,
        "Label_name": label_name,
    }
    return render(request, "courses/detailedCourse/custom_page.html", context)