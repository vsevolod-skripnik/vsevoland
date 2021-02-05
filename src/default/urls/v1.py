from django.urls import include, path

app_name = 'api_v1'
urlpatterns = [
    path('comics/', include('comics.urls')),
    path('users/', include('users.urls')),
    path('healthchecks/', include('django_healthchecks.urls')),
]
