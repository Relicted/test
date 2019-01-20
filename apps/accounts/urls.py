from django.urls import path, include


app_name = 'accounts'
urlpatterns = [

    # Rest Auth:
    path('rest-auth/', include('rest_auth.urls')),
    # Rest Auth Registration:
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # All Auth:
    path('account/', include('allauth.urls')),
]
