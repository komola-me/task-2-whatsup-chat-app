from django.urls import path
from chat.views import ChatListView, ChatDetailView
urlpatterns = [
    path("chat/", ChatListView.as_view()),
    path('chat/<int:id>/messages/', ChatDetailView.as_view()),
    

]