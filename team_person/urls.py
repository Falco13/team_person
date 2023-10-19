from django.urls import path
from rest_framework import routers
from team_person.views import TeamViewSet, PersonViewSet

router = routers.SimpleRouter()
router.register('teams', TeamViewSet)
router.register('persons', PersonViewSet)

urlpatterns = [
]

urlpatterns += router.urls
