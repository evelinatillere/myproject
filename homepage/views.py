from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import EmailForm

def index_view(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "homepage/home.html", {})

def home_view(request):
    return render(request, "homepage/home.html", {})

def git_view(request):
    return render(request, "homepage/git.html", {})

def form_view(request):
        # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = request.POST.get("email", "")
            text = request.POST.get("text", "")
            send_mail(
                f"Saņemta ziņa no mājaslapas sūtītājs: {email}",
                text,
                "tillers.test@gmail.com",
                ["evelina.tillere@gmail.com"],
                fail_silently=False,)

            return render(request, "homepage/thanks.html", {})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, "homepage/form.html", {"form": form})

def send_email_view(request, email, text):
        send_mail(
        f"Saņemta ziņa no mājaslapas sūtītājs: {email}",
        text,
        "tillers.test@gmail.com",
        ["evelina.tillere@gmail.com"],
        fail_silently=False,
)