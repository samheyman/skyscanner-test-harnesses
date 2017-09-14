from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm
from skyscanner.skyscanner import Flights, FlightsCache
apikey = 'fetch from environment'
flights_cache_service = FlightsCache(apikey)
flights_service = Flights(apikey)
import json 
from pprint import pprint

def index(request):
	# country = flights_cache_service.get_cheapest_quotes(
	# 		    market='UK',
	# 		    currency='GBP',
	# 		    locale='en-GB',
	# 		    originplace= 'UK',
	# 		    destinationplace= 'AE-sky',
	# 		    outbounddate='anytime',
	# 		    inbounddate='anytime').parsed
	if 'origin_field' in request.GET:
		market='UK'
		currency='GBP'
		locale='en-GB'
		
		# create a form instance and populate it with data from the request:
		form = SearchForm(request.GET)
		# check whether it's valid:
		if form.is_valid():
			origin = form.cleaned_data['origin_field']
			destination = form.cleaned_data['destination_field']
			outbounddate=form.cleaned_data['from_date_field']
			inbounddate=form.cleaned_data['to_date_field']
			api_service=form.cleaned_data['service_field']
			# Make query to the live prices API
			#flights = flights

			if api_service=='browsequotes':
			# Make query to Flights Browse Cache API
				response = flights_cache_service.get_cheapest_quotes(
				    market=market,
				    currency=currency,
				    locale=locale,
				    originplace= origin,
				    destinationplace= destination,
				    outbounddate=outbounddate,
				    inbounddate=inbounddate).parsed
				quotes = response['Quotes']
				print("Date format: " + str(type(response['Quotes'][0]['OutboundLeg']['DepartureDate'])))
				routes = []
				dates = []
				outboundDates = []
				inboundDates = []

			elif api_service=='browseroutes':
				response = flights_cache_service.get_cheapest_price_by_route(
				    market=market,
				    currency=currency,
				    locale=locale,
				    originplace= origin,
				    destinationplace= destination,
				    outbounddate=outbounddate,
				    inbounddate=inbounddate).parsed
				quotes = response['Quotes']
				routes = response['Routes']
				dates = []
				outboundDates = []
				inboundDates = []

			elif api_service=='browsedates':
				response = flights_cache_service.get_cheapest_price_by_date(
				    market=market,
				    currency=currency,
				    locale=locale,
				    originplace= origin,
				    destinationplace= destination,
				    outbounddate=outbounddate,
				    inbounddate=inbounddate).parsed
				quotes = response['Quotes']
				dates = response['Dates']
				outboundDates = sorted(dates["OutboundDates"], key=lambda x:x['PartialDate'])
				inboundDates = sorted(dates["InboundDates"], key=lambda x:x['PartialDate'])
				routes = []

			elif api_service=='browsegrid':
				response = flights_cache_service.get_grid_prices_by_date(
				    market=market,
				    currency=currency,
				    locale=locale,
				    originplace= origin,
				    destinationplace= destination,
				    outbounddate=outbounddate,
				    inbounddate=inbounddate).parsed
				dates = response['Dates']
				routes = []
				quotes = []

			
			context = {
				"api_service": api_service,
				"form": form,
				"from": origin,
				"to": destination,
				"quotes": sorted(quotes, key=lambda x:x['MinPrice']),
				"routes": routes,
				"outboundDates": outboundDates,
				"inboundDates": inboundDates,
				"response": response,
				"repro_url": "http://partners.api.skyscanner.net/apiservices/" 
					+ api_service + "/v1.0/" + market + "/" + currency + "/" + locale 
					+ "/" + origin + "/" + destination + "/" + outbounddate + "/" 
					+ inbounddate + "?apikey=" + apikey
			}

		else:
			context = {
				"form": form,
				"from": "",
				"to": "",
				"flights": "no flights",
			}
		return render(request, 'flights/results.html', context)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = SearchForm()
		context = {
		"form": form,
		"flights": "please search",
		#"country": country
		}

	return render(request, 'flights/index.html', context)


def search_results(request):
	return render(request, 'flights/results.html', {})

def live_prices(request):
	with open('/Users/samheyman/Sites/b2b_api/flights_finder/static/flights.json','r') as flights_file:    
    		flights = json.load(flights_file)
	
	#flights = pprint(flights_data)
	return render(request, 'flights/live_prices.html', {"flights":flights})

def travel_insights(request):
	
	#flights = pprint(flights_data)
	return render(request, 'flights/travel_insights.html', {})
