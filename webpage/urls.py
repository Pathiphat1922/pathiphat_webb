from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("contact/", views.contactPage, name="contact"),
    path('for_test/', views.forPage, name="for_test"),
    path("card_template/", views.cardPage, name="card_template"),
    path("cardcolor/", views.cardColorPage, name="card_color"),
    path("form/", views.formPage, name="form"),

]
