from django.shortcuts import render, redirect


def index(request):
    return redirect('/shows')


def shows(request):
    context = {
        "all_shows": shows.objects.all()
    }
    return render(request, "shows.html", context)
