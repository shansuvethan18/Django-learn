from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login" ),
    path("logout/", views.logoutUser, name="logout" ),
    path("register/", views.registerPage, name="register" ),
    path("home/", views.home, name="home" ),
    path("room/<int:pk>/", views.room, name="room" ),
    path('create-room/', views.createRoom,name="create-room"),
    path('update-room/<str:pk>', views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>', views.deleteMessage,name="delete-message"),

    path('sample/', views.samplePage,name="sample"),
    path('sample2/', views.samplePage2,name="sample2")
]
