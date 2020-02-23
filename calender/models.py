import datetime
from django.db import models
from django.utils import timezone

class plan(models.Model):
    #予定
    plan_do         = models.CharField('WHAT',max_length=50)
    plan_when       = models.CharField('WHEN',max_length=5)
    plan_where      = models.CharField('WHERE',max_length=50)
    calender_year   = models.IntegerField(4)
    calender_month  = models.IntegerField(2)
    calender_day    = models.IntegerField(2)


"""class Schedule(models.Model):
    """スケジュール"""
    summary      = models.CharField('概要', max_length=50)
    description  = models.TextField('詳細な説明', blank=True)
    start_time   = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time     = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date         = models.DateField('日付')
    created_at   = models.DateTimeField('作成日', default=timezone.now)"""

    def __str__(self):
        return self.summary