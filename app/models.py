from django.db import models
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class IsActiveOnlyOne:

    @staticmethod
    def save(self, *args, **kwargs):
        if self.is_active:
            objs = self.__class__.objects.filter(is_active=True)
            if objs.exists():
                objs.update(is_active=False)
        return super(self.__class__, self).save(*args, **kwargs)


class IsActiveField(models.Model):

    is_active = models.BooleanField("Активно на страницу", default=True)

    class Meta:
        abstract = True


class Benefits(IsActiveField):

    title = models.CharField("Заголовок", max_length=50, blank=True)
    entry = models.TextField("Запись", max_length=2000)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.title}, {self.entry}'


class SocialNetwork(IsActiveField):

    link = models.CharField("Ссылка", max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.link}, Cтатус - {self.is_active}'


class Email(IsActiveField):

    address = models.EmailField("Адрес почты")

    class Meta:
        abstract = True

    def __str__(self):
        return self.address


class Content(IsActiveField):

    title = models.CharField("Заголовок", max_length=50)
    sub_title = models.TextField("Описание", max_length=1000)
    picture = models.ImageField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.title}, {self.sub_title[:15]}...'


class TelephoneNumberS(IsActiveField):

    tell = models.CharField("Номер телефона", max_length=20)

    class Meta:
        verbose_name_plural = "Номера телефонов"

    def __str__(self):
        return self.tell


class Viber(SocialNetwork):
    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Viber"


class Telegram(SocialNetwork):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Telegram"


class Whatsapp(SocialNetwork):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Whatsapp"


class ForMailing(Email):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Почта для отправки уведомлений о рассылке"


class ForApplications(Email):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Почта для отправки уведомлений о заказах"


class ForFeedback(Email):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Почта для отправки уведомлений о отзыве"


class ForCallback(Email):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Почта для отправки уведомлений о обратном звонке"


class Feedback(models.Model):

    RATING = [
        (0, '0'), (1, '1'), (2, '2'),
        (3, '3'), (4, '4'), (5, '5')
    ]

    name = models.CharField("Имя", max_length=30)
    entry = models.TextField("Запись")
    rating = models.IntegerField("Рейтинг", choices=RATING, default=5)
    picture = models.ImageField("Фото", upload_to='Feedback/', blank=True)
    is_active = models.BooleanField("Активно на страницу", default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f'{self.id}, {self.name}, {self.entry[:40]}...'


class Faq(IsActiveField):

    header = models.CharField("Заголовок", max_length=150)
    entry = models.TextField("Запись")

    class Meta:
        verbose_name_plural = "Часто задаваемые вопросы"

    def __str__(self):
        return f'{self.header}, {self.entry[:20]}...'


class PrivacyPolicy(IsActiveField):

    entry = models.TextField("Запись")

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Политика конфиденциальности"

    def __str__(self):
        return f'{self.entry[:30]}...'


class FirstWindow(Content):

    class Meta:
        verbose_name_plural = "Первый экран"


class SecondWindow(Content):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Второй экран"


class Product(IsActiveField):
    TYPE = [
        (1, 'Мешок'), (2, 'Термоупаковка'),
        (3, 'Биг Бег'), (4, 'Навал')
    ]

    title = models.CharField("Заголовок", max_length=200)
    specification = models.TextField("Описание", max_length=2000)
    # characteristic
    calorific_value = models.CharField("Теплотворная способность", max_length=50)
    ash_content = models.CharField("Зольность", max_length=50)
    strength = models.CharField("Механическая прочность", max_length=50)
    packing = models.CharField("Фасовка", max_length=50)
    type_packing = models.IntegerField("Тип фасовки", choices=TYPE, default=1)
    price = models.CharField("Цена за тонну", max_length=50)

    picture_main = models.ImageField("Освновное фото", upload_to='Product/', unique=True)

    class Meta:
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'{self.title}, {self.packing}'


class ProductGalleryPhoto(models.Model):

    image = models.ImageField("Картинка", upload_to='ProductImage/')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None,
                                null=True, related_name='photo')
    # verbose_name

    class Meta:
        verbose_name_plural = "Фото для товаров"

    def __str__(self):
        return f'id - {self.id}, {self.product.title}'


class ProductGalleryVideo(models.Model):

    link = models.CharField("Ссылка", max_length=5000)
    preview_link = models.CharField("Ссылка на привью", max_length=5000, blank=True, default=None, null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None,
                                null=True, related_name='video')

    @classmethod
    def extract_video_id(cls, link):
        query = urlparse(link)

        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in {'www.youtube.com', 'youtube.com'}:
            if query.path == '/watch':
                return parse_qs(query.query)['v'][0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
        # fail?
        return None

    def save(self, *args, **kwargs):
        if self.link:
            video_id = self.__class__.extract_video_id(self.link)

            self.preview_link = f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
        return super(self.__class__, self).save(*args, **kwargs)

    @property
    def get_img_src(self):
        return f'http://img.youtube.com/vi/{ProductGalleryVideo.extract_video_id(self.link)}/maxresdefault.jpg'

    class Meta:
        verbose_name_plural = "Ссылки на видео"

    def __str__(self):
        return f'id - {self.id}, {self.product.title}'


class Applications(models.Model):
    TYPE = [
        ('new', 'Новая'), ('processing', 'В обработке'),
        ('success', 'Успех'), ('refusing', 'Отказ')
    ]

    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey('Person', verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    quantity = models.CharField('Количество', max_length=500, null=True, blank=True, default='0')
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    status = models.CharField("Статус заявки", max_length=30, choices=TYPE, default='new')
    date_ready = models.DateTimeField("Дата готовности", default=None, null=True, blank=True)

    note = models.CharField(verbose_name="Заметка", null=True, default=None, max_length=5000)
    geography = models.CharField(verbose_name="География", null=True, default=None, max_length=1024)

    class Meta:
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        if self.status == 'success' or self.status == 'refusing':
            self.date_ready = datetime.now()
        return super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f'id-{self.id},товар: {self.product.__str__()}, {self.date_created.strftime("%d.%m.%y %H:%M")}'

    quantity.short_description = "Количество"


class Person(models.Model):

    name = models.CharField("Имя", max_length=100, blank=True)
    tell = models.CharField("Телефон", max_length=20, blank=True)
    mail = models.EmailField("Почта", max_length=200, blank=True, null=True)
    mailing_status = models.BooleanField("Согласен на рассылку", default=False)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Клиенты"
        verbose_name = "Клиент"

    def save(self, *args, **kwargs):
        if self.mail:
            self.mailing_status = True
        return super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f'id-{self.id}, {self.name}, {self.tell}, {self.mail}, Рассылка - {self.mailing_status}'


class Callback(models.Model):
    TYPE = [
        ('new', 'Новая'), ('processing', 'В обработке'),
        ('success', 'Успех'), ('refusing', 'Отказ')
    ]

    person = models.ForeignKey("Person", verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    status = models.CharField("Статус заявки", max_length=30, choices=TYPE, default='new')
    application = models.ForeignKey("Applications", verbose_name="Заказ", on_delete=models.SET_NULL,
                                    null=True, default=None, blank=True)
    date_created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Заявка на обратный звонок"
        verbose_name = "Заявки на обратный звонок"

    def __str__(self):
        return f'{self.person.name}, {self.person.tell}. Статус-{self.status}'


class WorkingTime(IsActiveField):

    working_time = models.CharField("Время работы", max_length=50)

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Время работы"

    def __str__(self):
        return f'{self.working_time}, Статус - {self.is_active}'


class Geomarker(IsActiveField):

    latitude = models.CharField("Широта", max_length=100)
    longitude = models.CharField("Долгота", max_length=100)

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Геометка офиса"

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'


class MainOffice(IsActiveField):

    address = models.CharField("Адрес", max_length=200)
    link = models.CharField("Ссылка", max_length=1000)

    class Meta:
        verbose_name_plural = "Главный офис"

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    def __str__(self):
        return f'{self.address}'


class StyleMainPage(IsActiveField):
    GREEN = 'green'
    ORANGE = 'orange'
    PINK = 'pink'
    TYPE = [(GREEN, 'Зеленый'), (PINK, 'Розовый'), (ORANGE, 'Оранжевый')]

    color = models.CharField("Цвет", max_length=20, choices=TYPE, default='')

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Стиль сайта"

    def __str__(self):
        return f'{self.color}'


class Benefits1(Benefits):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Приемущества - 1"


class Benefits2(Benefits):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Приемущества - 2"


class Benefits3(Benefits):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Приемущества - 3"


class Benefits4(Benefits):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Приемущества - 4"


class Benefits5(Benefits):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Приемущества - 5"


class Benefits6(Benefits):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Приемущества - 6"


class Benefits7(Benefits):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Приемущества - 7"


class Benefits8(Benefits):

    def save(self, *args, **kwargs):
        IsActiveOnlyOne.save(self, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Приемущества - 8"
