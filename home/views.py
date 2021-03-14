from django.shortcuts import render
from .models import orders
from .forms import OrderForm


def home_index(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = OrderForm()
        return render(request, 'index.html', {'form': form})
def index(request):
    form=OrderForm()
    return render(request,'index.html',{'form':form})


