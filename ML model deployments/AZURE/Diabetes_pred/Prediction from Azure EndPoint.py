import json
import requests

input_data=[1,89,66,23,94,28.1,0.167,21]

input_data_json=json.dumps({'data':[input_data]})

scoring_uri="http://e21ef61a-e945-4201-88f1-e045dfd6215e.centralindia.azurecontainer.io/score"

headers={"content-Type":"application/json"}

response=requests.post(scoring_uri,data=input_data_json,headers=headers)

if response.status_code==200:
    result=json.loads(response.json())
    print(result)
    prediction=result['result'][0]
    print(f"prediction: {prediction}")
else:
    print(f"Error: {response.text}")