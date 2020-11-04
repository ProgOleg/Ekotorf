from django.contrib import admin
from django.utils.safestring import mark_safe
from app.models import *
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

admin.site.register(FirstWindow)
admin.site.register(SecondWindow)
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

"""
class ProductGalleryVideoAdmin(admin.ModelAdmin):
    models = ProductGalleryVideo

    readonly_fields = ["preview_video_lin", "preview_img_lin"]
    list_display = ('name', 'preview_video_lin', 'preview_img_lin')

    def preview_video_lin(self, obj):
        return mark_safe(f'<img src="{obj.link.url}" height="100">')

    def preview_img_lin(self, obj):
        return mark_safe(f'<img src="{obj.preview_link.url}" height="100">')

    def name(self, obj):
        return f'{obj.__str__()}'
"""


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
        return f'{obj.tell}'


class ApplicationsInline(admin.StackedInline):
    model = Applications
    extra = 0
    readonly_fields = ["person_tell",]

    def person_tell(self, obj):
        return f'{obj.tell}'


class ApplicationsAdmin(admin.ModelAdmin):
    #inlines = [PersonInline]

    list_display = ("product", "person", "date_created")

    def person(self, obj):
        return f'{obj.__str__()}'

    def product(self, obj):
        return f'{obj.__str__()}'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGalleryPhoto, ProductGalleryPhotoAdmin)
admin.site.register(ProductGalleryVideo, ProductGalleryVideooAdmin)
admin.site.register(Applications, ApplicationsAdmin)












