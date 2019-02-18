from __future__ import absolute_import, unicode_literals
from django.shortcuts import get_object_or_404
from celery import shared_task
from .models import Test


@shared_task
def add(x, y):
    return x + y


@shared_task
def delete_test(id):
    get_object_or_404(Test, id=id).delete()
    return 'delete is done!'

# add.apply_async((2, 2), countdown=10)