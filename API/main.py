from fastapi import FastAPI,File,UploadFile
import uvicorn 
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from tensorflow import keras


app = FastAPI()

# load the model here 
import tensorflow as tf

MODEL = keras.models.load_model("/home/aniruth/Desktop/RRC/Projects/Potato Disease Classifier/Training/saved model/2.h5")

CLASS_NAMES = ["Early Blight" , 'Late Blight' , 'Healthy']


@app.get("/ping")
async def ping():
    return "hello sir"


def read_file_as_image(data): # retuns a numpy array 
    image = np.array(Image.open(BytesIO(data))) 
    return image


# use localhost:8001/docs and debug terminal to check the working 
@app.post("/predict") # send a pic as input 
async def predict(
    file : UploadFile = File(...)
):
    
    # we need to convert this to numpy
    image = read_file_as_image(await file.read())
    
    # convert to batch 
    img_batch = np.expand_dims(image,0)

    prediction = MODEL.predict(img_batch)

    pred_class = CLASS_NAMES[np.argmax(prediction[0])] # take the first one in batch 
    confidence = np.max(prediction[0])

    return {
        "class" : pred_class ,
        "confidence":float(confidence)
    }




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)  # now the site name is localhost:800/ping




