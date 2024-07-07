import streamlit as st
import json
from streamlit_lottie import st_lottie
# Create a dictionary to store user information (for demonstration purposes)
import mysql.connector

db=mysql.connector.connect(host='localhost',passwd='root',user='root',port=3306,database='edxpert')
if db.is_connected():
    print("DB Connection success :)")
else:
    st.warning("DB error! Broken MySQL Pipeline :( ")
cursor=db.cursor()
# Create a Streamlit app


# Create a sidebar for navigation
menu = st.sidebar.radio("Menu", ["Sign Up", "Sign In"])

with st.sidebar:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    
    lottie_coding = load_lottiefile("C://Users//sanch//OneDrive//Desktop//multipage//lotts//code.json")
    
    st_lottie(
    lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=300,
        width=300,
        key=None,
    )

if menu == "Sign In":
    st.subheader("Sign In🔒")
    email=st.text_input('Email:')
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        cursor=db.cursor()
        cursor.execute('select * from userinfo where email like %s AND password like %s',(email,password))
        res=cursor.fetchone()
        print(res)
        if(res!=None):
            st.success("Signed In!")
        else:
            st.warning("Invalid Credentials!")

elif menu == "Sign Up":
    st.subheader("Sign Up🔐")
    email=st.text_input('Email:')
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    fname=st.text_input('Name:')

# creating radio button 
    gender=st.radio('Gender',('Male','Female'))

# creating date picker
    bday=st.date_input('Enter Birthdate:')
# creating a text area
    l= st.text_input('% in SSLC:')
    address=st.text_area('Enter Address:')

    if new_password != confirm_password:
        st.warning("Passwords do not match.")
    elif st.button("Sign Up"):
        cursor.execute('insert into userinfo values(%s,%s,%s,%s,%s,%s,%s,%s)',(email,fname,new_password,gender,bday,l,address,'unpredicted'))
        db.commit()
        st.success("Signed Up!")
# Add a footer to your Streamlit app
st.sidebar.markdown("---")
#st.sidebar.markdown("---")

# Run the app
if __name__ == "__main__":
    st.sidebar.text("")
    st.sidebar.text("")