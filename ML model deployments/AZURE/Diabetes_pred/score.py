import json
import joblib
import numpy as np
from azureml.core.model import Model

def init():
    global model
    model_path=Model.get_model_path('diabetes_prediction_model')
    model=joblib.load(model_path)

def run(raw_data):
    try:
        data=json.loads(raw_data)['data']
        data=np.array(data).reshape(1,-1)

        result=model.predict(data)

        return json.dumps({'result':result.tolist()})

    except Exception as e:
        return json.dumps({'error':str(e)})
