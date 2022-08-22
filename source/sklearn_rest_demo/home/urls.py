from django.urls import path
from home.pages.start_page import StartPage
from home.pages.record_page import RecordsPage


urlpatterns = [
    path('start/', StartPage().as_view()),
    path('records/', RecordsPage().as_view()),
]
