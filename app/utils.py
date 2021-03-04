from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
from app.models import ForApplications, ForFeedback, ForCallback, ForMailing
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def pdb_stoper(function, request, *args, **kwargs):

    try:
        function(request, *args, *kwargs)
    except BaseException:
        import pdb
        pdb.set_trace()
    finally:
        #exit()
        return function(*args, *kwargs)


class SendEmailMessage:
    mail_from_send = settings.EMAIL_HOST_USER
    template = 'app/mail_template.html'
    header_collections = {
        'Application': {
            'header': lambda pk, tell: f'Новая заявка, id- {pk}, телефон: {tell}',
            'header_template': 'Новая заявка'},
        'Feedback': {'header': lambda pk: f'Новый отзыв, id- {pk}',
                     'header_template': 'Новый отзыв'},
        'Callback': {'header': lambda tell, name: f'Обратный звонок, телефон: {tell}, имя: {name}',
                     'header_template': 'Обратный звонок'},
        'Mailing': {'header': lambda pk, mail: f'Разрешение на рассылку, id- {pk}, email - {mail}',
                    'header_template': 'Заявка на рассылку'}
    }
    models_collections = {
        'Application': ForApplications,
        'Feedback': ForFeedback,
        'Callback': ForCallback,
        'Mailing': ForMailing
    }

    def __init__(self, context, class_name, data=None):
        self.mail_to_send = self.__models_constructor(class_name)
        self.context = context
        self.header = self.__header_constructor(class_name, data)
        self.context.update({'header_template': self.header_collections[class_name]['header_template']})

    def __header_constructor(self, class_name, data=None):
        try:
            if data:
                return self.header_collections[class_name]['header'](**data)
            return self.header_collections[class_name]['header_template']
        except KeyError:
            raise ValueError()

    def __models_constructor(self, class_name):
        try:
            obj = self.models_collections[class_name].objects.filter(is_active=True).values('address')
            return obj[0].get('address')
        except KeyError:
            raise ValueError()

    def send_message(self):
        html_content = render_to_string(self.template, self.context)
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(self.header, text_content, self.mail_from_send, [self.mail_to_send])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
