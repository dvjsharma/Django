"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from templatesApp import views
from empApp import views as empViews
from formsApp import views as formViews
from fbvApp import views as fbvViews
from cbvApp import views as cbvViews
from cookiesApp import views as cookiesViews
from sessionApp import views as sessionViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("firstApp/", include("firstApp.urls")),
    path("quoteApp/", include("quoteApp.urls")),
    path("firstTemplate/", views.renderTemplate),
    path("employeeInfo/", views.employee),
    path("employeeDb/", empViews.emploteedata),
    path("userRegisteration/", formViews.userRegisterationView),
    path("listProjects/", formViews.listProjects),
    path("addProjects/", formViews.addProject),
    # path("", formViews.index),
    path("index-fbv/", fbvViews.getStudent),
    path("index-fbv/create", fbvViews.createStudent),
    path("index-fbv/delete/<int:id>", fbvViews.deleteStudent),
    path("index-fbv/update/<int:id>", fbvViews.updateStudent),
    path("index-cbv/", cbvViews.GreetingView.as_view()),
    path("index-cbv/students", cbvViews.StudentListView.as_view(), name="students"),
    path("index-cbv/students/<int:pk>", cbvViews.StudentDetailView.as_view(), name="detail"),
    path("index-cbv/students/create/", cbvViews.StudentCreateView.as_view()),
    path("index-cbv/students/update/<int:pk>", cbvViews.StudentUpdateView.as_view()),
    path("index-cbv/students/delete/<int:pk>", cbvViews.StudentDeleteView.as_view()),
    path("home/", cookiesViews.Home),
    path("afterHome/", cookiesViews.afterHome),
    # path("count/", cookiesViews.countView),
    # path("", cookiesViews.index),
    # path("addItem/", cookiesViews.addItem),
    # path("displayItems/", cookiesViews.displayCart)
    path("count/", sessionViews.pageCount),
    path("", sessionViews.index),
    path("addItem/", sessionViews.addItem),
    path("displayItems/", sessionViews.displayCart),
    path("exception/", sessionViews.ExceptionView),
    path("accounts/", include("django.contrib.auth.urls")), #should be /accounts only as there are lot of views already attached to it
]
