from django.shortcuts import redirect

# fontion de Kevin Bonga
# definition permettant d'autoriser une liste de groupes prédéfini.
def allowed_users(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_groups:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('gererproduit')
        return wrapper_func
    return decorator