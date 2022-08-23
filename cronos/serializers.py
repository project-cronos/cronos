from cronos.models.job import Job
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "name",
            "cron_expression",
            "service_id",
            "created_time",
            "updated_time",
        ]
