from django.views.generic import DetailView, ListView

from card.models import Card


class CardListView(ListView):
    model = Card
    paginate_by = 10


class CardDetailView(DetailView):
    model = Card
