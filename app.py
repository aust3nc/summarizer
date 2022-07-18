#imports 
import streamlit as st
from scraper import s
from bart import b
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wc(text):
    wc = st.radio(
            "Would you like a visualization of frequent words in your search?",
            ('Yes', 'No'))
    if wc == 'Yes':
        wordcloud = WordCloud(width=800, height=400, random_state=21).generate(response)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()
#add submit button

S = s()

choice = st.radio(
     "What would you like to scrape? ",
     ('URL', 'Query'))
    
if choice == 'URL':
    url = st.text_input('URL:', help='Enter the URL and press Enter/Return')
    if url:
        urlText = S.makeUrlQuery(url)
        response = b(urlText, 4, 1.5, 250, 250, 2)
        st.text_area(label = "Summary", value = response)
        wc(response)
else:
    query = st.text_input("Query: ", help='Enter the search string and press Enter/Return')
    urlCount = st.number_input("How many results would you like to scrape?", 1, 25, 5, 1)
    if query:
        queryText = S.makeQuery(query, urlCount)
        response = b(queryText, 4, 1.5, 250, 250, 2)
        st.text_area(label = "Summary", value = response)
        wc(response)



