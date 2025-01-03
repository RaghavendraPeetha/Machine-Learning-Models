import pickle
import pandas as pd
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from mangum import Mangum

app=FastAPI()
handler=Mangum(app)

class ModelInput(BaseModel):
    pressure:float
    dewpoint:float
    humidity:int
    cloud:int
    sunshine:float
    winddirection:float
    windspeed:float

try:
    with open('rainfall_prediction_model.pkl','rb') as model_file:
        model_data=pickle.load(model_file)
        loaded_model=model_data['model']
        feature_names=model_data['feature_names']
        print(feature_names,"hiii>>>>")
        print(loaded_model.get_params())
except Exception as e:
    raise Exception(f'Error occurred while loading model: {e}')

@app.post('/predict_rainfall')
def predict_rainfall(input_data:ModelInput):
    try:
        input_dict=input_data.dict()
        input_data_df=pd.DataFrame([input_dict],columns=feature_names)

        prediction=loaded_model.predict(input_data_df)

        result='Rainfall' if prediction[0]==1 else "No Rainfall"

        return {"Prediction":result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")






