#Team H final project
#we are using streamlit

#Tutorial/sources used:
#https://www.youtube.com/watch?v=sogNluduBQQ
#https://www.youtube.com/watch?v=Loxhpjho5h4

#to run app, navigate to the directory containing the app and run "streamlit run app.py"
#may need to install Streamlit before running using "pip install streamlit" command
import streamlit as st
import pageviews as view

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
    view.seeReq()
