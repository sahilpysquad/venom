from django.urls import path

from vc.views import VCListView, VCCreateView

urlpatterns = [
    path('all-vcs/', VCListView.as_view(), name='all_vcs'),
    path('create-vc/', VCCreateView.as_view(), name='create_vc')
]
