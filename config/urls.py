from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def healthcheck(request):
    return Response({"status": "ok"})


urlpatterns = [
    path("health/", healthcheck),
    path("comuni-italiani/", include("comuni_italiani.urls")),
]
