from django.conf.urls import url
from authentification import views

urlpatterns = [
    url(r'^sign_up/$',views.sign_up,name="sign_up"),
    url(r'^log_out/$',views.log_out,name="log_out"),
    url(r'^login/$',views.login,name="login"),
]
