from django.urls import path, include


app_name = 'api'
urlpatterns = [
    path('', include('apps.accounts.urls')),
    path('', include('apps.todo.urls')),

]
