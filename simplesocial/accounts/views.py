from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    # We're not executing the class so we don't use
    # forms.UserCreateForm() instead we're setting
    # the class form_class to forms.UserCreateForm
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
