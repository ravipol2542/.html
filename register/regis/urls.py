from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login_view, name ="login"),
    path('logout',views.logout_view,name = "logout"),
    path('classcourse',views.classcourse,name="classcourse"),
    path('studentinfo/<str:username>',views.studentinfo,name="student_info"),
    path('enroll',views.enroll, name = "enroll")

]