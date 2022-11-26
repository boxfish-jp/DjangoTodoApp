from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Todo(models.Model):
    title = models.CharField("タスク名", max_length = 30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締切")
    frequency = models.IntegerField("通知の送信時間間隔", blank=True, default=24)
    mail = models.TextField("メール", blank=True)
    def __str__(self):
        return self.title
    