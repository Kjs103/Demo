from django.urls import path
from . import views

#app_name='polls'

urlpatterns={
    path('',views.toLogin_view),
    path('index/',views.Login_view),
    path('toregister/',views.toregister_view),
    path('register/',views.register_view),
    path('test1/',views.test1_view),
    path('totest1/',views.totest1_view),

}