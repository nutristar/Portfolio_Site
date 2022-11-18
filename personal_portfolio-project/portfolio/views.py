from django.shortcuts import render

# Create your views here.
def home(request):
    # r=request.GET.get("rot")
    return render(request, "home2.html")

def pirozochek(request):
    r=request.GET.get("rot")
    return render(request, "home.html", {"rrr":r})