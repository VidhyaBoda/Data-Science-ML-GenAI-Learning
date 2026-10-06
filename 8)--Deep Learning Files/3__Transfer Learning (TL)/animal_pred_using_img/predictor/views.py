from django.shortcuts import render
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from django.core.files.storage import FileSystemStorage

model = load_model("animal_model.h5")

CLASS_NAMES = [
    'Bear','Bird','Cat','Cow','Deer','Dog','Dolphin',
    'Elephant','Giraffe','Horse','Kangaroo','Lion',
    'Panda','Bird, Parrot','Tiger','Zebra',
]

def home(request):
    prediction = None
    img_url = None

    if request.method == "POST" and request.FILES['image']:
        img_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)
        img_path = fs.path(filename)
        img_url = fs.url(filename)

        img = image.load_img(img_path, target_size=(224, 224))
        img = image.img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        pred = model.predict(img)
        prediction = CLASS_NAMES[np.argmax(pred)]

    return render(request, "index.html", {
        "prediction": prediction,
        "img_url": img_url
    })
