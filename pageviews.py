import streamlit as st
from getDb import get_database #importing database connection function

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#These functions will set the views for each of the options selectable from the sidebar
# in the main program.

dbname=get_database()

def home():
    st.header("Making Christmas More Merry Since 1947!")
    #Can probably add more to this page

# def db_submit_donation(): #code for sending donation info to db
    



def donations():
    st.header("Make a Donation!")
    st.text_input("Enter your Full Name OR your organization's name")
    st.text_input("Monetary Donation amount:")
    st.text_input("Toy being donated:")

    #Will probably remove this option, unless we have time to implement it at the end
    ###radioOptions = st.radio("Would you like a receipt?", options = ["No", "Yes"])
    ####if they select that they would like a reciept then get their name to put on it
    ###if radioOptions == "Yes":
    ###     code to create a receipt will go here


    st.button("Submit Donation", on_click= None)
    #the "on_click" will be the code to create an instance of the Sponsors Class
    # and send it's attributes to the DB, 
    #create function and call in the on_Click

def db_submit_request(parent_name, child_name, toy_requested, child_age): #code for sending request info to db
    collection_name = dbname["Requested"]
    collection_name.insert_many([{
        "parent_name": parent_name,
        "child_name": child_name,
        "child_age": child_age,
        "toy_requested": toy_requested
    }])

def makeReq():
    st.header("Request a Donation!")
    parent_name = st.text_input("What is your first and last name?")
    child_name = st.text_input("What is the child's first and last name?")
    child_age = st.text_input("How old is the child?")
    toy_requested = st.text_input("What toy are you requesting?")
    st.button("Submit Donation Request", on_click= db_submit_request(parent_name, child_name, child_age, toy_requested)) 
        #the "on_click" will be the code to send to DB, 
        #create function and call here
        #need to add code to button to have it send the entered info to the MongoDB database
        # ref https://docs.streamlit.io/library/api-reference/widgets/st.button

@st.cache_data(ttl=600)
def seeReq():
    st.header("Requested Toys:")
    items = dbname.Requested.find()
    items == list(items)
    # return items
    for item in items:
        st.write(f"{item}")
    #Insert code to display all the toys requested and the ages of the kids requesting them
    #Maybe use selectbox?
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
