from django.http import JsonResponse
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from rest_framework.views import APIView

handler400 = "rest_framework.exceptions.bad_request"
handler500 = "rest_framework.exceptions.server_error"


class HealthCheckView(APIView):
    permission_classes = []

    def get(self, request):
        return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health/", HealthCheckView.as_view()),
    path("comuni_italiani/", include("comuni_italiani.urls")),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("", RedirectView.as_view(url="/api/schema/swagger-ui/", permanent=False)),
]
