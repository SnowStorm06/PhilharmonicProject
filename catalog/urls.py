from django.urls import path
from . import views

urlpatterns = [
    # Artist
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
    path('artists/create/', views.ArtistCreateView.as_view(), name='artist-create'),
    path('artists/<int:pk>/update/', views.ArtistUpdateView.as_view(), name='artist-update'),
    path('artists/<int:pk>/delete/', views.ArtistDeleteView.as_view(), name='artist-delete'),

    # Impresario
    path('impresarios/', views.ImpresarioListView.as_view(), name='impresario-list'),
    path('impresarios/<int:pk>/', views.ImpresarioDetailView.as_view(), name='impresario-detail'),
    path('impresarios/create/', views.ImpresarioCreateView.as_view(), name='impresario-create'),
    path('impresarios/<int:pk>/update/', views.ImpresarioUpdateView.as_view(), name='impresario-update'),
    path('impresarios/<int:pk>/delete/', views.ImpresarioDeleteView.as_view(), name='impresario-delete'),

    # Meropriyatie
    path('meropriyaties/', views.MeropriyatieListView.as_view(), name='meropriyatie-list'),
    path('meropriyaties/<int:pk>/', views.MeropriyatieDetailView.as_view(), name='meropriyatie-detail'),
    path('meropriyaties/create/', views.MeropriyatieCreateView.as_view(), name='meropriyatie-create'),
    path('meropriyaties/<int:pk>/update/', views.MeropriyatieUpdateView.as_view(), name='meropriyatie-update'),
    path('meropriyaties/<int:pk>/delete/', views.MeropriyatieDeleteView.as_view(), name='meropriyatie-delete'),

    # Soorujenie
    path('soorujenies/', views.SoorujenieListView.as_view(), name='soorujenie-list'),
    path('soorujenies/<int:pk>/', views.SoorujenieDetailView.as_view(), name='soorujenie-detail'),
    path('soorujenies/create/', views.SoorujenieCreateView.as_view(), name='soorujenie-create'),
    path('soorujenies/<int:pk>/update/', views.SoorujenieUpdateView.as_view(), name='soorujenie-update'),
    path('soorujenies/<int:pk>/delete/', views.SoorujenieDeleteView.as_view(), name='soorujenie-delete'),

    # Organizator
    path('organizators/', views.OrganizatorListView.as_view(), name='organizator-list'),
    path('organizators/<int:pk>/', views.OrganizatorDetailView.as_view(), name='organizator-detail'),
    path('organizators/create/', views.OrganizatorCreateView.as_view(), name='organizator-create'),
    path('organizators/<int:pk>/update/', views.OrganizatorUpdateView.as_view(), name='organizator-update'),
    path('organizators/<int:pk>/delete/', views.OrganizatorDeleteView.as_view(), name='organizator-delete'),
]