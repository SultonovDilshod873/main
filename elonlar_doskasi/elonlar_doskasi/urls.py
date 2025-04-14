from django.contrib import admin
from django.urls import path
from elonlar import views  # faqat 'elonlar' appdan import qilish yetarli

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.elon_list, name='elon_list'),  # bosh sahifa
]
