import streamlit as st
import tensorflow as tf
from PIL import Image
from deepface import DeepFace
import os 

def main():
      
       st.header("Görünüşüne göre yaşını bil")
       st.write("Öğrenmek için aşağıya kendi resminizi yükleyin!")
       file = st.file_uploader("Upload Photo")
       
       if file is not None:
           file_details = {"FileName":file.name,"FileType":file.type}
           st.write(file_details)
           img = tf.load_image(file)
           st.image(img,height=250,width=250)
           with open(os.path.join("https://github.com/ibrahimalsamarrae/ai_yas",file.name),"wb") as f:
               f.write(file.getbuffer())         
           st.success("Saved File")
       
       
       # if file is not None:
            # st.image(file, width=300)
            # img = Image.open(file)
            
            # image = tf.keras.preprocessing.image.img_to_array(image)
            # image = tf.image.resize(image, [224,224]) 
            # image = image / 255.0      
            # image = tf.expand_dims(image, axis=0)
            # model = tf.keras.models.load_model("yasmodel.h5") 
            # age = model.predict(image)
            
   
            # objs = DeepFace.analyze(img, actions = ['age', 'gender', 'race', 'emotion'])
            
            
            # st.markdown("## yaşınız %i gibi görünüyor" %pred[0][0])
            # st.markdown("## yaşınız %i gibi görünüyor" %objs['age'])
            
            
if __name__ == '__main__':
     main()
        
        
        
        