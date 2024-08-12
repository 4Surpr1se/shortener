from urllib.parse import urlparse

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect

from main.models import ShortedURL
from main.utils import random_url


def index(request):
    context = {'full_path': request.build_absolute_uri()}
    if request.method == 'GET':
        return render(request, 'index.html', context)
    if request.method == 'POST':
        try:
            url = request.POST['url']
            short_url = request.POST['short_url']
            ShortedURL.objects.create(url=url, short_url=short_url)
            context.update({'success': True, 'shorted_url': short_url})
            return render(request, 'index.html', context)
        except (IntegrityError, Exception) as e:
            if isinstance(e, IntegrityError):
                context.update({'error': True, 'error_description': f'URL {short_url} уже занят'})
            else:
                context.update({'error': True, 'error_description': repr(e)})
            return render(request, 'index.html', context)


def redirector(request, redirect_url):
    try:
        url = ShortedURL.objects.get(short_url=redirect_url).url
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = f'//{url}'
        return redirect(url)
    except ObjectDoesNotExist:
        return render(request, 'redirect_error.html', {'url': request.build_absolute_uri(redirect_url)})


def random_url_view(request):
    return JsonResponse({'url': random_url()})
