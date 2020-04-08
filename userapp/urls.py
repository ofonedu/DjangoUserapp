from django.conf.urls import url
from userapp import views

#SET NAMESPACE!
app_name = 'userapp'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]