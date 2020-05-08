from django.db import models
from datetime import datetime
from employee.models import Employee

# Create your models here.
class Requisition(models.Model):

    class RequisitionStatus(models.IntegerChoices):
        # [not_published, pending, authorized, approved]
        NOT_PUBLISHED = 1
        PENDING = 2
        AUTHORIZED = 3
        APPROVED = 4
        PROCURED = 5
        DISPATCHED = 6
        DELIVERED = 7
        RECIEVED = 8

    originator = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='originator')
    authorizer = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='authorizer')
    approver = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='approver')
    item = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    unit = models.CharField(max_length=10)
    image_1 = models.ImageField(upload_to='requisition/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='requisition/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='requisition/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='requisition/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='requisition/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='requisition/%Y/%m/%d/', blank=True)
    status = models.IntegerField(choices=RequisitionStatus.choices)
    due_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.item


    