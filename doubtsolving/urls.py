from django.contrib import admin
from django.urls import path
from doubtsolving import views
urlpatterns = [
    path('about' ,views.about, name ="doubtsolving"),
    path('services' ,views.services, name ="doubtsolving"),
    path('bookfreedemo' ,views.bookfreedemo, name ="doubtsolving"),
    path('' ,views.index, name ="doubtsolving"),
]