from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .forms import CustomForm
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
    latest_Title_list = Title.objects.all()
    latest_Label_list = Label.objects.all()
    template = loader.get_template("courses/detailedCourse/daily_vocabulary.html")
    context = {
        "latest_Title_list": latest_Title_list,
        "latest_Label_list": latest_Label_list
    }
    return HttpResponse(template.render(context, request))


def custom_page(request):
    if request.method == 'POST':
        form = CustomForm(request.POST, request.FILES)
        if form.is_valid():
            title_name = request.POST.get('title', '')
            title, created = Title.objects.get_or_create(title=title_name)
            
            label_name = request.POST.get('label', '')
            label = Label(label=label_name, title=title)
            label.save()
            
            custom_data = CustomData(
                audio1=form.cleaned_data['audio1'],
                text1=form.cleaned_data['text1'],
                audio2=form.cleaned_data['audio2'],
                text2=form.cleaned_data['text2'],
                message=form.cleaned_data['message'],
                label=label
            )
            custom_data.save()
            return redirect('/courses/detailedCourse/custom_page/')
    else:
        custom_data = CustomData.objects.all().first()
        if custom_data:
            initial_text1 = custom_data.text1
            initial_text2 = custom_data.text2
            initial_message = custom_data.message
        else:
            initial_text1 = ''
            initial_text2 = ''
            initial_message = ''

        form = CustomForm()

    return render(request, 'courses/detailedCourse/custom_page.html', {
        'form': form,
        'initial_text1': initial_text1,
        'initial_text2': initial_text2,
        'initial_message': initial_message
    })
