from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse, JsonResponse
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
    label_name = request.GET.get('label', None)
    custom_data = None
    
    if label_name:
        try:
            label = Label.objects.get(label=label_name)
            custom_data = CustomData.objects.filter(label=label).first()
        except Label.DoesNotExist:
            pass

    if request.method == 'POST':
        form = CustomForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data and save it to the database
            if custom_data:
                custom_data.text1 = form.cleaned_data['text1']
                custom_data.text2 = form.cleaned_data['text2']
                custom_data.message = form.cleaned_data['message']
                if 'audio1' in request.FILES:
                    custom_data.audio1 = request.FILES['audio1']
                if 'audio2' in request.FILES:
                    custom_data.audio2 = request.FILES['audio2']
                custom_data.save()
            else:
                # Create a new CustomData object if it doesn't exist
                label = Label.objects.get_or_create(label=label_name)[0]
                CustomData.objects.create(
                    label=label,
                    text1=form.cleaned_data['text1'],
                    text2=form.cleaned_data['text2'],
                    message=form.cleaned_data['message'],
                    audio1=request.FILES.get('audio1', None),
                    audio2=request.FILES.get('audio2', None)
                )
            # Return a JSON response indicating success
            return JsonResponse({'success': True})
        else:
            # Return a JSON response indicating form errors
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        # Prepare initial form data
        initial_data = {
            'text1': custom_data.text1 if custom_data else '',
            'text2': custom_data.text2 if custom_data else '',
            'message': custom_data.message if custom_data else ''
        }
        form = CustomForm(initial=initial_data)

    return render(request, 'courses/detailedCourse/custom_page.html', {
        'form': form,
        'initial_text1': initial_data['text1'],
        'initial_text2': initial_data['text2'],
        'initial_message': initial_data['message']
    })