import streamlit as st
import os

st.set_page_config(layout="wide")
# col1, col2, col3 = st.columns(3)
# file_loc=r'C:\Users\McKinley Slade\Dropbox\MS Docs\Work\Sublime_Misc\Dash_images'
# charts=os.listdir(r'C:\Users\McKinley Slade\Dropbox\MS Docs\Work\Sublime_Misc\Dash_images')

file_loc=r'C:\Users\Lenovo user\Dropbox\MS Docs\Work\Sublime_Misc\Dash_images'
charts=os.listdir(r'C:\Users\Lenovo user\Dropbox\MS Docs\Work\Sublime_Misc\Dash_images')


# file_loc=r"C:\Users\McKinley\Dropbox\MS Docs\Work\Sublime_Misc\Dash_images\seasonals_dash_st.py"
# charts=os.listdir(r'C:\Users\McKinley\Dropbox\MS Docs\Work\Sublime_Misc\Dash_images')

del charts[13]

for x in charts:
	st.image(x,output_format='PNG')

# with col1:	
# 	for x in charts[0:9]:
# 		st.image(x,output_format='PNG', width=600)

# with col2:
# 	for x in charts[9:18]:
# 		st.image(x,output_format='PNG',width=600)

# with col3:
# 	for x in charts[18:]:
# 		st.image(x,output_format='PNG',width=600)