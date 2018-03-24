from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='flights'),
    url('live_prices', views.live_prices, name='live_prices'),
    url('travel_insights', views.travel_insights, name='travel_insights'),
    url('search_results', views.search_results, name='search_results'),
    url('destinations', views.destinations, name='destinations'),
    url('airports', views.airports, name='airports'),
    url('low_fare_search', views.sandbox_low_fare_search, name='low_fare_search'),
    url('points_of_interest', views.points_of_interest, name='points_of_interest')
]