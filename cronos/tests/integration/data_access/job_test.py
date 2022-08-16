from django.test import TestCase
from cronos.data_access.job import create_job
from cronos.data_access.job import list_jobs
from cronos.data_access.job import update_job
from django.db.utils import IntegrityError
from cronos.models.job import Job


DEFAULT_CRON_EXPRESSION = "* * * * *"


class JobCreateFunctionTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_job_successfully(self):
        job = create_job(
            name="test_job_name",
            cron_expression=DEFAULT_CRON_EXPRESSION,
        )
        self.assertIsNotNone(job.id)

    def test_create_job_with_same_name(self):
        create_job(
            name="test_job_name",
            cron_expression=DEFAULT_CRON_EXPRESSION,
        )

        with self.assertRaises(IntegrityError):
            create_job(
                name="test_job_name",
                cron_expression=DEFAULT_CRON_EXPRESSION,
            )

    def test_create_job_invalid_service_id_type_raises_error(self):
        with self.assertRaises(ValueError):
            create_job(
                name="test_job_name",
                cron_expression=DEFAULT_CRON_EXPRESSION,
                service_id=12345,
            )


class JobListFunctionTestCase(TestCase):
    def setUp(self) -> None:
        self.job1 = create_job(
            name="test_job_name_1",
            cron_expression=DEFAULT_CRON_EXPRESSION,
            service_id="test_service_id_a",
        )
        self.job2 = create_job(
            name="test_job_name_2",
            cron_expression=DEFAULT_CRON_EXPRESSION,
            service_id="test_service_id_b",
        )
        self.job3 = create_job(
            name="test_job_name_3",
            cron_expression=DEFAULT_CRON_EXPRESSION,
            service_id="test_service_id_a",
        )

    def test_list_job_by_id(self):
        jobs = list_jobs(job_id=self.job1.id)

        self.assertEquals(1, len(jobs))

        job = jobs[0]
        self.assertEquals(job.name, self.job1.name)
        self.assertEquals(job.cron_expression, self.job1.cron_expression)

    def test_list_job_by_name(self):
        jobs = list_jobs(name=self.job1.name)

        self.assertEquals(1, len(jobs))

        job = jobs[0]
        self.assertEquals(job.id, self.job1.id)

    def test_list_job_by_service_id(self):
        jobs = list_jobs(service_id=self.job1.service_id)

        self.assertEquals(2, len(jobs))

        job1, job3 = jobs
        self.assertEquals(job1.id, self.job1.id)
        self.assertEquals(job3.id, self.job3.id)


class JobUpdateFunctionTestCase(TestCase):
    def setUp(self) -> None:
        self.job1 = create_job(
            name="test_job_name_1",
            cron_expression=DEFAULT_CRON_EXPRESSION,
            service_id="test_service_id_a",
        )
        self.job2 = create_job(
            name="test_job_name_2",
            cron_expression=DEFAULT_CRON_EXPRESSION,
            service_id="test_service_id_b",
        )

    def test_update_job_successfully(self):
        job_id = self.job1.id
        job = update_job(
            job_id=job_id,
            name="new_job_name",
            cron_expression="* * * * ?",
            service_id="new_service_id",
        )

        self.job1 = list_jobs(self.job1.id)[0]

        self.assertEquals(job.name, self.job1.name)
        self.assertEquals(job.cron_expression, self.job1.cron_expression)
        self.assertEquals(job.service_id, self.job1.service_id)

    def test_update_job_id_not_exist(self):
        job_id = self.job1.id + 10086
        with self.assertRaises(Job.DoesNotExist):
            update_job(job_id=job_id)

    def test_update_job_to_existed_name(self):
        job_id = self.job1.id
        with self.assertRaises(IntegrityError):
            update_job(
                job_id=job_id,
                name="test_job_name_2",
            )

    def test_update_job_invalid_service_id(self):
        job_id = self.job1.id
        with self.assertRaises(ValueError):
            update_job(
                job_id=job_id,
                service_id=10086,
            )
