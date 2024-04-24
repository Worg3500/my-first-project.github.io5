from django.shortcuts import render
from  .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView

def news_home(request):
    news = Artiles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

class NewDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'article'



def create(request):
    form = ArtilesForm
    data = {
        'form': form
    }

    return render(request, 'news/create.html' )