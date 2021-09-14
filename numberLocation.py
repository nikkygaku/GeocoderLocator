import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

key = "1f429012d70048e998ac7596c116ea87"

# number location
theNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(theNumber, "en")
print(yourLocation)

# service provider

from phonenumbers import carrier

serviceProvider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
print(results)

# latitude and longitude
lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)
# install the folium package
map = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to(map)

# move map to HTML file

map.save("myLocation.html")
