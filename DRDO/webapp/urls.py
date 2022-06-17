from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name='Index'),
    path('Mumbai/',views.Mumbai, name='Mumbai'),
    path('Ques/',views.Ques, name='Ques'),
    path('CourseAnalysis/',views.CourseAnalysis, name='CourseAnalysis'),

]