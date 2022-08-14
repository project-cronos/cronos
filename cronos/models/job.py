from django.db import models


# This model stores the basic information of jobs
class Job(models.Model):
    """
    The class represents a specific cron job.
    id: int, the id of the job
    name: str, the name of the job
    cron_expression: str, the cron expression of the job
    is_inactive: bool, the sign shows whether the job is inactive
    service_id: str, the identifier of the service that should run the job
    created_time: datetime, the time of the job was created
    updated_time: datetime, the latest time of the job was updated
    """

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    cron_expression = models.CharField(max_length=32)
    is_inactive = models.BooleanField(default=False)
    # job_group_id = models.BigIntegerField(null=True)
    service_id = models.CharField(max_length=64, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
