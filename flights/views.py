import os
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm
from skyscanner.skyscanner import Flights, FlightsCache
apikey = 'sh244837416937362282979494394467'
flights_cache_service = FlightsCache(apikey)
flights_service = Flights(apikey)
import json 
from pprint import pprint
#from django.contrib.staticfiles.templatetags.staticfiles import staticfiles
from django.contrib.staticfiles.storage import staticfiles_storage


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
	with open('/Users/sheyman/Documents/Code/API_test_harnesses/static/response.json','r') as flights_file:    
    		flights = json.load(flights_file)
	
	#flights = pprint(flights_data)
	return render(request, 'flights/live_prices.html', {"flights":flights})

def travel_insights(request):
	
	#flights = pprint(flights_data)
	return render(request, 'flights/travel_insights.html', {})


def destinations(request):
	origin = "New York"
	market = "UK"
	period = "2018-01"

	# Most searched data
	# ------------------
	searches_xs = ['x']
	searches = ['searches']
	with open('searches.json','r') as content:
		searches_values = json.load(content)
	for data_entry in searches_values["data"][0]["numberOfSearches"]["perDestination"].items(): 
		searches_xs.append(data_entry[0])
		searches.append(data_entry[1])

	most_searched_data = {
		"origin": origin,
		"period": period,
		"xs": json.dumps(searches_xs),
		"searches": json.dumps(searches)
	}

	# Most booked data
	# ----------------
	booking_xs = ['x']
	bookings = ['bookings']
	with open('bookings.json','r') as content:
		bookings_values = json.load(content)
	for data_entry in bookings_values["data"]: 
		booking_xs.append(data_entry["destination"])
		bookings.append(data_entry["analytics"]["travellers"]["score"])

	most_travelled_data = {
		"market" : market,
		"origin": origin,
		"xs": json.dumps(booking_xs),
		"bookings": json.dumps(bookings)
	}

	#Console.log(booking_xs)
	#Console.log(bookings)
	return render(request, 'flights/destinations.html', {"most_searched_data": most_searched_data, "most_travelled_data": most_travelled_data})







