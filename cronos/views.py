# from django.shortcuts import render
from cronos.logic.job import list_jobs as logic_list_jobs
from django.http import JsonResponse
from rest_framework import viewsets
from cronos.serializers import JobSerializer


# # Understand why we need the serializer
# @api_view(http_method_names=['GET'])
# def list_jobs(request: Request) -> Response:
#     jobs = logic_list_jobs()
#     return JsonResponse({
#         "jobs": json.dumps([
#             job for job in jobs
#         ])
#     }, status=200, content_type='application/json')


class JobViewSet(viewsets.ViewSet):
    def list(self, request):
        jobs = JobSerializer(data=logic_list_jobs(), many=True)
        jobs.is_valid()
        return JsonResponse(
            {
                "jobs": jobs.data,
            },
            status=200,
            safe=False,
        )
