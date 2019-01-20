from django.urls import path, include
from apps.todo import endpoints

app_name = 'todo'
urlpatterns = [
    path('todo/lists/', endpoints.ColumnListAPIView.as_view()),
    # path('todo/lists/create', endpoints.ListsCreateAPIView.as_view())
    path('tasks/archive/<int:pk>/', endpoints.ArchiveTaskAPIVView.as_view()),
    path('tasks/create/', endpoints.CreateTaskAPIView.as_view()),
    path('tasks/move/<int:pk>/', endpoints.MoveTaskAPIView.as_view()),
    path('tasks/edit/<int:pk>/', endpoints.EditTaskAPIView.as_view()),
]
