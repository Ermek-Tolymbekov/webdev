from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views import (CompanyListAPIView, CompanyDetailAPIView, CompanyVacancyAPIView,
                       vacancy_list, get_vacancy, top_ten)


urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:pk>/vacancies/', CompanyVacancyAPIView.as_view()),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:id>/', get_vacancy),
    path('vacancies/top_ten/', top_ten),

    path('login/', obtain_jwt_token)
]