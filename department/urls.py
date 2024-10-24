from django.urls import path
from department import views

urlpatterns=[
    path('',views.homep,name='homepage'),
    path('about',views.aboutp,name='aboutpage'),
    path('contact',views.contactp,name='contactpage'),
    path('login',views.loginp,name='loginpage'),
    path('profile',views.profilep,name='profilepage'),
    path('register',views.registerp,name='registerpage'),
    path('single',views.singlep,name='singlepage'),
    path('update/<int:rid>',views.updatep,name="update"),
    path('delete/<int:rid>',views.deletep,name="delete"),
    path('logout',views.logoutp,name="logoutpage"),
    path('batch',views.batchp,name='batchpage'),
    path('display/<int:rid>',views.displayp,name="displaypage"),
    path('batch1',views.batch1p,name='batch1page'),
    path('batch2',views.batch2p,name='batch2page'),
    path('batch3',views.batch3p,name='batch3page'),


   

]

