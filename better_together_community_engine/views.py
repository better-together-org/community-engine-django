# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Person,
	Group,
	Membership,
	Invitation,
	Role,
)


class PersonCreateView(CreateView):

    model = Person


class PersonDeleteView(DeleteView):

    model = Person


class PersonDetailView(DetailView):

    model = Person


class PersonUpdateView(UpdateView):

    model = Person


class PersonListView(ListView):

    model = Person


class GroupCreateView(CreateView):

    model = Group


class GroupDeleteView(DeleteView):

    model = Group


class GroupDetailView(DetailView):

    model = Group


class GroupUpdateView(UpdateView):

    model = Group


class GroupListView(ListView):

    model = Group


class MembershipCreateView(CreateView):

    model = Membership


class MembershipDeleteView(DeleteView):

    model = Membership


class MembershipDetailView(DetailView):

    model = Membership


class MembershipUpdateView(UpdateView):

    model = Membership


class MembershipListView(ListView):

    model = Membership


class InvitationCreateView(CreateView):

    model = Invitation


class InvitationDeleteView(DeleteView):

    model = Invitation


class InvitationDetailView(DetailView):

    model = Invitation


class InvitationUpdateView(UpdateView):

    model = Invitation


class InvitationListView(ListView):

    model = Invitation


class RoleCreateView(CreateView):

    model = Role


class RoleDeleteView(DeleteView):

    model = Role


class RoleDetailView(DetailView):

    model = Role


class RoleUpdateView(UpdateView):

    model = Role


class RoleListView(ListView):

    model = Role

