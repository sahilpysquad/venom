from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from vc.forms import VCModelForm
from vc.models import VC


class VCListView(LoginRequiredMixin, ListView):
    model = VC
    template_name = 'vc/vc_list.html'
    context_object_name = 'organizer_vcs_objs'

    def get_queryset(self):
        return self.model.objects.filter(organizer=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VCListView, self).get_context_data(object_list=None, **kwargs)
        context['participant_vcs_objs'] = self.model.objects.filter(participant=self.request.user.id)
        return context


class VCCreateView(LoginRequiredMixin, CreateView):
    template_name = 'vc/vc_create.html'
    model = VC
    form_class = VCModelForm
    success_url = '/vc/all-vcs/'
