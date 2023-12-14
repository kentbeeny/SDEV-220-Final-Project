#Team H final project
#we are using streamlit

#Tutorial/sources used:
#https://www.youtube.com/watch?v=sogNluduBQQ
#https://www.youtube.com/watch?v=Loxhpjho5h4

#will need to run "pip install pymongo" in command line
#may need to install Streamlit before running using "pip install streamlit" command
#to run app, navigate to the directory containing the app and run "streamlit run app.py"

import streamlit as st
import pageviews as view
import NewClasses as classes
from NewClasses import Kids

st.title("Toys for Tots!")
st.text("Here you can make donations to ensure children have Merry Christmases!")
st.sidebar.title('Nav')
options = st.sidebar.radio('Pages', options=['Home',
                                             'Make Donation', 
                                             'Request Donation', 
                                             'See Requested Donations'])


if options == 'Home':
    view.home()
elif options == 'Make Donation':
    view.donations()
elif options == 'Request Donation':
    view.makeReq()
elif options == 'See Requested Donations':
    classes.seeReq(Kids.parentName, Kids.name, Kids.age, Kids.toy)
