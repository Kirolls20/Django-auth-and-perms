from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
   path('login/',v.LoginView.as_view(template_name='registration/login.html'),name='login'),
   path('logout/',v.LogoutView.as_view(),name='logout'),
   path('sign-up/',views.sign_up,name='sign_up'),
   path('create-post',views.create_post,name='create_post')
]
