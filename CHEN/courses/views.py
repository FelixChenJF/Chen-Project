import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import CustomForm, LabelForm, TitleForm
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
    error_message = None

    if request.method == 'POST':
        if 'delete_titles' in request.POST:
            titles_to_delete = request.POST.getlist('titles_to_delete')
            if titles_to_delete:
                Title.objects.filter(id__in=titles_to_delete).delete()
            return redirect('courses:daily_vocabulary')

        if 'delete_labels' in request.POST:
            labels_to_delete = request.POST.getlist('labels_to_delete')
            if labels_to_delete:
                Label.objects.filter(id__in=labels_to_delete).delete()
            return redirect('courses:daily_vocabulary')

        if 'title_form' in request.POST:
            title_form = TitleForm(request.POST)
            if title_form.is_valid():
                title_form.save()
                return redirect('courses:daily_vocabulary')
            label_form = LabelForm()

        elif 'label_form' in request.POST:
            label_form = LabelForm(request.POST)
            if label_form.is_valid():
                new_label = label_form.cleaned_data['label']
                if Label.objects.filter(label=new_label).exists():
                    error_message = f"The label '{new_label}' already exists."
                else:
                    label_form.save()
                    return redirect('courses:daily_vocabulary')
            title_form = TitleForm()

        elif 'edit_title' in request.POST:
            title_id = request.POST.get('title_id')
            new_title = request.POST.get('new_title')
            Title.objects.filter(id=title_id).update(title=new_title)
            return redirect('courses:daily_vocabulary')

        elif 'edit_label' in request.POST:
            label_id = request.POST.get('label_id')
            new_label = request.POST.get('new_label')
            if Label.objects.filter(label=new_label).exists():
                error_message = f"The label '{new_label}' already exists."
            else:
                Label.objects.filter(id=label_id).update(label=new_label)
            return redirect('courses:daily_vocabulary')

    else:
        title_form = TitleForm()
        label_form = LabelForm()

    latest_Title_list = Title.objects.all()
    latest_Label_list = Label.objects.all()
    
    context = {
        "latest_Title_list": latest_Title_list,
        "latest_Label_list": latest_Label_list,
        "title_form": title_form,
        "label_form": label_form,
        "error_message": error_message
    }
    
    return render(request, 'courses/detailedCourse/daily_vocabulary.html', context)

def custom_page(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            custom_data_list = data.get('customDataList', [])
            for custom_data in custom_data_list:
                try:
                    custom_data_obj = CustomData.objects.get(id=custom_data['id'])
                    custom_data_obj.text1 = custom_data['text1']
                    custom_data_obj.text2 = custom_data['text2']
                    custom_data_obj.message = custom_data['message']
                    custom_data_obj.save()
                except CustomData.DoesNotExist:
                    continue
            return JsonResponse({'status': 'success'})
        else:
            form = CustomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('courses:custom_page')

    else:
        form = CustomForm()

    label_name = request.GET.get('label')
    latest_CustomData_list = CustomData.objects.filter(label__label=label_name) if label_name else CustomData.objects.all()
    context = {
        'form': form,
        'latest_CustomData_list': latest_CustomData_list,
        'label_name': label_name,
    }
    return render(request, 'courses/detailedCourse/custom_page.html', context)

