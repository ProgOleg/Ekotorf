from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from app.models import *
from django import forms
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

admin.site.register(FirstWindow)
admin.site.register(Feedback)
admin.site.register(Faq)
admin.site.register(PrivacyPolicy)
admin.site.register(ForFeedback)
admin.site.register(ForApplications)
admin.site.register(ForMailing)
admin.site.register(TelephoneNumberS)
admin.site.register(Whatsapp)
admin.site.register(Telegram)
admin.site.register(Viber)
admin.site.register(ForCallback)
admin.site.register(Person)
admin.site.register(WorkingTime)
admin.site.register(Geomarker)
admin.site.register(MainOffice)
admin.site.register(Benefits1)
admin.site.register(Benefits2)
admin.site.register(Benefits3)
admin.site.register(Benefits4)
admin.site.register(Benefits5)
admin.site.register(Benefits6)
admin.site.register(Benefits7)
admin.site.register(Benefits8)
admin.site.register(StyleMainPage)


admin.site.site_title = "Админапанель 'ЭкоТорф'"
admin.site.site_header = "Админапанель 'ЭкоТорф'"


class ProductGalleryVideooAdmin(admin.ModelAdmin):
    models = ProductGalleryVideo

    readonly_fields = ["preview"]
    list_display = ('name', 'preview')
    exclude = ('preview_link',)

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.get_img_src}" height="100">')

    def name(self, obj):
        return f'{obj.__str__()}'

    # !
    def link_(self, obj):
        return f'<a href="{obj.link}">{obj.link[:15]}</a>'


class ProductGalleryPhotoAdmin(admin.ModelAdmin):
    models = ProductGalleryPhoto

    readonly_fields = ["preview"]
    list_display = ('name', 'preview')

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="100">')

    def name(self, obj):
        return f'{obj.__str__()}'


class ProductGalleryPhotoInline(admin.StackedInline):
    model = ProductGalleryPhoto
    extra = 0
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="350">')


class ProductGalleryVideoAInline(admin.StackedInline):
    model = ProductGalleryVideo
    extra = 0
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.get_img_src}" height="350">')


class ProductAdmin(admin.ModelAdmin):

    inlines = [ProductGalleryPhotoInline, ProductGalleryVideoAInline]

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.picture_main.url}" height="350">')


class ProductInline(admin.StackedInline):
    model = Product
    extra = 0
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.get_img_src}" height="350">')


class PersonInline(admin.StackedInline):
    model = Person
    extra = 0
    #readonly_fields = ["tell", "mail", "mailing_status"]
    readonly_fields = ["person_tell", ]

    def person_tell(self, obj):
        return f'{obj.tell}' if obj.tell else '-'


class ApplicationsInline(admin.StackedInline):
    model = Applications
    extra = 0
    readonly_fields = ["person_tell",]

    def person_tell(self, obj):
        return f'{obj.tell}' if obj.tell else '-'


class ApplicationsAdmin(admin.ModelAdmin):

    list_display = (
        "id", "admin_product_title", "persons", "persons_tell", "quantity", "status",  "date_cr", "date_ready",
        "note", "geography",
    )

    list_display_links = ('admin_product_title', 'persons')
    list_editable = ("quantity", "status", "note", "geography")

    # readonly_fields = ["person",]

    def admin_product_title(self, obj):
        return f'{obj.product.title}'
    admin_product_title.short_description = 'Товар'
    admin_product_title.admin_order_field = 'product__title'

    def persons(self, obj):
        if obj.person:
            return format_html(
                f'<a href="/admin/app/person/{obj.person.pk}/change">{obj.person.name}</a>'
            )
    persons.short_description = "Клиент"
    persons.admin_order_field = 'person__name'
    persons.allow_tags = True

    def persons_tell(self, obj):
        if obj.person:
            return format_html(
                f'<a href="tel:{obj.person.tell}">{obj.person.tell}</a>'
            )
    persons_tell.short_description = "Телефон"
    persons_tell.admin_order_field = 'person__tell'
    persons_tell.allow_tags = True

    def date_cr(self, obj):
        return obj.date_created
    date_cr.short_description = "Дата создания"
    date_cr.admin_order_field = 'date_created'

    def count_prod(self, obj):
        return obj.quantity
    count_prod.short_description = "Количество"

    def get_row_css(self, obj, index):
        if obj.status == 'new':
            return 'row-new'
        elif obj.status == 'processing':
            return 'row-processing'
        elif obj.status == 'success':
            return 'row-success'
        elif obj.status == 'refusing':
            return 'row-refusing'
        else:
            return 'row-non'


class ApplicationsTabular(admin.TabularInline):
    model = Applications
    raw_id_fields = ("id",)


# class CallbackAdminForm(forms.ModelForm):
#     class Meta:
#         model = Callback


class CallbackAdmin(admin.ModelAdmin):
    fields = ("person", "status")
    # inlines = ("PersonTabular",)
    list_display = ("id", "persons", "persons_tell", "status", "application_", "date_created",
                    )
    list_editable = ("status",)
    list_display_links = ("id",)

    def get_row_css(self, obj, index):
        if obj.status == 'new':
            return 'row-new'
        elif obj.status == 'processing':
            return 'row-processing'
        elif obj.status == 'success':
            return 'row-success'
        elif obj.status == 'refusing':
            return 'row-refusing'
        else:
            return 'row-non'

    def persons_tell(self, obj):
        if obj.person:
            return format_html(
                f'<a href="tel:{obj.person.tell}">{obj.person.tell}</a>'
            )

    persons_tell.short_description = "Телефон"
    persons_tell.admin_order_field = 'person__tell'
    persons_tell.allow_tags = True

    def persons(self, obj):
        if obj.person:
            return format_html(
                f'<a href="/admin/app/person/{obj.person.pk}/change">{obj.person.name}</a>'
            )

    persons.short_description = "Клиент"
    persons.admin_order_field = 'person__name'
    persons.allow_tags = True

    def application_(self, obj):
        if obj.application:
            return format_html(
                f'<a href="/admin/app/applications/{obj.application.pk}/change">{obj.application.__str__()}</a>'
            )
    application_.short_description = "Заявка"
    application_.admin_order_field = 'applications__date_created'
    application_.allow_tags = True





admin.site.register(Callback, CallbackAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGalleryPhoto, ProductGalleryPhotoAdmin)
admin.site.register(ProductGalleryVideo, ProductGalleryVideooAdmin)
admin.site.register(Applications, ApplicationsAdmin)












