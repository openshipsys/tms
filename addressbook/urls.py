from django.urls import path

from addressbook import views as addressbook_views

app_name = "addressbook"
urlpatterns = [
    path(
        route="person/",
        view=addressbook_views.PersonFormCreateView.as_view(),
        name="person-create",
    ),
    path(
        route="person/<int:pk>/",
        view=addressbook_views.PersonFormUpdateView.as_view(),
        name="person-update",
    ),
    path(
        route="persons/<int:pk>/",
        view=addressbook_views.PersonFormDetailView.as_view(),
        name="person-detail",
    ),
    path(
        route="parties/",
        view=addressbook_views.PartyTemplateView.as_view(),
        name="party-navigation",
    ),
]
