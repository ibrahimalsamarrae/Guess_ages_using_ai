import streamlit as st
import tensorflow as tf
from PIL import Image
from deepface import DeepFace


def main():
    st.header("Görünüşüne göre yaşını bil")
    st.write("Öğrenmek için aşağıya kendi resminizi yükleyin! ")
    file = st.file_uploader("Upload Photo")
    if file is not None:
        st.image(file)
        image = Image.open(file)
        img=image
        image = tf.image.resize(image, [224,224]) 
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image / 255.0      
        image = tf.expand_dims(image, axis=0)
        
     
      
        
        model = tf.keras.models.load_model("my_model.h5")
        sonuc = DeepFace.analyze(img, actions = ['age'])
        age = model.predict(image)
        st.markdown("## yaşınız %i gibi görünüyor" %age[0][0])
        st.markdown("## yaşınız %i gibi görünüyor" %sonuc['age'])
    
if __name__ == '__main__':
	main()