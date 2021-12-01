import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
from PIL import Image

def app():
    header = st.container()
    body = st.container()
    img_sp_votes = Image.open('assets/votes_ratio-spender.png')
    img_nsp_votes = Image.open('assets/votes_ratio-nonspender.png')
    img_sp_cor1 = Image.open('assets/spenders_sp-1.png')
    img_sp_cor2 = Image.open('assets/spenders_soc-1.png')
    img_nsp_cor1 = Image.open('assets/non-spenders_soc-1.png')
    tab="&nbsp&nbsp"

    with header:
        st.header('Correlation analysis')

    with body:
        st.markdown("To identify factors that may contribute to voters reach of the candidates, we performed correlation analysis of our data.")

        ## Spenders
        st.subheader("Potential factors contributing to spenders’ reach")
        
        # by Expenditures
        st.markdown("#### &nbsp&nbsp Expenditures")
        # st.image(img_sp_votes, width=250)
        st.image(img_sp_cor1, width=800, caption="Correlation of spender votes to different expenditures")
        st.markdown("Our results show that 91% of the votes of spenders correlated with their expenses (R=0.78).")
        st.markdown("Here, we could see a strong positive correlation between votes and total expenditures (R=0.78), and pol ads (R=0.76).")
        st.markdown("Other spending types, however, had moderate to weak correlation (R <= 0.60) to the number of votes.")
        # st.markdown("These results show that as candidates tend to invest in political advertisments, their number of votes tend to increase as well.")

        # by Social
        st.markdown("#### &nbsp&nbsp Social media interaction")
        st.image(img_sp_cor2, width=800, caption="Correlation of spender votes to social media")
        st.markdown("Here, we could see that spender votes showed weak correlations to different social media interactions.")
        st.markdown("These results might indicate that spenders were able to connect to their voters through pol ads than in social media.")
        # st.markdown("While this in the case of spenders, the results of non-spenders showed otherwise.")

        ## Non-Spenders
        st.subheader("How non-spenders establish voter reach")
        st.markdown("#### &nbsp&nbsp Social media interaction")
        st.image(img_nsp_cor1, width=800, caption="Correlation of non-spender votes to social media")
        st.markdown("While spenders appear to obtain their reach primarily through political advertisements, non-spenders appear to acquire their reach mostly through social media interactions (R = 0.98 ± 0.01).")
        st.markdown("However, this only makes up to 9% of the total votes of non-spenders, as compared to 91% from the spenders.")
        
        st.subheader("About Political Advertisements")
        st.markdown((tab*3)+"**Political adverstisments** use *mass communication*, a message intended to reach a large audience through any advertising displays, newspaper ads, billboards, signs, brochures, articles, tabloids, flyers, letters, radio or television presentations, including *social media*.")
        st.image([img_sp_votes, img_nsp_votes], width=200)
        st.markdown("In this case, even if non-spenders are able to reach voters through social media, they're still up against their spender competitors.")
        st.markdown("Because, they have not much funds to spend on travel, communication, political meetings/ rallies, etc., aside from social media, they very much have no options to reach their potential voters.")

# app()