from django.urls import path
from . import views

urlpatterns = [
    path('',view=views.home, name='home'),
    path('login/',view=views.login_view, name='login'),
    path('logout/',view=views.logout_view, name='logout'),
    path('register/',view=views.signup, name='signup'),
    
    #check base html
    path('base/', view=views.base, name='base'),

    path('addcustomer/', view=views.addcustomer, name='addcustomer'),
    path('update/<int:pk>/', view=views.updatecustomer, name='update'),
    path('delete/<int:pk>/', view=views.delete, name='delete'),
]