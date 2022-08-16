from cronos.models.job import Job
from typing import List
from datetime import datetime


def list_jobs(
    job_id: int = None,
    name: str = None,
    cron_expression: str = None,
    service_id: str = None,
) -> List[Job]:
    query = Job.objects.filter(is_inactive=False)
    if job_id:
        query = query.filter(id=job_id)
    if name:
        query = query.filter(name=name)
    if cron_expression:
        query = query.filter(cron_expression=cron_expression)
    if service_id:
        query = query.filter(service_id=service_id)
    return list(query.all())


def create_job(
    name: str,
    cron_expression: str,
    service_id: str = None,
) -> Job:
    if service_id and not isinstance(service_id, str):
        raise ValueError("Service id must be a string")
    new_job = Job.objects.create(
        name=name,
        cron_expression=cron_expression,
        service_id=service_id,
    )
    return new_job


def update_job(
    job_id: int,
    name: str = None,
    cron_expression: str = None,
    service_id: str = None,
) -> Job:
    job = Job.objects.get(id=job_id)

    if name:
        job.name = name
    if cron_expression:
        job.cron_expression = cron_expression
    if service_id:
        if not isinstance(service_id, str):
            raise ValueError("Service id must be a string")
        job.service_id = service_id
    job.updated_time = datetime.now()
    job.save()
    return job


def remove_job(
    job_id: int,
):
    job = Job.objects.get(id=job_id)
    if not job.is_inactive:
        job.is_inactive = True
    else:
        raise Exception("This job has been already inactived")
    job.save()
