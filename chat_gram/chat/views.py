
from django.shortcuts import render
from .forms import ChatForm
from .models import ChatModel
from django.http import HttpResponseRedirect 
from django.urls import reverse

# Create your views here.
def index_view(request):
    form = ChatForm(request.POST or None)
    chat = ChatModel.objects.all()
    
    
    return render (request , 'index.html', {'form': form, 'chat': chat} )
def send_view(request):
    if request.POST:
        form = ChatForm(request.POST)
        if form.is_valid():
            user=request.user
            text = form.cleaned_data.get('text')
            chat_model = ChatModel(user=user, text=text)
            chat_model.save()
    return HttpResponseRedirect(reverse('index'))
