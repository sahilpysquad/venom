from django.urls import path

from vc.views import VCListView, VCCreateView, VCDetailView, VCUpdateView

urlpatterns = [
    path('all-vcs/', VCListView.as_view(), name='all_vcs'),
    path('create/', VCCreateView.as_view(), name='vc_create'),
    path('detail/<str:vc_id>/', VCDetailView.as_view(), name='vc_detail'),
    path('update/<str:vc_id>/', VCUpdateView.as_view(), name='vc_update'),
]
