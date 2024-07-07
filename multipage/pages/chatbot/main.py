import pickle

import numpy as np

import streamlit as st

loaded_model=pickle.load(open('C:/Users/Vijesh Pethuram K/JupyFiles/trained_model.sav','rb'))


def careerpred(inputarr):

    nparr=np.asarray(inputarr)

    nparrrs=nparr.reshape(1,-1)

    pred=loaded_model.predict(nparrrs)

    return pred

 

 

def main():

    ssscore=0

    st.title('EdExpert - AI Based Career Prediction')

    st.header('Questions on :blue[SOCIAL SCIENCE] :')

    ans=""

    ans1 = "india"

    ans2="china"

    ans3="russia"

    choices = [ans,ans1,ans2,ans3]

    st.subheader(':green[What is 7 th country in world]:')

    st.divider()

    a = st.selectbox('Answer:', choices)

    st.write(f"You chose {a}")

    if ans1==a:

        st.success('Correct!')

        ssscore+=1

    elif ans==a:

        st.write('')

    else:

        st.warning(f'Incorrect! The correct answer is {ans1}')

       

    ans=""

    ans1 = "Rome"

    ans2="Athens"

    ans3="Egypt"

    choices = [ans,ans1,ans2,ans3]

    st.subheader(':green[Which of the following is considered the birthplace of democracy]:')

    st.divider()

    a = st.selectbox('Answer:', choices)

    st.write(f"You chose {a}")

    if ans2==a:

        st.success('Correct!')

        ssscore+=1

    elif ans==a:

        st.write('')

    else:

        st.warning(f'Incorrect! The correct answer is {ans1}')     

    st.write(f'Your Score: {ssscore}/2')

       

    

    Programming=st.number_input('Programming Subject Marks: ')

    Science=st.number_input('Science Subject Marks: ')

    SocialScience=st.number_input('Social Subject Marks: ')

    ComputerScience=st.number_input('Computer Subject Marks: ')

    Mathematics=st.number_input('Maths Subject Marks: ')

    Communicationskills =st.number_input('Communication Skills Marks: ')

    Hourswork =st.number_input('Hours he/she can work: ')

    Logicalqr =st.number_input('Logical quotient: ')

    publicspeak =st.number_input('Public Speaking skillpoints: ')

    canworklong =st.number_input('Can work long time before system?: ')

    selflearning =st.number_input('SelfLearning capability?: ')

    Extracourses =st.number_input('Extra courses did?: ')

    talenttests =st.number_input('Talent tests taken?: ')

    olympiads =st.number_input('Olympiads taken?: ')

    readingwritingskills =st.number_input('Reading and writing skills: ')

    memorycapabilityscore =st.number_input('Memory capability score: ')

    HigherStudies =st.number_input('Interested in higher studies: ')

    Takeninputsfromseniors =st.number_input('Taken input from seniors?: ')

    interestedingames =st.number_input('Interested in games?: ')

    relationship =st.number_input('In a relationship?: ')

    Tuff =st.number_input('Tuff personality?: ')

    Management =st.number_input('Management or Technical: ')

    hardsmart =st.number_input('Hard or smart worker?: ')

    workedinteams =st.number_input('Has Worked in teams?: ')

    Introvert =st.number_input('Is an Introvert: ')

   

    res=''

    if st.button('Check my career'):

        res=careerpred([Programming,Science,SocialScience,ComputerScience,Mathematics,Communicationskills,Hourswork,Logicalqr,publicspeak,canworklong,selflearning,Extracourses,talenttests,olympiads,readingwritingskills,memorycapabilityscore,HigherStudies,Takeninputsfromseniors,interestedingames,relationship,Tuff,Management,hardsmart,workedinteams,Introvert])

       

    st.success(res)

   

if __name__ == '__main__':

    main()

 