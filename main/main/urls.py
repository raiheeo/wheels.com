from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Wheels",
        default_version='v1', ),
    public=True,
    permission_classes=[AllowAny],
)


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('car.urls')),
    path('accounts/', include('allauth.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
