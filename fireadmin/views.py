from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from developenv import models
from fireadmin import command


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


@csrf_exempt
def commands(request):
    if request.is_ajax():
        car = request.POST['car']
        command_type = request.POST['command_type']
        param_1 = request.POST['param_1']
        param_2 = request.POST['param_2']

        data = {
            "car": car,
            "command_type": command_type,
            "param_1": param_1,
            "param_2": param_2,
        }

        ret_data = {
            'ret_code': '200',
            'ret_message': '接收成功!',
            "car": car,
            "command_type": command_type,
            "param_1": param_1,
            "param_2": param_2,
            "is_accept": "1",
        }

        flag = command.accept_command(data)
        if flag:
            # 存储命令
            models.Command.objects.create(type=command_type, param_1=param_1, param_2=param_2, is_accept="1")
            return JsonResponse(ret_data)
        else:
            # 失败命令
            models.Command.objects.create(type=command_type, param_1=param_1, param_2=param_2, is_accept="0")
            ret_data['ret_code'] = '300'
            ret_data['ret_message'] = '接收失败!'
            ret_data["is_accept"] = "0"
            return JsonResponse(ret_data)

    command_list = models.Command.objects.all()

    return render(request, 'fireadmin/commands.html', {"command_list": command_list})
