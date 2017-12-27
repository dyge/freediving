from django.views.generic import TemplateView
from django.shortcuts import render
from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DetailView

class CreateShop(LoginRequiredMixin, CreateView):
    form_class = forms.ShopForm
    model = models.Shop
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class CreateVerein(LoginRequiredMixin, CreateView):
    form_class = forms.VereinForm
    model = models.Verein
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class CreateEvent(LoginRequiredMixin, CreateView):
    form_class = forms.EventForm
    model = models.Event
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class CreateBuddy(LoginRequiredMixin, CreateView):
    form_class = forms.BuddyForm
    model = models.Buddy
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
