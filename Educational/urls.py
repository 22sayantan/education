from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('oldUser',views.oldUsers,name='oldUser'),
    path('newUser',views.newUser,name='newUser'),
    path('new_data',views.new_data,name='new_data'),
    path('newQues',views.newQues,name='newQues'),
    path('mockTest',views.mockTest,name='mockTest'),
    path('courses',views.courses,name='courses'),
    path('new_courses',views.new_courses,name='new_courses'),
    path('invoice',views.invoice,name='invoice'),
    path('sales',views.sales,name='sales'),
    path('submit_form',views.submit_form,name='submit_form'),

]