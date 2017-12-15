from django.conf.urls import url
from . import views


urlpatterns = [
    url('index', views.index, name='index'),
    url('live_prices', views.live_prices, name='live_prices'),
    url('travel_insights', views.travel_insights, name='travel_insights'),
    url('search_results', views.search_results, name='search_results')
]