import django.db.models
import django.conf


class Structure(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
        unique=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "состав"
        verbose_name_plural = "составы"

    def __str__(self):
        return self.name[:15]


class Tip(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
        unique=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "тип соревнования"
        verbose_name_plural = "типы соревнований"

    def __str__(self):
        return self.name[:15]


class Group(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
        unique=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "наименование спортивного мероприятия"
        verbose_name_plural = "наименования спортивного мероприятия"

    def __str__(self):
        return self.name[:15]


class Meropriation(django.db.models.Model):
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        max_length=200,
        null=True,
    )
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=True,
        unique=False,
    )
    text = django.db.models.TextField(
        null=True,
        verbose_name="текст",
    )
    count = django.db.models.PositiveIntegerField(
        null=True,
        verbose_name="количество участников",
    )
    place = django.db.models.TextField(
        null=True,
        verbose_name="место проведения",
    )
    structure = django.db.models.ForeignKey(
        Structure,
        verbose_name="категория",
        null=True,
        on_delete=django.db.models.CASCADE,
        related_name="catalog_items",
    )
    tip = django.db.models.ForeignKey(
        Tip,
        verbose_name="категория",
        null=True,
        on_delete=django.db.models.CASCADE,
        related_name="catalog_items",
    )
    group = django.db.models.ForeignKey(
        Group,
        verbose_name="категория",
        null=True,
        on_delete=django.db.models.CASCADE,
        related_name="catalog_items",
    )
    date_start = django.db.models.DateField(
        verbose_name="дата начала",
        null=True,
    )
    date_end = django.db.models.DateField(
        verbose_name="дата конца",
        null=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "мероприятие"
        verbose_name_plural = "мероприятия"

    def __str__(self):
        return self.name

class Discipline(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
        unique=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "дисциплина"
        verbose_name_plural = "дисциплины"

    def __str__(self):
        return self.name[:15]

class CustomRequest(django.db.models.Model):
    user = django.db.models.ForeignKey(
        django.conf.settings.AUTH_USER_MODEL,
        verbose_name="пользователь",
        on_delete=django.db.models.SET_NULL,
        null=True,
    )
    disciplines = django.db.models.ManyToManyField(
        Discipline,
        verbose_name="дисциплины",
    )
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
        unique=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "дисциплина"
        verbose_name_plural = "дисциплины"

    def __str__(self):
        return self.name[:15]
