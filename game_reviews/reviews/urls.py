from django.urls import path, re_path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # User identification
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Game URLs
    re_path(r'^add-game/$', views.add_game, name='add_game'),
    path('game/<int:game_id>/', views.game_profile, name='game_profile'),

    # User profile
    path('<str:username>/', views.user_profile, name='user_profile'),
    #re_path(r'^edit-profile/$', views.edit_profile, name='edit_profile'), - beta

    # Reviews URLs
    path('add-review/<int:game_id>/', views.add_review, name='add_review'),
]