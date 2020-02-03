# -*- coding: utf-8 -*-

import argparse
import torch

import torchvision.models
import torchvision.transforms as transforms
from PIL import Image
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
def prepare_image(image):
    if image.mode != 'RGB':
        image = image.convert("RGB")
    Transform = transforms.Compose([
            transforms.Resize([224,224]),      
            transforms.ToTensor(),
            ])
    image = Transform(image)   
    image = image.unsqueeze(0)
    return image.to(device)

def predict(image, model):
    image = prepare_image(image)
    with torch.no_grad():
        preds = model(image)
    return preds.item()
def doit(image):
    model = torchvision.models.resnet50()
    # model.avgpool = nn.AdaptiveAvgPool2d(1) # for any size of the input
    model.fc = torch.nn.Linear(in_features=2048, out_features=1)
    model.load_state_dict(torch.load(os.path.join(ROOT_DIR,'model-resnet50.pth'), map_location=device)) 
    model.eval().to(device)
    
    
    return predict(image, model)
    

if __name__ == '__main__':
    import os
    l = os.listdir("C://Users//Intel//Documents//Facepopularitypredictor//Intrinsic-Image-Popularity//images//")
    
    results = {}
    model = torchvision.models.resnet50()
    # model.avgpool = nn.AdaptiveAvgPool2d(1) # for any size of the input
    model.fc = torch.nn.Linear(in_features=2048, out_features=1)
    model.load_state_dict(torch.load('model-resnet50.pth', map_location=device)) 
    model.eval().to(device)
    for x in l:
        image_path = "C://Users//Intel//Documents//Facepopularitypredictor//Intrinsic-Image-Popularity//images//" + x
        image = Image.open(image_path)

        results[x] = predict(image, model)
    print(results)
