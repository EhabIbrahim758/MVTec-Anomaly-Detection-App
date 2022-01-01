from logging import debug
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import cv2
from fastapi.datastructures import UploadFile
from fastapi.params import File

from TestingAndAPI.Prediction import predict
from Utils.functions import data_transformation
from Utils.read_img import read_image
from TestingAndAPI.RequestPath import Image_path

test_transform = data_transformation()['test']

app = FastAPI()

@app.get('/')
def index() :
    return 'Anomaly Detection App'

@app.post('/predict_by_img_path') 
def predict_anomaly_map(img_data : Image_path) :
    data = img_data.dict()
    img_path = data['img_path']
    img_type = data['img_type']
    save_path = predict(img_type, transform = test_transform, img_path = img_path)
    
    return FileResponse(save_path) 


@app.post('/predict_by_image') 
async def predict_anomaly_map(img_type : str, file : bytes = File(...)) :
    image = read_image(file)
    save_path = predict(img_type, transform = test_transform, image = image)
    
    return FileResponse(save_path) 



if __name__ == '__main__' :
    uvicorn.run(app, debug = True)



