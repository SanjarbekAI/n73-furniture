from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'shared/404.html', status=404)


def handler403(request, exception):
    return render(request, 'shared/403.html', status=403)


def handler500(request):
    return render(request, 'shared/500.html', status=500)
