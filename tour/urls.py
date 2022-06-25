
from django.urls import path
from tour import views
app_name = 'tour'
urlpatterns = [
    path('country/', views.countrycreate.as_view(), name="country"),
    path('', views.countryselect.as_view(), name="countrys"),
    path('countryu/<pk>/', views.countryupdate.as_view(), name="countryu"),
    path('countryd/<pk>/', views.countrydelete.as_view(), name="countryd"),


    path('state/', views.statecreate.as_view(), name="state"),
    path('stateu/<pk>/', views.stateupdate.as_view(), name="stateu"),
    path('stated/<pk>/', views.statedelete.as_view(), name="stated"),


    path('city/', views.citycreate.as_view(), name="city"),
    path('citys/', views.cityselect.as_view(), name="citys"),
    path('cityu/<pk>/', views.cityupdate.as_view(), name="cityu"),
    path('cityd/<pk>/', views.citydelete.as_view(), name="cityd"),

    path('success/', views.successview.as_view(), name="success"),
    path('selectstate/<pk>/', views.selectstate, name="selectstate"),
    path('selectcity/<pk>/', views.selectcity, name="selectcity"),
    path('show/', views.show, name="show"),


    path('citydetails/', views.citydetailscreate.as_view(), name="citydetails"),
    path('citygallary/', views.citygallarycreate, name="citygallary"),
    path('citygallaryselect/<pk>/',
         views.citygallaryselect, name="citygallaryselect"),


]
