from django.urls import path
from .views import OsList, OsDetail

urlpatterns = [
    path('', OsList.as_view()),
    path('<int:pk>/',OsDetail.as_view()),
]