from django.urls import path
from card.views import CardListView, CardDetailView


app_name = 'card'

urlpatterns = [
    path('', CardListView.as_view(), name='card_list'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card_detail'),
]
