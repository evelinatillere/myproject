from django import forms
import re


class EmailForm(forms.Form):
    email = forms.EmailField(label="Jūsu epasts", max_length=100)
    text = forms.CharField(label="Jūsu ziņa", widget=forms.Textarea)

    def _init_(self, *args, **kwargs):
       super()._init_(*args, **kwargs)
       for field in self.fields:
            new_data = {
                # "placeholder": str(field), 
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(new_data)
            # self.fields['location'].widget.attrs.update({'class': 'form-control'})
            self.fields['text'].widget.attrs.update({'placeholder': 'Ieraksti man ziņu!'})

    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        text = cleaned_data.get('text')
        if not email:
            self.add_error('email',_('nevar būt tukšs'))
        if not text:
            self.add_error('text',_('nevar būt tukšs'))
        elif not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            self.add_error('email','ievadiet derīgu epasta adresi')
        return cleaned_data