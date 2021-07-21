import phonenumbers
from test import number
from phonenumbers import timezone 

from phonenumbers import geocoder, carrier 
  
# This will print the phone number and  
# it's basic details.
ch_no = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_no, "en"))

service_no = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_no, "en"))

# Pass the parsed phone number in below function 
timeZone = timezone.time_zones_for_number(number) 
  
# It print the timezone of a phonenumber 
print(timeZone)
