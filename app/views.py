import datetime

from django.shortcuts import render
from app.models import Data
from app.forms import DataForm

def index_view(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'] 
            date = form.cleaned_data['date'] 
        item = Data(
            name=name,
            date=date,
        )
        item.save()
    else:
        form = DataForm()

    return render(request, 'index.html', {'form': form})


def datatables_net(request):
    items = Data.objects.values()
    
    formatted_data = []
    
    for item in items:
        formatted_data.append({
            'name': item['name'],
            'date': item['date'].strftime('%Y-%m-%d_%H:%M')
        })
    data ={
        "data": formatted_data,
    }
    return render(request, "datatables.html", data)