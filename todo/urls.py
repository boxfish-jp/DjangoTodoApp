from django.urls import path, include
from .views import TodoDelete, TodoDetail, TodoList, TodoCreate, TodoUpdate

urlpatterns = [
    path('', include('accounts.urls')),  #追加
    path("list/", TodoList.as_view(), name="list"), #変更
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    path("create/", TodoCreate.as_view(), name="create"),
    path("update/<int:pk>", TodoUpdate.as_view(), name="update"),
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"),
]