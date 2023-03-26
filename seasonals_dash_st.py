import streamlit as st
import os

st.set_page_config(layout="wide")

file_loc = "."
charts = [x for x in os.listdir(file_loc) if x.lower().endswith((".jpg", ".jpeg", ".png"))]

for x in charts:
    image_path = os.path.join(file_loc, x)
    st.image(image_path, width=800,output_format='PNG')

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
