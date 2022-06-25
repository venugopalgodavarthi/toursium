from django.urls import path
from authe import views
app_name='authe'
urlpatterns = [
    path('register/',views.registerview.as_view(),name="register"),
    path('success/',views.successview,name="success"),
    path('login/',views.loginview.as_view(),name="login"),
    path('logout/',views.logoutview,name="logout"),
]
