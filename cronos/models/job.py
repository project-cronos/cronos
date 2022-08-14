from django.db import models


class Job(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    cron_expression = models.CharField(max_length=32)
    is_inactive = models.BooleanField(default=False)
    # job_group_id = models.BigIntegerField(null=True)
    service_id = models.CharField(max_length=64, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
