from django.http import JsonResponse
from django.shortcuts import render

from developenv import models
from . import command

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'developenv/index.html')


def car_status(request):
    return render(request, 'developenv/status.html')


@csrf_exempt
def car_command(request):
    if request.is_ajax():
        car = request.POST['car']
        car_type = request.POST['car_type']
        param_1 = request.POST['param_1']
        param_2 = request.POST['param_2']

        data = {
            "car": car,
            "car_type": car_type,
            "param_1": param_1,
            "param_2": param_2,
        }

        ret_data = {'ret_code': '200', 'ret_message': '接收成功!'}

        flag = command.accept_command(data)
        if flag:
            # 存储命令
            models.Command.objects.create(type=car_type, param_1=param_1, param_2=param_2, is_accept="1")
            return JsonResponse(ret_data)
        else:
            # 失败命令
            models.Command.objects.create(type=car_type, param_1=param_1, param_2=param_2, is_accept="0")
            ret_data['ret_code'] = '300'
            ret_data['ret_message'] = '接收失败!'
            return JsonResponse(ret_data)

    return render(request, 'developenv/command.html')
