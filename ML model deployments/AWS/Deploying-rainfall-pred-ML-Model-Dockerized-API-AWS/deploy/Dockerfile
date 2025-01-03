FROM public.ecr.aws/lambda/python:3.10

COPY rainfall_prediction_model.pkl requirements.txt .

RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY main.py ${LAMBDA_TASK_ROOT}

CMD ["main.handler"]