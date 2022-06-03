"""sports_hunch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions


from v1.urls import router as v1_urls
from bet_details.viewsets import BetsDetailsByUserViewSet
from bets.viewsets import BetsViewSet, CurrentRankingViewSet
from seed.viewsets import (
    SportsHunchViewSet,
    SeedStandingsViewSet,
    SeedBetRankingViewSet,
)
from standings.viewsets import CurrentStandingsViewSet

from teams.viewsets import TeamViewSet
from users.viewsets import ActiveUsersListViewSet

router = routers.DefaultRouter()
router.register(r"api/teams", TeamViewSet, basename="Team")
router.register(r"api/bets", BetsViewSet, basename="Bet")
router.register(r"api/users", ActiveUsersListViewSet, basename="User")
router.register(
    r"api/bets/details/user", BetsDetailsByUserViewSet, basename="BetDetails"
)
router.register(
    r"api/bets/details/user/ranking", CurrentRankingViewSet, basename="BetDetails"
)
router.register(r"api/manager/seed", SportsHunchViewSet, basename="ManagerSeed")
router.register(
    r"api/manager/seed/standings", SeedStandingsViewSet, basename="ManagerStandingsSeed"
)
router.register(
    r"api/standings/current", CurrentStandingsViewSet, basename="CurrentStandingViewSet"
)
router.register(
    r"api/ranking/current", CurrentRankingViewSet, basename="CurrentRankingViewSet"
)
router.register(
    r"api/manager/seed/championship/bets/ranking",
    SeedBetRankingViewSet,
    basename="CurrentViewSet",
)


schema_view = get_schema_view(
   openapi.Info(
      title="Sports Hunch API",
      default_version='v1',
      description="API for sports hunch clients",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="felipepqm@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("v1/", include((v1_urls.urls, 'sports_hunch_v1'), namespace='sport_hunch')),
]
