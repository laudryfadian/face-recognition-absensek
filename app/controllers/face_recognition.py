from deepface import DeepFace
from app.utils import *

def face_recog_deepface(image1, image2, model):
  recog = DeepFace.verify(img1_path=image1, img2_path=image2, model_name=model)
  if recog['distance'] > 0.36:
    return False #gagal face recognition
  
  return True #berhasil face recognition