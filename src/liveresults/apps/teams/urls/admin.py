from django.urls import path

from liveresults.apps.teams.views.admin import (TeamAdminCreateView, TeamAdminRetrieveView,
                                                HonorAdminCreateView, HonorAdminRetrieveUpdateDeleteView)

urlpatterns = [
    path('create/', TeamAdminCreateView.as_view(), name='create-team'),
    path('<str:name>/', TeamAdminRetrieveView.as_view(), name='detail-team'),
    path('honor/create/', HonorAdminCreateView.as_view(), name='create-honor'),
    path('honor/<int:pk>/', HonorAdminRetrieveUpdateDeleteView.as_view(), name='detail-honor'),
]