from django.shortcuts import render


def error_403(request, e):
    return render(request, 'errors/403.html')


def error_404(request, e):
    return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html')
