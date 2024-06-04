import streamlit as st
from PIL import Image

st.set_page_config(page_title="Emmanuel Nenchin", page_icon=":shark:", layout="wide")

#st.title("Emmanuel Nenchin")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Head
st.markdown("""
# EMMANUEL Nenchin
#### Data Scientist""")

# dp
img = Image.open("images/en1.jpg")
st.image(img, width=150)

st.markdown("### About Me", unsafe_allow_html=True)
st.info("""
        I am a Data Scientist with an Engineering background. I have a passion for solving real-world 
        problems using data and machine learning. I am proficient in Python, SQL, Tableau, and Excel. 
        I have experience in building machine learning and deep learning models, data analysis, and 
        visualization with a specialization in NLP. I am a fast learner and a team player. I am looking 
        for opportunities to work on challenging projects that will help me grow as a Data Scientist.
        """)

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/Nenchin" target="_blank">Emmanuel Nenchin</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#articles">Articles</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom functions for texts
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt5(a, b, c):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f"<a class='nav-link' href='{c}'>`{a}`</a>", unsafe_allow_html=True)
  with col2:
    st.markdown(b)


#####################
st.markdown("""
## Education
""")

txt("**Bachelors of Engineering** (Electrical Electronics Engineering), *Federal University of Technology Minna*, Minna, Niger State, Nigeria", "2018-2024")
st.markdown("""
- CGPA: `3.69`
""")

#####################
st.markdown("""
## Work Experience
""")

txt("**Tutor (Data Science)**, NAMTES-FUTMinna", "March 2024, June 2024")
st.markdown("""
- Took a class on Machine Learning for beginners at the Skill Acquisiton Program organised by NAMTES FUTminna Chapter.
""")

txt("**Mentor (Data Science)**, CADEMit", "November 2023, January 2024")
st.markdown("""
- Took a class on Data Science and Machine Learning for beginners at the Digital skill Career Track Mentorship Cohort 1.0 by CADEMit.
""")

txt("**Data Scientist**, Provarex", "2023-Present")
st.markdown("""
- Developing Data and AI solutions to improve the company's growth and meet its customers' needs.
""")

txt("**Data Lead**, Ingressive for Good, FUTMinna Circle", "2023-Present")
st.markdown("""
- Promoting the knowledge of data skills in and around the Circle.
""")

txt("**Engineer (Intern)**, Artificial Intelligence for Clean Energy Limited", "2023-2024")
st.markdown("""
- Help in the development of AI models for the company's projects.
""")

txt("**Tutor**, Explore Machine Learning Bootcamp Series - GDCS, FUTMinna", "May 2023")
st.markdown("""
- Explore Machine Learning (ML) is a Google-sponsored program for university students to get started with Machine Learning.
""")

txt("**Public Relations Officer**, Google Developers Student Club, FUTMinna Chapter", "2022-2023")
st.markdown("""
- Incharge of information dissemination and circulation in the community.
""")

txt("**Student Research Assistant**, Advance Engineering Innovation Research Group, FUTMinna", "2021-Present")
st.markdown("""
- Assisting in research and physical installation of various electrical and electronics equipments.
- Providing project improvement recommendations.
- Providing support and assistance on AI researches.
""")

txt("**Computer Operator**, HedgeMarks Integrated", "2018-2021")
st.markdown("""
- Digital documentation.
- Scanning and printing of documents of various sizes.
""")

#####################
st.markdown("""
## Projects
""")
txt4("biz_chat", "A Business development chatbot for creating BMCs", "https://github.com/Nenchin/biz_chat")
txt4("hogFE", "Feature extraction using HOG feature extraction technique", "https://github.com/Nenchin/HOG_feature_extraction")
txt4("CryptojackingDetector", "Model for detection of cryptojacting","https://github.com/Nenchin/umojahack-africa-2023-intermediate-challenge")
txt4("Intro", "Lessons during my introduction to Data Science and Machine Learning", "https://github.com/Nenchin/my-intro-to-ml")
txt4("AI4PM", "A web server for predicting flowrate", "https://github.com/Nenchin/ai4pm")
txt4("FaceRecogniton", "Face recognition app using python's face-recognition library and KNN", "https://github.com/Nenchin/face-recognition-app-using-recognition-library-and-knn")
txt4("maize-weed-detector", "Object detection model maize and weed detection", "https://github.com/Nenchin/maize-detection-using-yolov4-")
txt4("health_news_tweets", "clustering and classification of health tweets", "https://github.com/Nenchin/health_news_tweets_nlp")
txt4("Customer Review Analysis", "Sentiment analysis of British Airways customers' review", "https://github.com/Nenchin/british_airways_internship_simulation")
txt4("fruit_classifier", "Deep learning model for fruit classification (Good, Mild, and Rotten)", "https://github.com/Nenchin/fruit_classifier")
txt4("electricity_fraud_detection", "Model for electricity fraud detection", "https://github.com/Nenchin/electricity_fraud_detection")
txt4("analysis-of-co2-emission-in-nigeria", "Analysis of Nigeria's carbon emission from 2000-2021","https://github.com/Nenchin/analysis-of-co2-emission-in-nigeria")
txt4("IV4PM", "CNN model for detection of defects in pipelines","https://github.com/Nenchin/cnn-for-pipeline-defect-detection")
txt4("CatDogClassifier", "This was my first lesson on image classification","https://github.com/Nenchin/cat_dog_classifier")


#####################
st.markdown("""
## Skills
""")
txt3("Programming", "`Python`")
txt3("Data processing/wrangling", "`SQL`, `pandas`, `numpy`")
txt3("Data visualization", "`matplotlib`, `seaborn`, `plotly`, `Tableau`")
txt3("Machine Learning", "`scikit-learn`")
txt3("Deep Learning", "`TensorFlow`")
txt3("Web development", "`Flask`, `Django`, `Streamlit`")
txt3("Model deployment", "`Streamlit`, `PythonAnywhere`")

#####################
st.markdown("""
## Articles
""")
txt5("Data Tree: A Harvest of Diverse Data Careers", """Welcome to the Data Tree, a comprehensive but definitely not exhaustive guide to explore the diverse applications and 
     exciting prospects this dynamic and sumptuous tree offers! The Data Tree is a super-awesome tree, with its branches laden with a vibrant tapestry of fruits.""", 
     "https://medium.com/@emmanuelnenchin/the-data-tree-a-harvest-of-diverse-data-careers-4ee18d75d4c1?source=user_profile---------0----------------------------")
txt5("Unleash Python’s Power: A Roadmap for Mastering Diverse Applications in 2024", """Have you ever dreamt of automating tasks, analysing data, building web apps, 
     or controlling robots? Python, the versatile programming language, can make it a reality! Are you ready to unlock its potential?""", 
     "https://medium.com/@emmanuelnenchin/unleash-pythons-power-a-roadmap-for-mastering-diverse-applications-in-2024-0c0908421905?source=user_profile---------1----------------------------")

#####################
st.markdown("""
## Social Media
""")
txt2("LinkedIn", "https://www.linkedin.com/in/nenchinemmanuel")
txt2("Twitter", "https://twitter.com/Mr_NNarnia")
txt2("GitHub", "https://github.com/Nenchin/")