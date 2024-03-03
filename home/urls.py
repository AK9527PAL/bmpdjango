from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.Contact,name='contact'),
    path('timetable1',views.timetable1,name='timetable1'),
    path('timetable2',views.timetable2,name='timetable2'),
    path('timetable3',views.timetable3,name='timetable3'),
    path('timetable4',views.timetable4,name='timetable4'),
    path('preprimary',views.preprimary,name='timetable4'),
    path('Middle',views.Middle,name='Middle'),
    path('Secondary',views.Secondary,name='Secondary'),
    path('Srsecondary',views.Srsecondary,name='Srsecondary'),
    path('Rules',views.Rules,name='Rules'),
    path('Tc',views.Tc,name='Tc'),
    path('Admission-Procedure',views.Admission_Procedure,name='Admission-Procedure'),
    path('Fee-Structure',views.Fee_Structure,name='Fee-Structure'),
    path('Admission-Form',views.Admission_Form,name='Admission-Form'),
    path('developer',views.developer,name='developer'),

]