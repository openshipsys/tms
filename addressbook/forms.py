from django import forms

from addressbook.models import Address, Organization, Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add field requirements if required
        # self.fields['fieldname'].required = True


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
