from django.shortcuts import render
from .forms import ItemForm
from django.http import HttpResponse

# Create your views here.
def pageCount(request):
    count = request.session.get("count", 0)
    count += 1
    request.session["count"] = count
    return render(request, "cookieApp/count.html", {"count": count})

def index(request):
    return render(request, "sessionApp/index.html")

def displayCart(request):
    return render(request, "sessionApp/displayItems.html")

def addItem(request):
    form = ItemForm
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
    return render(request, "sessionApp/addItem.html", {"form": form})

def ExceptionView(request):
    raise Exception("This is an test exception")