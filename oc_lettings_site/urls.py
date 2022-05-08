from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views


def trigger_error(request):
    # division_by_zero = 1 / 0
    pass


app_name = 'oc_lettings_site'


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
]
