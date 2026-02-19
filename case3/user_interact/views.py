from django.http import HttpRequest
from django.shortcuts import render

from user_interact.forms import UserNameForm
from user_interact.service import save_provided_username


def index(request: HttpRequest):
    context = {"form": UserNameForm(), "username": None}

    if request.method == "POST":
        form = UserNameForm(request.POST)
        if form.is_valid():
            context["username"] = save_provided_username(form.cleaned_data["username"])
        else:
            context["form"] = form

    return render(request, "index.html", context)
