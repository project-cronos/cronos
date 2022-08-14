from django.db import models


# This model stores the basic information of jobs
class Job(models.Model):
    id = models.BigAutoField(primary_key=True)  # the id of the job
    name = models.CharField(max_length=64, unique=True)  # the name of the job
    cron_expression = models.CharField(max_length=32)  # the cron expression of the job
    is_inactive = models.BooleanField(
        default=False
    )  # the sign shows whether the job is inactive
    # job_group_id = models.BigIntegerField(null=True)
    service_id = models.CharField(
        max_length=64, null=True
    )  # the identifier of the service that should run the job
    created_time = models.DateTimeField(
        auto_now_add=True
    )  # the time of the job was created
    updated_time = models.DateTimeField(
        auto_now=True
    )  # the latest time of the job was updated
