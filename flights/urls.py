from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'index', views.index, name='index'),
    url(r'live_prices', views.live_prices, name='live_prices'),
    url(r'travel_insights', views.travel_insights, name='travel_insights'),
    url(r'search_results', views.search_results, name='search_results')
]