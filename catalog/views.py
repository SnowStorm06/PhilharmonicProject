from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Artist, Impresario, Meropriyatie, Soorujenie, Organizator


# ---------- Artist ----------
class ArtistListView(ListView):
    model = Artist
    template_name = 'catalog/artist_list.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'catalog/artist_detail.html'


class ArtistCreateView(CreateView):
    model = Artist
    fields = ['imya', 'vozrast', 'obrazovanie', 'staj', 'pol', 'photo']
    template_name = 'catalog/artist_form.html'
    success_url = reverse_lazy('artist-list')


class ArtistUpdateView(UpdateView):
    model = Artist
    fields = ['imya', 'vozrast', 'obrazovanie', 'staj', 'pol', 'photo']
    template_name = 'catalog/artist_form.html'
    success_url = reverse_lazy('artist-list')


class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'catalog/artist_confirm_delete.html'
    success_url = reverse_lazy('artist-list')


# ---------- Impresario ----------
class ImpresarioListView(ListView):
    model = Impresario
    template_name = 'catalog/impresario_list.html'
    context_object_name = 'impresarios'


class ImpresarioDetailView(DetailView):
    model = Impresario
    template_name = 'catalog/impresario_detail.html'


class ImpresarioCreateView(CreateView):
    model = Impresario
    fields = ['imya', 'vozvrast', 'pol']
    template_name = 'catalog/impresario_form.html'
    success_url = reverse_lazy('impresario-list')


class ImpresarioUpdateView(UpdateView):
    model = Impresario
    fields = ['imya', 'vozvrast', 'pol']
    template_name = 'catalog/impresario_form.html'
    success_url = reverse_lazy('impresario-list')


class ImpresarioDeleteView(DeleteView):
    model = Impresario
    template_name = 'catalog/impresario_confirm_delete.html'
    success_url = reverse_lazy('impresario-list')


# ---------- Meropriyatie ----------
class MeropriyatieListView(ListView):
    model = Meropriyatie
    template_name = 'catalog/meropriyatie_list.html'
    context_object_name = 'meropriyaties'


class MeropriyatieDetailView(DetailView):
    model = Meropriyatie
    template_name = 'catalog/meropriyatie_detail.html'


class MeropriyatieCreateView(CreateView):
    model = Meropriyatie
    fields = ['nazvanie', 'data', 'organizator', 'soorujenie']
    template_name = 'catalog/meropriyatie_form.html'
    success_url = reverse_lazy('meropriyatie-list')


class MeropriyatieUpdateView(UpdateView):
    model = Meropriyatie
    fields = ['nazvanie', 'data', 'organizator', 'soorujenie']
    template_name = 'catalog/meropriyatie_form.html'
    success_url = reverse_lazy('meropriyatie-list')


class MeropriyatieDeleteView(DeleteView):
    model = Meropriyatie
    template_name = 'catalog/meropriyatie_confirm_delete.html'
    success_url = reverse_lazy('meropriyatie-list')


# ---------- Soorujenie ----------
class SoorujenieListView(ListView):
    model = Soorujenie
    template_name = 'catalog/soorujenie_list.html'
    context_object_name = 'soorujenies'


class SoorujenieDetailView(DetailView):
    model = Soorujenie
    template_name = 'catalog/soorujenie_detail.html'


class SoorujenieCreateView(CreateView):
    model = Soorujenie
    fields = ['nazvanie', 'vmestitelnost', 'atribute', 'tip_soorujenia', 'photo']
    template_name = 'catalog/soorujenie_form.html'
    success_url = reverse_lazy('soorujenie-list')


class SoorujenieUpdateView(UpdateView):
    model = Soorujenie
    fields = ['nazvanie', 'vmestitelnost', 'atribute', 'tip_soorujenia', 'photo']
    template_name = 'catalog/soorujenie_form.html'
    success_url = reverse_lazy('soorujenie-list')


class SoorujenieDeleteView(DeleteView):
    model = Soorujenie
    template_name = 'catalog/soorujenie_confirm_delete.html'
    success_url = reverse_lazy('soorujenie-list')


# ---------- Organizator ----------
class OrganizatorListView(ListView):
    model = Organizator
    template_name = 'catalog/organizator_list.html'
    context_object_name = 'organizators'


class OrganizatorDetailView(DetailView):
    model = Organizator
    template_name = 'catalog/organizator_detail.html'


class OrganizatorCreateView(CreateView):
    model = Organizator
    fields = ['nazvanie', 'forma_sobstvennosti', 'vid_organizatora']
    template_name = 'catalog/organizator_form.html'
    success_url = reverse_lazy('organizator-list')


class OrganizatorUpdateView(UpdateView):
    model = Organizator
    fields = ['nazvanie', 'forma_sobstvennosti', 'vid_organizatora']
    template_name = 'catalog/organizator_form.html'
    success_url = reverse_lazy('organizator-list')


class OrganizatorDeleteView(DeleteView):
    model = Organizator
    template_name = 'catalog/organizator_confirm_delete.html'
    success_url = reverse_lazy('organizator-list')