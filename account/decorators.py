from django.http import HttpResponse
from django.shortcuts import redirect
from django import template
register = template.Library()


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=()):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                for groups in request.user.groups.all():    # проверяем все имена групп
                    group = groups.name
                    if group in allowed_roles:              # проверка ролей
                        return view_func(request, *args, **kwargs)
                return HttpResponse('No access')
        return wrapper_func
    return decorator
