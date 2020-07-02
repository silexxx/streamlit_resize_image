import streamlit as st

from PIL import Image

count=0


image = st.sidebar.file_uploader("Upload")
if image != None:
	img = Image.open(image)
	count=1
	st.image(image,caption="inserted image",use_column_width=True)


new_width  = st.sidebar.slider("set height",0,10000,300)
new_height = st.sidebar.slider("set width",0,10000,300)

if count==1:
	img = img.resize((new_width, new_height), Image.ANTIALIAS)


	
	st.image(img,caption="new image",use_column_width=True)


	st.write("Now right click and save as to save the image ")
	

