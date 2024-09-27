from flask import request, jsonify, current_app
from deepface import DeepFace
import os
import pandas as pd
                
def compare():
    if 'image_1' not in request.files or 'image_2' not in request.files:
        return jsonify({'errors': 'Deux images sont nécessaires pour la comparaison'}), 400
    
    image_1 = request.files["image_1"]
    image_2 = request.files["image_2"]
    
    image1_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_1.filename)
    image2_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_2.filename)
    
    image_1.save(image1_path)
    image_2.save(image2_path)
    
    result = DeepFace.verify(
    img1_path = image2_path,
    img2_path = image1_path)
    
    return jsonify(result), 200

def compare_database():
    if 'image' not in request.files :
        return jsonify({'errors': 'Une image sont nécessaire pour la comparaison'}), 400
    
    image = request.files["image"]
    
    image_path = os.path.join(current_app.config["UPLOAD_FOLDER"], image.filename)
    
    image.save(image_path)
    
    # try :
    
    list_similarty = DeepFace.find(img_path=image_path, db_path= os.path.join('datasets/datasets_1'))

    if len(list_similarty)!=0:
    
        print(list_similarty)
        data = list_similarty[0].iloc[0].to_dict()
        
        df1_path = os.path.join('data/dataset1.csv')
        df2_path = os.path.join('data/dataset2.csv')
        
        df1 = pd.read_csv(df1_path)
        df2 = pd.read_csv(df2_path)
        
        result = pd.merge(df1, df2, on="Path")
        
        paths = data["identity"].split("/")[-1]
        
        print(paths)
        
        path_list = result[result["Path"]==paths]
        
        print(path_list.to_dict("list"))
        
        if len(path_list["Lastname"])!=0:

            return jsonify(path_list.to_dict("list")),200
        else :
            return jsonify({"errors": "Not match"}),404
    
    else :
        return jsonify({"errors": "Cette personne n'a pas de correspondant dans notre base de donnée"}),404
    
    