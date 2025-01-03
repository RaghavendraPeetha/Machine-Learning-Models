import pickle
import pandas as pd
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)

app=FastAPI()

class ModelInput(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

try:
    with open('trained_model/customer_churn_pred_model.pkl','rb') as model_file:
        model_data=pickle.load(model_file)
        loaded_model=model_data['model']
        feature_names=model_data['feature_names']

        print(loaded_model.get_params())

    with open('encoders/encoders.pkl','rb') as encoders_file:
        encoders=pickle.load(encoders_file)
except Exception as e:
    raise Exception(f"Error loading model or encoders: {e}")

@app.post('/predict_churn')
def predict_churn(input_data:ModelInput):
    try:
        input_dict=input_data.dict()
        input_data_df=pd.DataFrame([input_dict])

        for column,encoder in encoders.items():
            if column in input_data_df.columns:
                input_data_df[column]=encoder.transform(input_data_df[column])

        input_data_df=input_data_df[feature_names]

        prediction=loaded_model.predict(input_data_df)
        pred_prob=loaded_model.predict_proba(input_data_df)

        result_obj={
            "label":int(prediction[0]),
            "result":"Churn" if prediction[0]==1 else "No Churn",
            "probability":{
                "No Churn":round(pred_prob[0][0],2),
                "Churn":round(pred_prob[0][1],2)
            }
        }
        return result_obj
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid input: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during prediction {e}")