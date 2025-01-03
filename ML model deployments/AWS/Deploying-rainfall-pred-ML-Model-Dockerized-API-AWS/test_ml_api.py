import json
import requests

input_data={
  "pressure": 1018.9,
  "dewpoint": 18.8,
  "humidity": 90,
  "cloud": 88,
  "sunshine": 1,
  "winddirection": 50,
  "windspeed": 16.9
}

url='https://azo6ini4coe45e4ywmyuoo6q5m0aprjq.lambda-url.ap-south-1.on.aws/predict_rainfall'

json_object=json.dumps(input_data)

response=requests.post(url,data=json_object)

print(response.json()['Prediction'])
