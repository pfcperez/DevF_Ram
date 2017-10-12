"""
realizar un pograma la libreria requests para poder ejecutar una peticion get a un APi. Obtner la respuesta
con clases Python. Obtner la respuesta y poder representar esa respuesta con clases Python. EL pograma debe pedir
una latitud y longitud.

"""
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE"
import requests

response = requests.get(url)
json_object_response = response.json()
#print json_object_response

class PlacesResponse(object):
    def __init__(self, place_object_response):
        self.__place_object_response = place_object_response
        self.html_attributions = self.__place_object_response["html_attributions"]
        #self.results = self.__place_object_response["results"]
        self.results = []
    def get_results(self):
        for place in self.__place_object_response['results']:
            self.results.append(place)
        return self.results

class Place(object):
    def __init__(self, place):
        self.place = place
        self.icon = place['icon']
        self.id = place['id']

results_list = PlacesResponse(json_object_response).results

places = PlacesResponse(json_object_response).get_results()
for place in places:
    print (place)



# places_list = []
#
# for lugar in places_list:
#     places_list.append(Place(lugar))
#
# #place = Place(results_list[0])
#
# #print place.id