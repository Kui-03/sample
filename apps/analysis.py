import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
from PIL import Image

def app():
    header = st.container()
    body = st.container()
    image = Image.open('assets/g1.png')
    image2 = Image.open('assets/g2.png')
    image3 = Image.open('assets/g3.png')
    image4 = Image.open('assets/g4.png')

    df_senatorialvotes = pd.read_csv('data/2019-senatorial-votes.csv')
    df_candidatecamps = pd.read_csv('data/2019-candidate-campaigns.csv')
    #merged = df_candidatecamps.merge(df_senatorialvotes, how='inner')

    with header:
        st.header('Exploratory Data Analysis')

    with body:
        # Insight on candidate demographics
        st.subheader("Insight on candidate demographics")
        txt = """
            First, we classified candidates according to those who invested in their political campaigns (spenders), and those who did not spend any money on campaigns (non-spenders).
        """
        st.markdown(txt)
        st.image(image, width=300)
        st.markdown("We found out that:")
        txt = '''
            - The majority of candidates (68%) were spenders, while the remaining (32%) were non-spenders.
            - All of the candidates who **won** the 2019 senatorial elections, belong to the group of **spenders**.
        '''
        st.markdown(txt)

        # Top Candidate Spenders
        st.subheader('2019 Top Election Candidate Spenders')
        st.image(image2, width=700)
        st.markdown(' - We then ranked the top 10 candidates according to the highest spending to determine whether a higher spending provides a higher chance of winning.')
        st.markdown(" - We found out that **6 out of the 10** top spenders won the elections.")
        # st.markdown(" - Though a higher spending might indicate winning 60% of the time, this result is not enough ")

        # Insight on candidate spendings
        st.subheader('Insight on candidate spendings')
        st.image(image3, width=800)
        st.markdown("To find out where spenders mostly invests on, we further looked into the breakdown of their expenses.")
        st.markdown('It is shown that most of the candidates focused on political advertisements (89.69%), which indicates that spenders mainly reach out to voters using pol ads.')
        # Insight on candidate votes
        st.subheader('Insight on candidate votes')
        st.image(image4, width=300)
        st.markdown("In our analyses, we also determined how much votes did spenders and non-spenders accumulate.")
        st.markdown('According to our findings, spenders make most out of the votes having 91% of the total votes, while non-spenders only got 9%.')
        st.markdown('In this scenario, we want to see whether spending money in pol ads can help you reach more voters.')
        st.markdown('And if this is the case, how much would non-spenders be missing out?')
        st.markdown('We take a deeper look into this in our correlation analysis.')

# app()