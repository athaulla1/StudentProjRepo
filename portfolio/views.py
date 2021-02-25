from django.shortcuts import render

# Create your views here.
def index(request):
    msg = {"Name": "Balaji","About":"I am 25yrs old runnng my own company"}
    #return render(request, 'index.html', msg)
    return render(request, 'index.html', {'msg':msg})
