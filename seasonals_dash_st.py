import streamlit as st
import os

st.set_page_config(layout="wide")

# Get the directory where the Streamlit app script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the subdirectory containing the images relative to the script directory
image_dir = "Dash_images"

# Get the full path to the image directory
image_dir_path = os.path.join(script_dir)

# Get a list of all image files in the directory
image_files = os.listdir(image_dir_path)

# Loop over the image files and display them
for image_file in image_files:
    image_path = os.path.join(image_dir_path, image_file)
    st.image(image_path, output_format='PNG')

# for x in charts:
# 	st.image(x,output_format='PNG')

# with col1:	
# 	for x in charts[0:9]:
# 		st.image(x,output_format='PNG', width=600)

# with col2:
# 	for x in charts[9:18]:
# 		st.image(x,output_format='PNG',width=600)

# with col3:
# 	for x in charts[18:]:
# 		st.image(x,output_format='PNG',width=600)