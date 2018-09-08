# -*- coding: utf-8 -*-


def accept_command(command):
    car = command['car']
    car_type = command['car_type']
    param_1 = command['param_1']
    param_2 = command['param_2']

    print(car, car_type, param_1, param_2)

    # 即接口处理函数
    # 调用方法后根据返回的参数返回是否接受命令成功，暂定为成功
    flag = True

    return flag
