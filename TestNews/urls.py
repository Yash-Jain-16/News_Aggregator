
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('busi/',views.business,name="business"),
    path("enter/",views.entertainment,name="entertainment"),
    path("health/",views.health,name="health"),
    path("science/",views.science,name="science"),
    path("sports/",views.sports,name="sports"),
    path("technology/",views.technology,name="technology"),
    path("contact/",views.contact,name="contact"),
    path("myfeed/",views.myfeed,name="myfeed"),
    path("myfeedreply",views.myfeedreply,name="myfeedreply"),
    path("prompt/",views.prompt,name="prompt"),
    path("savebookmark",views.SaveBookmark,name="SaveBookmark"),
    path("display/",views.display,name="display"),
    path("deletebookmark",views.deletebookmark,name="deletebookmark"),
]