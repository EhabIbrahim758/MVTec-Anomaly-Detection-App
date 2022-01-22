# Anomaly-Detection-App
simple anomaly detection of products done by teacher student network

## Description
Anomaly Detection is one of the most important topics in computer vision as it helps companies to search and get the bad products through a network
in this project i have developed a model to predict the anomaly map of some of the most important products like :
- bottle
- cable
- capsule
- carpet
- grid
- hazelnut
- leather 
- metal nut
- pill 
- screw
- tile
- toothbrush
- transistor
- wood 
- zipper

## Aproach 
I have used the approach developed by the paper of teacher student network which is dependant of extracting features from two resnet18 networks and compare them to get the anomaly map 
The link to the paper --> https://paperswithcode.com/paper/uninformed-students-student-teacher-anomaly

## Installation 
clone the repository
- git clone https://github.com/EhabIbrahim758/MVTec-Anomaly-Detection-App.git

open the project in visual studio code and run this script in the terminal 
```python
python app.py
```
then open the resulting link to the api and then input the type of the product and the image so you will get the result

## Results 
![bottle](https://user-images.githubusercontent.com/76840608/150634998-e68c2746-162f-41ad-a5ad-f94597ac4602.PNG)

![wood](https://user-images.githubusercontent.com/76840608/150635023-deb9199c-73a1-497e-b4c3-791495234632.PNG)
