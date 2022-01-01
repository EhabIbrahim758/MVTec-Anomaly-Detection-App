import cv2
import os
import sys
from pathlib import Path
import torch
from TestingAndAPI.Inference import Inference
from Utils.functions import heatmap_on_image, min_max_norm, cvt2heatmap

all_chk_paths = os.path.join((Path.cwd()), 'ModelWeights')

def predict(img_type, transform, img_path = None, image = None):
    if img_path :
        image = cv2.imread((img_path))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   
    
    image = transform(image)
    image = image.unsqueeze(axis = 0)
    model_chk_path = os.path.join(all_chk_paths, f'model_s_{img_type}.pt')
    # model_chk_path = r'D:\ITI-- -AI-PRO\competetions\GP Anomaly Detection\Anomaly-Detection-Project\Full Project\ModelWeights\model_s_bottle.pt'
    weights = torch.load(model_chk_path, map_location=torch.device('cpu'))
    model=Inference(weights)
    a_maps, anomaly_map = model.anomaly_map(image)
    
    img = image.squeeze().numpy().transpose(1,2,0)   
    anomaly_map = anomaly_map.detach().squeeze().numpy()
    
    heatmap = cvt2heatmap(min_max_norm(anomaly_map)*255)
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)

    hm_on_img = heatmap_on_image(heatmap, img*255)
    
    os.makedirs(os.path.join(os.getcwd(),'results'), exist_ok=True)
    if img_path : 
        img_name = img_path.split('\\')[-1]
    else :
        img_name = img_type + '.png'
    save_path = os.path.join(os.getcwd(),'results', f'mask{img_name}')
    cv2.imwrite(save_path, hm_on_img*255)


    return save_path

