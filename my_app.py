import streamlit as st
import tensorflow as tf
from tensorflow.keras.utils import load_img
from PIL import Image
import os 

def main():
      
       st.header("Görünüşüne göre yaşını bil")
       st.write("Öğrenmek için aşağıya kendi resminizi yükleyin!")
       file = st.file_uploader("Upload Photo")
       
       if file is not None:
           file_details = {"FileName":file.name,"FileType":file.type}
           st.write(file_details)
           img = load_img(file)
           st.image(img,height=250,width=250)
           with open(os.path.join("https://github.com/ibrahimalsamarrae/ai_yas",file.name),"wb") as f:
               f.write(file.getbuffer())         
           st.success("Saved File") 
            
if __name__ == '__main__':
     main()
        
        
        
        