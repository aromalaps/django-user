from django.http import HttpResponseForbidden
from .models import CustomUser

def staff_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.flag == CustomUser.STAFF:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not authorized to view this page.")
    return _wrapped_view_func

def staff_manager_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.flag == CustomUser.STAFF_MANAGER:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not authorized to view this page.")
    return _wrapped_view_func

def delivery_boy_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.flag == CustomUser.DELIVERY_BOY:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not authorized to view this page.")
    return _wrapped_view_func
