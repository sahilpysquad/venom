from django.urls import path

from vc.views import VCListView, VCCreateView, VCDetailView, VCUpdateView, VCDeleteView, VCLeaveView

urlpatterns = [
    # All VCs
    path('all-vcs/', VCListView.as_view(), name='all_vcs'),

    # CRUD VCs
    path('create/', VCCreateView.as_view(), name='vc_create'),
    path('detail/<str:vc_id>/', VCDetailView.as_view(), name='vc_detail'),
    path('update/<str:vc_id>/', VCUpdateView.as_view(), name='vc_update'),
    path('delete/<str:vc_id>/', VCDeleteView.as_view(), name='vc_delete'),

    # Leave VCs
    path('leave/<str:vc_id>/', VCLeaveView.as_view(), name='vc_leave'),
]
