from django.urls import path
from .views import chatbot_response, chatbot_page

urlpatterns = [
    path('chatbot/', chatbot_response, name='chatbot_response'),
    path('', chatbot_page, name='chatbot_page'),  # Home page
    path('', chatbot_page, name='chatbot_page'),
]

