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
from django.urls import path, include
from rest_framework import routers

from bet_details.viewsets import BetsDetailsByUserViewSet
from bets.viewsets import BetsViewSet
from seed.viewsets import SportsHunchViewSet, SeedStandingsViewSet
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
router.register(r"api/manager/seed", SportsHunchViewSet, basename="ManagerSeed")
router.register(
    r"api/manager/seed/standings", SeedStandingsViewSet, basename="ManagerStandingsSeed"
)
router.register(
    r"api/standings/current", CurrentStandingsViewSet, basename="CurrentViewSet"
)

urlpatterns = [
    path("", include(router.urls)),
]
