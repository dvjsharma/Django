from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm

# 2 Views to check if the cookies are enabled in the browser
def Home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Setting the cookie page</h1>")

def afterHome(request):
    if request.session.test_cookie_worked():
        print("Cookies are enabled in your browser")
    request.session.delete_test_cookie()
    return HttpResponse("<h1>After setting the cookie page</h1>")

def countView(request):
    if "count" in request.COOKIES:
        count = int(request.COOKIES["count"]) + 1
    else :
        count = 1
    #instead returning the render, we will store that in response so that we can set cookie in it
    response = render(request, "cookieApp/count.html", {"count": count})
    response.set_cookie("count", count)
    return response

def index(request):
    return render(request, "cookieApp/index.html")

def displayCart(request):
    return render(request, "cookieApp/displayItems.html")

def addItem(request):
    form = ItemForm()
    response = render(request, "cookieApp/addItem.html", {"form": form})
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            quantity = form.cleaned_data["quantity"]
            response.set_cookie(name, quantity, 120)
    return response