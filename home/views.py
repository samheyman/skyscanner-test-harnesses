from django.views.generic import TemplateView
from home.forms import LocationSearchForm
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def index(self, request):
        return render(request, self.template_name, {})

#
# def getGeoCordinates(location):
#     # initiating map in Madrid
#
#     url = 'https://maps.googleapis.com/maps/api/geocode/json'
#     params = {
#         'sensor':'true',
#         'apikey':'AIzaSyCNmfg_E1JASzqwIMheoUBjd4weWbKcWmg',
#         'address': location
#     }
#     query = url+"?sensor="+params['sensor']+"&address="+params['address']+"&key="+params['apikey']
#     print("Query: " + query)
#     try:
#         response = requests.get(query)
#         type = response.headers['content-type']
#         result = response.json()
#         print(result)
#         lat = result['results'][0]['geometry']['location']['lat']
#         print("Latitude: " + str(lat))
#         lng = result['results'][0]['geometry']['location']['lng']
#         print("Longitude: " + str(lng))
#     except:
#         lat,lng = (0,0)
#         result = "Error making the geolocation call: "
#         print(result)
#
#     return (lat,lng)
#
#
# def getAirports(lat,lng,limit):
#     api_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/airports?"
#     headers = {
#         'Authorization': 'Bearer ' + getOAuthToken()
#     }
#     values = {
#         "latitude": lat,
#         "longitude": lng,
#         "sort": "relevance",
#         "page[limit]": limit
#     }
#     api_endpoint = api_endpoint + urllib.parse.urlencode(values)
#     req = urllib.request.Request(api_endpoint, headers= headers)
#     print(req)
#     response = urllib.request.urlopen(req)
#     try:
#         json_data = json.load(response)
#     except:
#         json_data = None
#         return({'error': "Failed to parse the response."})
#
#     return json_data
#
# def getOAuthToken():
#     secrets = AccessCredentials.secrets
#     ACCESS_TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
#
#     authorization_response = (requests.post(
#         ACCESS_TOKEN_URL,
#         data=secrets
#     )).json()
#     return authorization_response['access_token']
