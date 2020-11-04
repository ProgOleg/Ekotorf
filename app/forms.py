from app.models import Person, Feedback, Product
from django import forms


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'tell', 'mail', 'mailing_status']

    def clean_mailing_status(self):
        if self.cleaned_data['mail']:
            self.cleaned_data['mailing_status'] = True
        self.cleaned_data['mailing_status'] = False
        return self.cleaned_data['mailing_status']


class ApplicationsForm(forms.Form):

    product_pk = forms.IntegerField()
    count_product = forms.CharField(max_length=50, required=False)

    def clean_product_pk(self):
        if self.cleaned_data['product_pk']:
            if not Product.objects.filter(pk=self.cleaned_data['product_pk']).exists():
                self.add_error(None, {'product_pk': 'Not valid Product reference'})
                return None
        return self.cleaned_data['product_pk']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'entry', 'rating', 'picture']
