import uuid

from django.db import models
from django.urls import reverse
from timezone_field import TimeZoneField

# Create your models here.


class TimeStampedModel(models.Model):
    # Abstract base class model that provides self-updating created and modified fields
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Party(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    short_name = models.CharField(max_length=8, unique=True)


class PartyRelation(TimeStampedModel):

    PARENT = "PARENT"
    SIBLING = "SIBLING"
    PARTNER = "PARTNER"

    RELATION_CHOICES = ((PARENT, "PARENT"), (SIBLING, "SIBLING"), (PARTNER, "PARTNER"))

    party_from = models.ForeignKey(
        to=Party, on_delete=models.CASCADE, related_name="parties_from"
    )
    party_to = models.ForeignKey(
        to=Party, on_delete=models.CASCADE, related_name="parties_to"
    )
    relationship_type = models.CharField(
        choices=RELATION_CHOICES, max_length=100, default=PARENT
    )


class Organization(Party):
    name = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=50)
    vat_id = models.CharField(max_length=50)


class Person(Party):
    full_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("addressbook:person-detail", kwargs={"pk": self.pk})


class Address(TimeStampedModel):
    MAIN = "MAIN"
    INVOICE = "INVOICE"
    DELIVERY = "DELIVERY"

    ADDRESS_TYPE_CHOICES = (
        (MAIN, "MAIN"),
        (INVOICE, "INVOICE"),
        (DELIVERY, "DELIVERY"),
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    party = models.ForeignKey(
        to=Party, null=False, blank=False, on_delete=models.CASCADE
    )
    line_one = models.CharField(max_length=100, null=True, blank=True)
    line_two = models.CharField(max_length=100, null=True, blank=True)
    line_three = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    post_office_box = models.CharField(max_length=50, null=True, blank=True)
    country_code = models.CharField(max_length=2)
    address_type = models.CharField(
        max_length=20, choices=ADDRESS_TYPE_CHOICES, default=MAIN
    )
    timezone = TimeZoneField(null=True, blank=True)
