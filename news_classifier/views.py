from django.shortcuts import render

from .forms import NewsForm
from ml_model.predict import predict_news

def index(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news_text = form.cleaned_data['news_text']
            result = predict_news(news_text)
            return render(request, 'news_classifier/result.html', {'result': result})
    else:
        form = NewsForm()
    return render(request, 'news_classifier/index.html', {'form': form})
# Create your views here.
