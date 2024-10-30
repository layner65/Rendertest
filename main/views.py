from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def page2(request):
    return render(request, 'main/page2.html')


from django.shortcuts import render


