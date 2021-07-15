from django.urls import path
from . import views
app_name= "book"


urlpatterns=[
    path('display/',views.display,name="display"),
    path('',views.form,name="form"),
     path('filter/',views.filter,name="filter")
    
]
