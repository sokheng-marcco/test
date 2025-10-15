from django.shortcuts import redirect

def instuctor_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('instuctor_id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper