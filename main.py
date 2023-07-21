import requests
import json
def get_prediction(CarModel,Age,Mileage):
  data={"Car Model":CarModel,"Age(yrs)":Age,"Mileage":Mileage}
  url = 'https://askai.aiclub.world/0eaeb473-e129-4ec9-85b2-d538d3887b56'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  predicted_label = json.loads(json.loads(response)['body'])['predicted_label']
  return predicted_label
car_name = input('Hello, I am a chat bot. Please state the car you own: ')

age = int(input('How old is your car(In years)? '))

mileage = int(input('What is the milelage? '))
respond=get_prediction(car_name,age,mileage)
print (int(respond))