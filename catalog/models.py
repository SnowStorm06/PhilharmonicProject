from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Pol(models.Model):
    """Пол (pol)"""
    pol = models.CharField(max_length=7, verbose_name="Пол")

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"
        db_table = "pol"

    def __str__(self):
        return self.pol


class Janri(models.Model):
    """Жанр (janri)"""
    tip = models.CharField(max_length=11, verbose_name="Тип жанра")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        db_table = "janri"

    def __str__(self):
        return self.tip


class TipSoorujenia(models.Model):
    """Тип сооружения (tipsoorujenia)"""
    tip = models.CharField(max_length=20, verbose_name="Тип сооружения")

    class Meta:
        verbose_name = "Тип сооружения"
        verbose_name_plural = "Типы сооружений"
        db_table = "tipsoorujenia"

    def __str__(self):
        return self.tip


class Nagrada(models.Model):
    """Награда (nagrada)"""
    tip = models.CharField(max_length=20, verbose_name="Тип награды")

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"
        db_table = "nagrada"

    def __str__(self):
        return self.tip


class Artist(models.Model):
    """Артист (artisti) — с фото"""
    imya = models.CharField(max_length=60, verbose_name="Имя артиста")
    vozrast = models.IntegerField(
        verbose_name="Возраст",
        validators=[MinValueValidator(16), MaxValueValidator(80)]
    )
    obrazovanie = models.CharField(max_length=60, verbose_name="Образование")
    staj = models.IntegerField(verbose_name="Стаж")
    pol = models.ForeignKey(Pol, on_delete=models.CASCADE, verbose_name="Пол")
    photo = models.ImageField(
        upload_to='artists/', verbose_name="Фото артиста",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"
        db_table = "artisti"

    def __str__(self):
        return self.imya

    def get_absolute_url(self):
        return reverse('artist-detail', args=[str(self.id)])


class Impresario(models.Model):
    """Импресарио (impresario)"""
    imya = models.CharField(max_length=60, verbose_name="Имя импресарио")
    vozvrast = models.IntegerField(
        verbose_name="Возраст",
        validators=[MinValueValidator(21), MaxValueValidator(70)]
    )
    pol = models.ForeignKey(Pol, on_delete=models.CASCADE, verbose_name="Пол")

    class Meta:
        verbose_name = "Импресарио"
        verbose_name_plural = "Импресарио"
        db_table = "impresario"

    def __str__(self):
        return self.imya

    def get_absolute_url(self):
        return reverse('impresario-detail', args=[str(self.id)])


class Organizator(models.Model):
    """Организатор (organizator)"""
    nazvanie = models.CharField(max_length=20, verbose_name="Название")
    forma_sobstvennosti = models.CharField(max_length=20, verbose_name="Форма собственности")
    vid_organizatora = models.CharField(max_length=20, verbose_name="Вид организатора")

    class Meta:
        verbose_name = "Организатор"
        verbose_name_plural = "Организаторы"
        db_table = "organizator"

    def __str__(self):
        return self.nazvanie

    def get_absolute_url(self):
        return reverse('organizator-detail', args=[str(self.id)])


class Soorujenie(models.Model):
    """Сооружение (soorujenia) — с фото"""
    nazvanie = models.CharField(max_length=60, verbose_name="Название сооружения")
    vmestitelnost = models.IntegerField(
        verbose_name="Вместимость",
        validators=[MinValueValidator(1)]
    )
    atribute = models.CharField(max_length=100, verbose_name="Атрибуты")
    tip_soorujenia = models.ForeignKey(
        TipSoorujenia, on_delete=models.CASCADE, verbose_name="Тип сооружения"
    )
    photo = models.ImageField(
        upload_to='soorujenia/', verbose_name="Фото сооружения",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Сооружение"
        verbose_name_plural = "Сооружения"
        db_table = "soorujenia"

    def __str__(self):
        return self.nazvanie

    def get_absolute_url(self):
        return reverse('soorujenie-detail', args=[str(self.id)])


class Meropriyatie(models.Model):
    """Мероприятие (meropriyatie)"""
    nazvanie = models.CharField(max_length=60, verbose_name="Название мероприятия")
    data = models.DateField(verbose_name="Дата проведения")
    organizator = models.ForeignKey(
        Organizator, on_delete=models.CASCADE, verbose_name="Организатор"
    )
    soorujenie = models.ForeignKey(
        Soorujenie, on_delete=models.CASCADE, verbose_name="Сооружение"
    )

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        db_table = "meropriyatie"

    def __str__(self):
        return self.nazvanie

    def get_absolute_url(self):
        return reverse('meropriyatie-detail', args=[str(self.id)])


# ---------- Оставшиеся таблицы (для полноты 8+ сущностей, без CRUD) ----------

class RabotaSImpresario(models.Model):
    """Работа с импресарио (rabotasimpresario)"""
    data = models.DateField(verbose_name="Дата договора")
    janri = models.ForeignKey(Janri, on_delete=models.CASCADE, verbose_name="Жанр")
    artisti = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Артист")
    impresario = models.ForeignKey(Impresario, on_delete=models.CASCADE, verbose_name="Импресарио")

    class Meta:
        verbose_name = "Договор с импресарио"
        verbose_name_plural = "Договоры с импресарио"
        db_table = "rabotasimpresario"

    def __str__(self):
        return f"{self.impresario} — {self.artisti} ({self.data})"


class UchastieArtistovVMeropriyatii(models.Model):
    """Участие артистов в мероприятии"""
    janri = models.ForeignKey(Janri, on_delete=models.CASCADE, verbose_name="Жанр")
    artisti = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Артист")
    meropriyatie = models.ForeignKey(Meropriyatie, on_delete=models.CASCADE, verbose_name="Мероприятие")

    class Meta:
        verbose_name = "Участие артиста"
        verbose_name_plural = "Участия артистов"
        db_table = "uchastie_artistov_v_meropriyatii"

    def __str__(self):
        return f"{self.artisti} на {self.meropriyatie}"


class Nagrajdeniya(models.Model):
    """Награждение (nagrajdeniya)"""
    data = models.DateField(verbose_name="Дата награждения")
    nagrada = models.ForeignKey(Nagrada, on_delete=models.CASCADE, verbose_name="Награда")
    uchastie = models.ForeignKey(
        UchastieArtistovVMeropriyatii, on_delete=models.CASCADE,
        verbose_name="Участие"
    )

    class Meta:
        verbose_name = "Награждение"
        verbose_name_plural = "Награждения"
        db_table = "nagrajdeniya"

    def __str__(self):
        return f"{self.nagrada} — {self.uchastie}"