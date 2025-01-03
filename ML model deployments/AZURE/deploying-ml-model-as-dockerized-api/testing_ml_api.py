import json
import requests

input_data={
  "pregnancies": 2,
  "Glucose": 100,
  "BloodPressure": 110,
  "SkinThickness": 8,
  "Insulin": 95,
  "BMI": 30,
  "DiabetesPedigreeFunction": 0.253,
  "Age": 30
}

json_object=json.dumps(input_data)

url="http://localhost/diabetes_prediction"

response=requests.post(url,data=json_object)


print(response.text)