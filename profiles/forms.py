from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    This will generate the relevant field for the user to
    submit delivery details
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_mob_number': 'Mobile Number',
            'default_first_address_line': '1st Address Line',
            'default_second_address_line': '2nd Address Line',
            'default_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
        }

        self.fields['default_mob_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ''
            self.fields[field].label = False
