from django.contrib import admin
from addressbook.models import Organization, Person, PartyRelation, Party, Address
# Register your models here.
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(PartyRelation)
admin.site.register(Party)
admin.site.register(Address)
