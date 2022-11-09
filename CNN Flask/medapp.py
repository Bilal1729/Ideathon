import numpy as np
import os
import keras
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask , request, render_template
#from gevent.pywsgi import WSGIServer

app = Flask(__name__)

model = load_model(r"C:\Ideathon\POC\MED_PLANT_SNAPS\MED_PLANT_SNAP.h5")
                 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)
        
        img = image.load_img(filepath,target_size = (64,64)) 
        x = image.img_to_array(img)
        print(x)
        x = np.expand_dims(x,axis =0)
        print(x)

       # preds = model.predict_classes(x)
        y=model.predict(x)
        preds=np.argmax(y,axis=1)
       
        print("The plant that you have uploaded is",class_prediction)
        index = ['Alpinia Galanga (Rasna)','Amaranthus Viridis (Arive-Dantu)','Artocarpus Heterophyllus (Jackfruit)','Azadirachta Indica (Neem)','Basella Alba (Basale)','Brassica Juncea (Indian Mustard)','Carissa Carandas (Karanda)','Citrus Limon (Lemon)','Ficus Auriculata (Roxburgh fig)','Ficus Religiosa (Peepal Tree)','Hibiscus Rosa-sinensis','Jasminum (Jasmine)','Mangifera Indica (Mango)','Mentha (Mint)','Moringa Oleifera (Drumstick)','Muntingia Calabura (Jamaica Cherry-Gasagase)','Murraya Koenigii (Curry)','Nerium Oleander (Oleander)','Nyctanthes Arbor-tristis (Parijata)','Ocimum Tenuiflorum (Tulsi)','Piper Betle (Betel)','Plectranthus Amboinicus (Mexican Mint)','Pongamia Pinnata (Indian Beech)','Psidium Guajava (Guava)','Punica Granatum (Pomegranate)','Santalum Album (Sandalwood)','Syzygium Cumini (Jamun)','Syzygium Jambos (Rose Apple)','Tabernaemontana Divaricata (Crape Jasmine)','Trigonella Foenum-graecum (Fenugreek)']
        text = "The name of the plant that you have uploaded and their mrdicinal uses is " + str(medicine)
    return text
if __name__ == '__main__':
    app.run(debug = True, threaded = False,port=8000)