from django.urls import path
from admins import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("ebook",views.Ebookview.as_view()),
    path("ebook/<int:ebook_id>",views.EbookDetails.as_view()),
    path("users/accounts/signup",views.UserCreationView.as_view()),
    path("users/accounts/login",views.SignInView.as_view()),
    path('accounts/token/', obtain_auth_token)
]

