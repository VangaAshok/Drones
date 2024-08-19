import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restful01.settings')

django.setup()  # Initialize the Django environment



from datetime import datetime
from django.utils import timezone
from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer
import json

# toy release date--> current date and time - present timezone
toy_release_date = timezone.make_aware(datetime.now(),
timezone.get_current_timezone())

#create 1-toy instance
toy1 = Toy(name='Ashok', 
    description='speaks five languages', release_date=toy_release_date,
    toy_category='Action figures', was_included_in_home=False)
# save 1-toy instance; Toy.objects.create automatically saves the new instance to database
# toy1.save()

# create 2-toy instance
toy2 = Toy(name='Hawaiian Barbie', description='Barbie loves Hawaii',
release_date=toy_release_date, toy_category='Dolls',
was_included_in_home=True)
#save 2-toy instance
# toy2.save()

# print(toy1.pk)
# print(toy1.name)
# print(toy1.created)
# print(toy1.was_included_in_home)
# print(toy2.pk)
# print(toy2.name)
# print(toy2.created)
# print(toy2.was_included_in_home)

# #code to serialize the 1-toy instance

# serializer_for_toy1 = ToySerializer(toy1)
# #print serialized data
# print(serializer_for_toy1.data)
# print(ToySerializer(toy1).data)
# python dictionary output data
#>>> {'id': 28, 'name': 'Ashok', 'description': 'speaks five languages', 
#     'release_date': '2024-07-17T15:23:09.686255Z', 
#     'toy_category': 'Action figures', 'was_included_in_home': False}


#to verify fields in toy1 instance
# print(toy1.__dict__)

# serializer_for_toy2 = ToySerializer(toy2)
# print(serializer_for_toy2.data)


#  render the dictionaries held in the data attribute into JSON 
# using rest_framework.renderers.JSONRenderer class
 
# rendering data from dictionary to JSON
# toy1_rendered_into_json = JSONRenderer().render(serializer_for_toy1.data)
# toy2_rendered_into_json = JSONRenderer().render(serializer_for_toy2.data)
#print data in JSON format
# print(toy1_rendered_into_json)
#>>> b'{"id":32,"name":"Ashok","description":"speaks five languages",
#       "release_date":"2024-07-17T15:37:05.261263Z",
#       "toy_category":"Action figures","was_included_in_home":false}'
# print(toy2_rendered_into_json)


"""
    
    in above created an instance e.g: toy1 in dictionary format....
    and converted the dict data into json data format by using 'renderer'
"""
"""
    now below reversing the above process i.e., json string(serilaized data)
    to dict format by using 'paser'
    json string -> json bytes -> stream objects(file-like objects) -> dict data
"""
# json string 

dict_for_new_toy ={
"name":"Clash Royale play set",
"description": "6 figures from Clash Royale",
"release_date": "2017-10-09T12:10:00.776594Z", 
"toy_category": "Playset",
"was_included_in_home": False
}

#convert dict to json string
# load dict string into dict and dump into json
# dict_load = json.loads(dict_for_new_toy)
# print(dict_load)

json_string_for_new_toy = json.dumps(dict_for_new_toy)
# print(json_string_for_new_toy)
#>>>{
#     "name":"Clash Royale play set",
#     "description":"6 figures from Clash Royale",
#     "release_date":"2017-10-09T12:10:00.776594Z",
#     "toy_category":"Playset",
#     "was_included_in_home":false
# }


# json_bytes_for_new_toy = bytes(json_string_for_new_toy, encoding="UTF-8")
# stream_for_new_toy = BytesIO(json_bytes_for_new_toy)
stream_for_new_toy = BytesIO(json_string_for_new_toy.encode('utf-8'))
parsed_new_toy = JSONParser().parse(stream_for_new_toy)
print(parsed_new_toy)
#>>> {'name': 'Clash Royale play set', 
# 'description': '6 figures from Clash Royale', 
# 'release_date': '2017-10-09T12:10:00.776594Z', 
# 'toy_category': 'Playset', 'was_included_in_home': False}

#creating new toy from parsed data
new_toy_serializer = ToySerializer(data=parsed_new_toy)
# print(new_toy_serializer)
if new_toy_serializer.is_valid():
    toy3 = new_toy_serializer.save()
    print(toy3.name, toy3.id)
else:
    print('Validation errors')




