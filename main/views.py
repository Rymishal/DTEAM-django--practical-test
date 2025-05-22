from django.shortcuts import render, get_object_or_404

from .models import CV


def home_view(request):
    cvs = CV.objects.select_related('contacts').prefetch_related('skills', 'projects').all()
    return render(request, 'home.html', {'cvs': cvs})


def cv_view(request, pk):
    cv = get_object_or_404(CV.objects.select_related('contacts').prefetch_related('skills', 'projects'), pk=pk)
    return render(request, 'cv.html', {'cv': cv})
