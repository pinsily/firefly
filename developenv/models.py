from django.db import models


# Create your models here.

class carStatus(models.Model):
    car_id = models.CharField(max_length=10, verbose_name="唯一标识ID")  #
    goal = models.CharField(max_length=10, verbose_name='目标地址代码')  # 0
    path_start = models.CharField(max_length=10)  # 0
    path_end = models.CharField(max_length=10)  # 0
    box = models.CharField(max_length=255)  # ['0'] * box_quantity
    created_time = models.DateField(auto_now=True)
    nav_status = models.CharField(max_length=10)  # 0
    nav_service = models.CharField(max_length=10)  # 0
    nav_location = models.CharField(max_length=255)  # [0., 0., 0.]

    class Meta:
        db_table = 'carstatus'

    def __str__(self):
        return "[{0}]-{1}".format(self.car_id, self.nav_location)


class Command(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='小车编号')
    type = models.CharField(max_length=1, verbose_name='命令类型')          # 对应一个参数类型表，前端实现数据字典管理
    param_1 = models.CharField(max_length=1, verbose_name='参数1')
    param_2 = models.CharField(max_length=1, verbose_name='参数2')
    is_accept = models.CharField(max_length=1, verbose_name='是否接受')

    class Meta:
        db_table = 'command'

    def __str__(self):
        return "[{0}]-{1}".format(self.id, self.type)


