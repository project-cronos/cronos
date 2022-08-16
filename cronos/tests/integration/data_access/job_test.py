from django.test import TestCase
from cronos.data_access.job import create_job
from cronos.data_access.job import list_jobs
from django.db.utils import IntegrityError


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
        # TODO (Remove this after done)
        # raise an error using the with clause  (context manager)
        # to test if the service id is passed in as an integer,
        # an error should be thrown
        pass


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
        pass

    def test_list_job_by_service_id(self):
        pass


class JobUpdateFunctionTestCase(TestCase):
    # TODO
    pass
