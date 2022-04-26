from . import views
from django.urls import path

app_name = "lettings"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
