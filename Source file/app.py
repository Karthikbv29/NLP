import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

course_df=pickle.load(open("C:/Users/karth/Downloads/course_df.pkl",'rb'))
similarity=pickle.load(open("C:/Users/karth/Downloads/cosine_sim.pkl",'rb'))
list_courses=np.array(course_df['Name'])

indices = pd.Series(course_df['Name'])

# this function takes in a course name as input and returns the top 5 recommended (similar) courses

def recommend(name, cosine_sim = similarity):
    recommended_courses = []
    idx = indices[indices == name].index[0]   # to get the index of the course name matching the input course
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)   # similarity scores in descending order
    top_5_indices = list(score_series.iloc[1:6].index)   # to get the indices of top 6 most similar courses
    # [1:6] to exclude 0 (index 0 is the input course itself)
    
    for i in top_5_indices: # to append the names of top 5 similar courses to the recommended_courses list
       recommended_courses.append(list(course_df['Name'])[i])
    return recommended_courses


st.title('Course Recommendation System')
menu=['Home','Recommend','About']
choice=st.sidebar.selectbox("Menu",menu)
if choice=='Home':
    st.subheader('Home')
    img=Image.open("C:/Users/karth/Downloads/features-of-mooc.jpg")
    st.image(img,caption='Learning never ends')
    st.text('This is a Recommendation System built using Content-based filtering.')
elif choice=='Recommend':
    option=st.selectbox('Select Course',(list_courses))
    if st.button('Recommend'):
        st.write('Courses Recommended for you are:')
        df=pd.DataFrame({
        'Course Recommended':recommend(option)
        })
        st.table(df)
else:
    st.subheader('About')
    img1=Image.open("C:/Users/karth/Downloads/streamlit.jpg")   
    resized_img1=img1.resize((round(img1.size[0]*1),round(img1.size[1]*0.5))) 
    st.image(resized_img1)
    st.text('Built using Streamlit')    