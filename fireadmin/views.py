from django.shortcuts import render


# Create your views here.
from developenv import models


def index(request):
    return render(request, 'fireadmin/index.html')


def typography(request):
    return render(request, 'fireadmin/typography.html')


def content_widgets(request):
    return render(request, 'fireadmin/content-widgets.html')


def tables(request):
    status = models.carStatus.objects.all()
    return render(request, 'fireadmin/tables.html', {"status": status})


def form_elements(request):
    return render(request, 'fireadmin/form-elements.html')


def form_components(request):
    return render(request, 'fireadmin/form-components.html')


def form_examples(request):
    return render(request, 'fireadmin/form-examples.html')


def form_validation(request):
    return render(request, 'fireadmin/form-validation.html')


def buttons(request):
    return render(request, 'fireadmin/buttons.html')


def labels(request):
    return render(request, 'fireadmin/labels.html')


def images_icons(request):
    return render(request, 'fireadmin/images-icons.html')


def alerts(request):
    return render(request, 'fireadmin/alerts.html')


def media(request):
    return render(request, 'fireadmin/media.html')


def components(request):
    return render(request, 'fireadmin/components.html')


def other_components(request):
    return render(request, 'fireadmin/other-components.html')


def charts(request):
    return render(request, 'fireadmin/charts.html')


def file_manager(request):
    return render(request, 'fireadmin/file-manager.html')


def calendar(request):
    return render(request, 'fireadmin/calendar.html')


def list_view(request):
    return render(request, 'fireadmin/list-view.html')


def profile_page(request):
    return render(request, 'fireadmin/profile-page.html')


def messages(request):
    return render(request, 'fireadmin/messages.html')


def login(request):
    return render(request, 'fireadmin/login.html')


def notfound(request):
    return render(request, 'fireadmin/404.html')


def commands(request):
    return render(request, 'fireadmin/commands.html')
