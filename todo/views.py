from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo

#下記は追加したもの
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class TodoCreate(CreateView):
    model = Todo
    fields = ['title', 'description', 'deadline', 'frequency']
    success_url = reverse_lazy("list")
    def form_valid(self, form):
        form.instance.mail = self.request.user.email
        return super().form_valid(form)

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title', 'description', 'deadline', 'frequency']
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")
