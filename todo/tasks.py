from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings  # 追加
from django.core.mail import send_mail   # 追加
from .models import Todo

def update():# 任意の関数名
    # ここに定期実行したい処理を記述する
    query_set = Todo.objects.filter(deadline=date.today())
    list_search = list(query_set.values())
    today_title = [d["title"] for d in list_search]
    today_description = [d["description"] for d in list_search]
    today_mail = [d["mail"] for d in list_search]
    today_frequency = [d["frequency"] for d in list_search]
    send(today_title,today_description,today_mail,today_frequency)
    
    

def send(title,description,mail,frequency):
    for i in range(len(title)):
        subject = "todoアプリからの通知"
        message = "タイトル[" + str(title[i]) + "]" + "詳細[" + str(description[i]) + "]" + "は今日までです"
        from_email = []
        recipient_list = [mail[i]]
        if(int(datetime.now().hour) % int(frequency[i]) == 0):
            send_mail(subject, message, from_email, recipient_list)
        elif(int(datetime.now().hour) == 7):
            send_mail(subject, message, from_email, recipient_list)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', seconds=30, start_date=None)
    scheduler.start()

