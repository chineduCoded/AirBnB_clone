#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create  a new State --")
new_state = State()
new_state.name = "Nigeria"
new_state.save()
print(new_state)

print("-- Create  a new City --")
new_city = City()
new_city.state_id = "ng001"
new_city.name = "Lagos"
new_city.save()
print(new_city)

print("-- Create  a new Amenity --")
new_amenity = Amenity()
new_amenity.name = "Kitchen utensils"
new_amenity.save()
print(new_amenity)

print("-- Create  a new Place --")
new_place = Place()
new_place.city_id = "lg-001"
new_place.user_id = "eli01"
new_place.name = "Ikosi"
new_place.decription = "located at ketu"
new_place.number_rooms = 4
new_place.number_bathrooms = 2
new_place.max_guest = 3
new_place.price_by_night = 6000
new_place.latitude = 3.2345
new_place.longitude = 4.5634
new_place.amenity_ids = ["ab2", "ac3"]
new_place.save()
print(new_place)

print("-- Create  a new Review --")
new_review = Review()
new_review.place_id = "lg-001"
new_review.user_id = "us01"
new_review.text = "Look good"
new_review.save()
print(new_review)
