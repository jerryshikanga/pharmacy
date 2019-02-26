from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
class UserCreateView(FormView):
    form_class = UserCreationForm
    # success_url = reverse("index")
    success_url = "/"
    template_name = "registration/user_create_form.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(UserCreateView, self).form_valid(form)
