from django.conf.urls import url
from authentification import views

urlpatterns = [
    url(r'^sign_up/$',views.sign_up,name="sign_up"),
]
