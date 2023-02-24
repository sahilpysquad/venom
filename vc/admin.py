from django.contrib import admin

from vc.models import VC, AmountPaidByUser, AmountReceivedByUser


@admin.register(AmountReceivedByUser)
class AmountReceivedByUserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(AmountPaidByUser)
class AmountPaidByUserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(VC)
class VCModelAdmin(admin.ModelAdmin):
    list_display = ('vc_id', 'emi_type', 'total_amount', 'is_active')
