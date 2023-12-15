import streamlit as st
from getDb import get_database #importing database connection function

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#These functions will set the views for each of the options selectable from the sidebar
# in the main program.

dbname=get_database()

def home():
    st.header("Making Christmas More Merry Since 1947!")
    st.image('toysfortots3.jpg') # place the toysfortots logo on the page
    #Can probably add more to this page

def db_submit_donation(donor_name, monetary_donation, toy_donation): #code for sending donation info to db
    collection_name = dbname["Donated"]
    collection_name.insert_one({
        "donor_name": donor_name,
        "money_donated": monetary_donation,
        "toys_donated": toy_donation
    })

def donations():
    st.image('toysfortots3.jpg') # place the toysfortots logo on the page
    st.header("Make a Donation!")
    donor_name = st.text_input("Enter your Full Name OR your organization's name")
    monetary_donation = st.text_input("Monetary Donation amount:")
    toy_donation = st.text_input("Toy being donated:")
    
    #Will probably remove this option, unless we have time to implement it at the end
    ###radioOptions = st.radio("Would you like a receipt?", options = ["No", "Yes"])
    ####if they select that they would like a reciept then get their name to put on it
    ###if radioOptions == "Yes":
    ###     code to create a receipt will go here

    if st.button("Submit Donation"):
        db_submit_donation(donor_name, monetary_donation, toy_donation)
        st.session_state.submitted = True
        st.success("Donation submitted! Thank you for your generosity!")

def db_submit_request(parent_name, child_name, child_age, toy_requested): #code for sending request info to db
    collection_name = dbname["Requested"]
    collection_name.insert_one({
        "parent_name": parent_name,
        "child_name": child_name,
        "child_age": child_age,
        "toy_requested": toy_requested
    })
    st.session_state.submitted = True


def makeReq():
    st.image('toysfortots3.jpg') # place the toysfortots logo on the page
    st.header("Request a Donation!")

    parent_name = st.text_input("What is your first and last name?")
    child_name = st.text_input("What is the child's first and last name?")
    child_age = st.text_input("How old is the child?")
    toy_requested = st.text_input("What toy are you requesting?")
    
    if st.button("Submit Donation Request"):
        db_submit_request(parent_name, child_name, child_age, toy_requested)
        st.session_state.submitted = True
        st.success("Request submitted!")
        # ref https://docs.streamlit.io/library/api-reference/widgets/st.button


@st.cache_data(ttl=1) # Annotation to refresh the data every 5 minutes
def seeReq():
    st.image('toysfortots3.jpg') # place the toysfortots logo on the page
    st.header("See What's Been Requested!")
    collection_name = dbname["Requested"]
    reqList = list(collection_name.find())
    for item in reqList:
        st.write(item["toy_requested"])
# ref https://docs.streamlit.io/library/api-reference/widgets/st.selectbox



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#The Classes and their attributes:
#Kids#
# -name
# -age
# -toy

#Sponsors#
# -name
# -money
# -toy

#Requestor#
# -Name

#The tables in the database
#Requested#
# -parent's name (from "Requestor" class)
# -kids name (from "Kids" class)
# -kids age (from "Kids" class)
# -toy requested (from "Kids" class)

#Donated#
# -donator's name (from "Sponsors" class)
# -money donated (from "sponsors" class) - can be null
# -toy being donated (from "sponsors" class) - can be null 
