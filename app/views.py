from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, FileResponse
from django.template import loader, Context
from .models import *
from .forms import *
from app.forms import *
from app.utils import *
from django.conf import settings
from django.db.models import Prefetch, F



class IndexPage(View):

    def get(self, request):
        product_data = []
        obj = Product.objects.filter(is_active=True).values('pk', 'title', 'specification', 'calorific_value',
                                                            'ash_content', 'strength', 'packing', 'type_packing',
                                                            'price',
                                                            'picture_main')
        for el in obj:
            photos = ProductGalleryPhoto.objects.filter(product_id=el['pk']).values('image')
            videos = ProductGalleryVideo.objects.filter(product_id=el['pk']).values('link', 'preview_link')
            product_data.append({**el, 'photos': photos, 'videos': list(videos)})

        context = {
            'tels': TelephoneNumberS.objects.filter(is_active=True).values('tell'),
            'first_window': FirstWindow.objects.filter(is_active=True).values('title', 'sub_title', 'picture'),
            'feedback': Feedback.objects.filter(is_active=True),
            'faq': Faq.objects.filter(is_active=True),
            'privacy_policy': PrivacyPolicy.objects.filter(is_active=True).values('entry'),
            'second_window': SecondWindow.objects.filter(is_active=True).values('title', 'sub_title', 'picture'),
            'product': product_data,
            'working_time': WorkingTime.objects.filter(is_active=True).values('working_time'),
            'geomarker': Geomarker.objects.filter(is_active=True).values('latitude', 'longitude'),
            'telegram': Telegram.objects.filter(is_active=True).values('link'),
            'whatsapp': Whatsapp.objects.filter(is_active=True).values('link'),
            'viber': Viber.objects.filter(is_active=True).values('link')
        }
        return render(request, 'app/index.html', context)


def application_view(request):
    if request.method == 'POST':
        applicataion_form = ApplicationsForm(request.POST)
        person_form = PersonForm(request.POST)
        if applicataion_form.is_valid() and person_form.is_valid():
            person_obj = person_form.save()
            obj = Applications.objects.create(person_id=person_obj.id,
                                              product_id=applicataion_form.cleaned_data['product_pk'],
                                              quantity=applicataion_form.cleaned_data['count_product'])
            context = Applications.objects.filter(pk=obj.id).values(
                'pk', 'person__name', 'person__tell', 'product__title', 'date_created',
                'person__mailing_status', 'person__mail', 'quantity', 'person_id')
            context = context[0]
            context_for_application = context.copy()
            data = {'pk': context_for_application['pk'], 'tell': context_for_application['person__tell'],
                    }
            context_for_application.update({'name': context_for_application.pop('person__name')})
            context_for_application.update({'tell': context_for_application.pop('person__tell')})
            context_for_application.update({'product_title': context_for_application.pop('product__title')})
            context_for_application.update({'mail': context_for_application.pop('person__mail')})
            send = SendEmailMessage(context_for_application, 'Application', data)
            send.send_message()
            if context['person__mail']:
                data = {'pk': context['person_id'], 'mail': context['person__mail']}
                context_for_mailing = {}
                context_for_mailing.update({'mail': context['person__mail']})
                context_for_mailing.update({'pk': context['person_id']})
                send = SendEmailMessage(context, 'Mailing', data)
                send.send_message()
            return HttpResponse(status=200)
        return JsonResponse(
            applicataion_form.errors or person_form.errors, status=400, safe=False)
    return HttpResponse(status=404)


def feedback_view(request):
    if request.method == 'POST':
        foo = FeedbackForm(request.POST, request.FILES)
        if foo.is_valid():
            foo = foo.save()
            obj = Feedback.objects.filter(pk=foo.id).values('pk', 'name', 'entry', 'rating', 'date_created')
            data = {'pk': obj[0]['pk']}
            send = SendEmailMessage(obj[0], 'Feedback', data)
            result = send.send_message()
            return HttpResponse(status=200)
        return JsonResponse(foo.errors, status=400, safe=False)
    return HttpResponse(status=404)


def callback_view(request):
    if request.method == 'POST':
        foo = PersonForm(request.POST)
        if foo.is_valid():
            obj = foo.save()
            obj = Person.objects.filter(pk=obj.id).values('pk', 'name', 'tell', 'date_created')
            data = {'name': obj[0]['name'], 'tell': obj[0]['tell']}
            var = SendEmailMessage(obj[0], 'Callback', data)
            result = var.send_message()
            return HttpResponse(status=200)
        return JsonResponse(foo.errors, status=400, safe=False)
    return HttpResponse(status=404)


def mailing_view(request):
    if request.method == 'POST':
        data = request.POST
        foo = PersonForm(data)
        if foo.is_valid():
            bar = foo.save()
            obj = Person.objects.filter(pk=bar.id).values('pk', 'mail')
            data = {'pk': obj[0]['pk'], 'mail': obj[0]['mail']}
            var = SendEmailMessage(obj[0], 'Mailing', data)
            result = var.send_message()
            return HttpResponse(status=200)
        return JsonResponse(foo.errors, status=400, safe=False)
    return HttpResponse(status=404)





















