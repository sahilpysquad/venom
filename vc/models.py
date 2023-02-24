import datetime

from django.db import models

from account_user.models import User


class VC(models.Model):
    EMI_TYPE = (
        ('W', 'Week'),
        ('M', 'Month'),
        ('Y', 'Year')
    )

    name = models.CharField(verbose_name='Name', max_length=250, default='')
    vc_id = models.CharField(verbose_name='VC Id', max_length=20, editable=False, unique=True)
    organizer = models.ManyToManyField(verbose_name='Organizers', to=User, related_name='vc_organizer_users')
    participant = models.ManyToManyField(
        verbose_name='Participants', to=User, related_name='vc_participant_users', blank=True
    )
    emi_type = models.CharField(verbose_name='EMI Type', max_length=12, choices=EMI_TYPE, default='M')
    total_amount = models.PositiveBigIntegerField(verbose_name='Total Amount')
    is_active = models.BooleanField(verbose_name='Active', default=True)
    created_at = models.DateTimeField(verbose_name='Created On', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated On', auto_now=True)

    class Meta:
        verbose_name = 'VC'
        verbose_name_plural = 'VCs'

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return f'<VC: {self.vc_id}>'

    def save(self, *args, **kwargs):
        self.vc_id = datetime.datetime.now().strftime('V%Y%m%d%H%M%SC')
        return super(VC, self).save(*args, **kwargs)

    @property
    def emi_amount(self):
        return self.total_amount / self.participant.count()


class AmountPaidByUser(models.Model):
    vc = models.ForeignKey(verbose_name='VC', to=VC, on_delete=models.DO_NOTHING, related_name='vc_amount_payers')
    paid_by = models.ForeignKey(verbose_name='Paid By', to=User, on_delete=models.DO_NOTHING, related_name='pay_users')
    amount = models.PositiveIntegerField(verbose_name='Amount Paid')
    paid_on = models.DateTimeField(verbose_name='Paid On', auto_now_add=True)

    class Meta:
        verbose_name = 'Amount Paid By User'
        verbose_name_plural = 'Amount Paid By Users'

    def __str__(self):
        return self.id


class AmountReceivedByUser(models.Model):
    vc = models.ForeignKey(verbose_name='VC', to=VC, on_delete=models.DO_NOTHING, related_name='vc_amount_receivers')
    received_by = models.ForeignKey(
        verbose_name='Received By', to=User, on_delete=models.DO_NOTHING, related_name='receive_users'
    )
    amount = models.PositiveIntegerField(verbose_name='Amount Received')
    received_on = models.DateTimeField(verbose_name='Received On', auto_now_add=True)

    class Meta:
        verbose_name = 'Amount Received By User'
        verbose_name_plural = 'Amount Received By Users'

    def __str__(self):
        return self.id
