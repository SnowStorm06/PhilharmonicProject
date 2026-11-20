from django.contrib import admin
from .models import (
    Pol, Janri, TipSoorujenia, Nagrada,
    Artist, Impresario, Organizator, Soorujenie,
    Meropriyatie, RabotaSImpresario,
    UchastieArtistovVMeropriyatii, Nagrajdeniya,
)

admin.site.register(Pol)
admin.site.register(Janri)
admin.site.register(TipSoorujenia)
admin.site.register(Nagrada)
admin.site.register(Artist)
admin.site.register(Impresario)
admin.site.register(Organizator)
admin.site.register(Soorujenie)
admin.site.register(Meropriyatie)
admin.site.register(RabotaSImpresario)
admin.site.register(UchastieArtistovVMeropriyatii)
admin.site.register(Nagrajdeniya)