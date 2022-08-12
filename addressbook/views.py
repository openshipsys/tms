from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .forms import PersonForm
from .models import Person

# Create your views here.


class HtmxMixIn:
    def success_template(self):
        return NotImplemented

    def get_template_names(self):
        if self.request.htmx:
            self.template_name_suffix += "_partial"

        return super().get_template_names()

    def form_valid(self, form):
        if self.request.htmx:
            context = {"form": form, "object": self.object}
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
            messages.add_message(self.request, messages.SUCCESS, self.success_message)

            return render(self.request, self.success_template, context)
        else:
            return super().form_valid(form)


class PersonFormCreateView(SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    success_message = "Created"
    success_template = "addressbook/person_detail_partial.html"


class PersonFormUpdateView(HtmxMixIn, SuccessMessageMixin, UpdateView):
    model = Person
    form_class = PersonForm
    success_message = "Updated"
    success_template = "addressbook/person_detail_partial.html"


class PersonFormDetailView(HtmxMixIn, SuccessMessageMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "addressbook/person_detail.html"


class PartyTemplateView(TemplateView):
    template_name = "addressbook/party_navigation.html"
