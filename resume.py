import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write('''
# Ahmed Ali Sabry, Data Scientist.
### *Resume* 
''')

image = Image.open('IMG_20230603_104506.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Iam a data scientist with expertise in data preprocessing and data analysis (EDA) and Classifications,Regressions Machine Learning algorithms and Deep Learning and Time Series, CNN, RNN, NLP, Recommendation System and a passion for delivering insights based on predictive modeling. 
- Successfully completed over 60 projects on Kaggle from understanding businees problem till making a model by Machine Learning and Deep Learning. showcasing proficiency in RFM analysis, churn rate prediction, customer segmentation, CLV estimation,Reviews Sentiment Analysis and price predictions for various markets including stocks, houses, and laps.
- Strong problem-solving skills demonstrated through development of more than 50 repositories on GitHub and 7 streamlit projects for price predictions and recommendation systems. Looking to leverage diverse skill set and experience to help companies make data-driven decisions.
''')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  </a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
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
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

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
  
def txt4(a, b, c ,d):
  col1, col2, col3, col4 = st.columns([3,4,3,3])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
  with col4:
    st.markdown(d)

def txt5(a, b, c):
  col1, col2, col3 = st.columns([3,3,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

st.markdown('''## Education''')
txt('**Bachelors of Faculty of Engineering (Civil Engineer), Zagazig University, Egypt**',
'**2006-2011**')
st.markdown('''
- Graduated with 61%.
''')

st.markdown('''## Work Experience''')

txt(' **Successfully completed over 60 projects on Kaggle and developed more than 50 repositories on GitHub and 7 streamlit projects.**',
'**2022-2023**')
st.markdown('''
- Successfully completed over 60 projects on Kaggle and developed more than 50 repositories on GitHub and 7 streamlit projects. 
- finishing this projects from  Problem understanding and Data Preprocessing , Data Analysis (EDA) till model dvelopment to solve the problem for various problems such as  RFM analysis, churn rate prediction, customer segmentation, CLV estimation, CNN , RNN ,Sentiment Anlaysis by NLP , Classifications ,and price predictions for various markets including stocks, houses, and laps.
''')

txt('**Project Manager**,**Tatwar Group For Constructions and Development**',
'**2020-2023**')
st.markdown('''
- civil engineer project manager for more than one site.
- Knowledgeable in implementation the project from start to finish with lower cost&lower time and high quality.
''')

txt('**Project Manager**,**Dakahlia Group For Development**',
'2014-2017')
st.markdown('''
-in this period I promotes to a project manager and I was responsible for several sites at the same time and my job was observations on sites engineers and supervisors.
''')

txt('**Technical Writer**, [Ahmadsabry Blog](https://medium.com/@ahmadsabry678) on Medium.com',
'2023-2023')

st.markdown('''## Projects''')
txt4('Boston House Price Prediction Application.', 'application for house price prediction from understanding business and Data Preprocessing and Visualization till price prediction', 'https://ahmedsabre-boston-house-price-bostonhousepriceprediction-by41kz.streamlit.app' , 'https://github.com/ahmedsabre/boston_house_price_prediction_application')
txt4('House Price Pridiction Application', 'application for house price prediction from understanding business and Data Preprocessing and Visualization till price prediction', 'https://ahmedsabre-house-price-pridiction-a-housepricepridiction-dxh5ml.streamlit.app/','https://github.com/ahmedsabre/house_price_pridiction_app')
txt4('Iris Classification Prediction Application', 'application for iris classification prediction from understanding business and Data Preprocessing till classification prediction','https://ahmedsabre-irisclassification-predict-irisclassification-x01l06.streamlit.app','https://github.com/ahmedsabre/irisclassification_prediction_app')
txt4('penguins species prediction Application', 'application for penguins classification prediction from understanding business till classification prediction', 'https://ahmedsabre-penguins-species-prediction-app-penguinsapp-ou3hps.streamlit.app','https://github.com/ahmedsabre/penguins_species_prediction_app')
txt4('Stock Price Application', 'Application for price movement and stationarity for stock price ','https://ahmedsabre-stockpriceapp-stockprice-p0wcwp.streamlit.app','https://github.com/ahmedsabre/stockpriceAPP')
txt4('Lap Prices Application', 'Application for laptops price prediction', 'https://ahmedsabre-lappricesapp-laptoppriceapp-waiqrz.streamlit.app','https://github.com/ahmedsabre/LapPricesAPP')
txt4('Movies Recommendation System Application', 'Application for movies recommendation system by content first making data preprocessing then count vectorizer then similarity measurements by cosine similarity','https://github.com/ahmedsabre/movies_recommendation_system','https://github.com/ahmedsabre/movies_recommendation_system')
txt5('CNN', 'photo classification for mnist data by ANN', 'https://github.com/ahmedsabre/CNN')
txt5('predicting employee attrition', 'Prediction Employee Attrition by classification algorithms first making data preprocessing then visualization then prediction with classification algorithms ', 'https://github.com/ahmedsabre/attrition-classification')
txt5('Web Scraping', 'scrapes fake and real news data from website from PolitiFact', 'https://github.com/ahmedsabre/data-web-scraping')
txt5('Spam Filter', 'detecting if the email is spam or not by NLP and Naive Bayes', 'https://github.com/ahmedsabre/spam-filter-naive_bayes')
txt5('Credit Card Fraud Detection', 'credit card fraud detection by machine learning and deep learning', 'https://github.com/ahmedsabre/credit-card-fraud-detection')
txt5('Customer Segmentation by unsupervised algorithms', 'making customer clustering for campaigns by KMeans , AgglomerativeClustering first making data preprocessing then data visualization then clustering the data', 'https://github.com/ahmedsabre/customer-Segmentation')
txt5('Customer Reviews Analysis NLP', 'flipkart product customer reviews analysis by TextBlob and get word cloud and polarity ', 'https://github.com/ahmedsabre/customer-review-analysis')
txt5('Sentiment Analysis NLP', 'reviews sentiment analysis using 2 different techniques: VADER and  Roberta Pretrained Model from HuggingFace Pipeline by data preprocessing by NLTK and ploting the results','https://github.com/ahmedsabre/sentiment-analysis-hugging-face')
txt5('Image Classification by CNN', 'classification images for hand written digits','https://github.com/ahmedsabre/-CNN-image-classification-')
txt5('House Price Prediction', 'house price pridiction by ML with Linear Regression and Random Forest and GridSearch CV','https://github.com/ahmedsabre/house-price-prediction')
txt5(' NO. of Air Passengers Prediction','predict number of air passengers for time period by making preprocessing to check the stationarity and plot the data and predict by SARIMAX Algorithm  ', 'https://github.com/ahmedsabre/timeseries-by-SARIMAX')
txt5('Energy Consume Prediction', 'predict the energy consume for time period by XGBoost and determine the most important feature','https://github.com/ahmedsabre/time-series-prediction')
txt5('Customer Churn Prediction', 'teleco customer churn from  data preprocessing till prediction by ML','https://github.com/ahmedsabre/customer-churn')
txt5('Customer Lifetime Value', 'calculate customer lifetime value by lifetimes library','https://github.com/ahmedsabre/Customer-Lifetime-Value')
txt5('Customer Segmentation by RFM', 'segment customer according to recency frequency monetary to detect the most important customers','https://github.com/ahmedsabre/customers-segmentation-by-RFM-ANALYSIS')
txt5('Customer Deposit Prediction', 'predict if the client will subscribe (yes/no) to the term deposit by classification models ','https://github.com/ahmedsabre/Bank-Marketing-Data-Set')
st.markdown('''## Skills''')
txt3('Programming', '`Python`,`Power BI`')
txt3('Data processing/wrangling', '`Pandas`, `numpy`, `Pandas_Profiling`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `PGYWalker`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`streamlit`,`Heroku`')
txt3('Language', '`English`,`German`')

st.markdown('''## Social Media''')
txt2('LinkedIn', 'https://www.linkedin.com/in/ahmed-ali-47abbb172/')
txt2('GitHub', 'https://github.com/ahmedsabre')
txt2('Kaggle', 'https://www.kaggle.com/ahmadali3')
txt2('Medium', 'https://medium.com/@ahmadsabry678')