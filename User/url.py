from django.conf.urls import url
from .import views

urlpatterns =[
    url(r'^login/$',views.login_user, name='login_user'),
<<<<<<< HEAD
    url(r'^logout/$',views.logout_user, name='logout'),
=======
    url(r'^logout/$',views.logout_user, name='logout_user'),
>>>>>>> e1806eb2a5c959dadc82846c06cb49e9aecd7797
    url(r'^signup/$',views.signup_user, name='signup_user'),
]