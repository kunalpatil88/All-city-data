# views.py
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City
from .serializers import CitySerializer

class CityDataView(APIView):
    def get(self, request):
        # Read data from the JSON file
        with open('cities.json', 'r') as json_file:
            data = json.load(json_file)

        # Create a list to store City objects
        cities_to_save = []

        # Iterate through the JSON data
        for entry in data:
            # Check if a city with the same name and country already exists in the database
            existing_city = City.objects.filter(name=entry['name'], country=entry['country']).first()
            if existing_city is None:
                # If it doesn't exist, create a new City object
                city = City(
                    name=entry['name'],
                    country=entry['country'],
                    latitude=entry['lat'],
                    longitude=entry['lon']
                )
                cities_to_save.append(city)

        # Bulk create the new City objects to avoid excessive database queries
        City.objects.bulk_create(cities_to_save)

        # Serialize the data and return it in the response
        serializer = CitySerializer(cities_to_save, many=True)
        return Response(serializer.data)


