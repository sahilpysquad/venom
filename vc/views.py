from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from account_user.models import User
from vc.forms import VCModelForm
from vc.models import VC


class VCListView(LoginRequiredMixin, ListView):
    model = VC
    template_name = 'vc/vc_list.html'
    context_object_name = 'organizer_vcs_objs'

    def get_queryset(self):
        return self.model.objects.filter(organizer=self.request.user.id).exclude(status='TM')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VCListView, self).get_context_data(object_list=None, **kwargs)
        context['participant_vcs_objs'] = self.model.objects.filter(
            participant=self.request.user.id
        ).exclude(status='TM')
        context['created_vcs'] = self.model.objects.filter(created_by=self.request.user.id).exclude(status='TM')
        return context


class VCCreateView(LoginRequiredMixin, CreateView):
    template_name = 'vc/vc_create.html'
    model = VC
    form_class = VCModelForm
    success_url = '/vc/all-vcs/'
    user_queryset = User.objects.filter(is_active=True)

    def get_form(self, form_class=form_class):
        form = super(VCCreateView, self).get_form(form_class)
        form.fields['organizer'].queryset = self.user_queryset.exclude(id=self.request.user.id)
        form.fields['participant'].queryset = self.user_queryset
        return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(VCCreateView, self).form_valid(form)


class VCDetailView(LoginRequiredMixin, DetailView):
    template_name = 'vc/vc_detail.html'
    model = VC
    context_object_name = 'vc_obj'
    slug_url_kwarg = 'vc_id'
    slug_field = 'vc_id'


class VCUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'vc/vc_update.html'
    model = VC
    slug_url_kwarg = 'vc_id'
    slug_field = 'vc_id'
    fields = ('name', 'organizer', 'emi_type', 'emi_amount', 'participant', 'interest')
    success_url = '/vc/all-vcs/'
    user_queryset = User.objects.filter(is_active=True)

    def get_form(self, form_class=None):
        form = super(VCUpdateView, self).get_form(form_class)
        form.fields['organizer'].queryset = self.user_queryset.exclude(id=self.request.user.id)
        form.fields['participant'].queryset = self.user_queryset
        return form


class VCDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'vc/vc_delete_confirmation.html'
    model = VC
    slug_url_kwarg = 'vc_id'
    slug_field = 'vc_id'
    success_url = '/vc/all-vcs/'

    def form_valid(self, form):
        self.object.status = 'TM'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class LeaveVCView(LoginRequiredMixin, DeleteView):
    template_name = 'vc/vc_leave.html'
    model = VC
    slug_url_kwarg = 'vc_id'
    slug_field = 'vc_id'
    success_url = '/vc/all-vcs/'

    def form_valid(self, form):
        if 'participated_btn' in self.request.POST:
            self.object.participant.remove(self.request.user)
        else:
            self.object.organizer.remove(self.request.user)
        return HttpResponseRedirect(self.get_success_url())
