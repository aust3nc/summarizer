#imports 
import streamlit as st
from scraper import s
from bart import b

S = s()

choice = st.radio(
     "What would you like to scrape? ",
     ('URL', 'Query'))
    
if choice == 'URL':
    url = st.text_input('URL:', help='Enter the URL and press Enter/Return')
    if url:
        urlText = S.makeUrlQuery(url)
        length = st.number_input("Enter the preferred length of your summary.", 250, 750, 250, 1)
        response = b(urlText, 4, 1.5, length, length, 2)
        st.text_area(label = "Summary", value = response)
else:
    query = st.text_input("Query: ", help='Enter the search string and press Enter/Return')
    urlCount = st.number_input("How many results would you like to scrape?", 1, 25, 5, 1)
    if query:
        queryText = S.makeQuery(query, urlCount)
        length = st.text_input("Enter the preferred length of your summary" )
        response = b(queryText, 4, 1.5, length, length, 2)
        st.text_area(label = "Summary", value = response)


