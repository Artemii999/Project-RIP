from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articles'
urlpatterns = [
    path('', views.main, name='home'),
    path('list/', views.list, name='list'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('hello', views.hello, name='hello'),
]