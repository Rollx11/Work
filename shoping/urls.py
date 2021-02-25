from django.urls import path
import shoping.views as v


urlpatterns = [
    path('', v.main, name="main"),
    path('drink', v.drinks, name='drink'),

    path('about', v.about, name="about"),

    path('login', v.logins, name="login"),

    path('register', v.register, name='register'),

    path('logout', v.logout_view, name='logout'),

    path('searchs', v.searchs, name='searchs'),





]