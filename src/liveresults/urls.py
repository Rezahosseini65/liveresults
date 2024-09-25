from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


front_urlpatterns = [
    path('api/front/league/', include(('liveresults.apps.leagues.urls.front', 'liveresults.apps.leagues'),
                                      namespace='front-league')),
    path('api/front/team/', include(('liveresults.apps.teams.urls.front', 'liveresults.apps.teams'),
                                    namespace='front-team')),
]

admin_urlpatterns = [
    path('api/admin/league/', include(('liveresults.apps.leagues.urls.admin', 'liveresults.apps.leagues'),
                                      namespace='admin-league')),
    path('api/admin/team/', include(('liveresults.apps.teams.urls.admin', 'liveresults.apps.teams'),
                                    namespace='admin-team')),
]

doc_urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include("debug_toolbar.urls")),
]+doc_urlpatterns+front_urlpatterns+admin_urlpatterns
