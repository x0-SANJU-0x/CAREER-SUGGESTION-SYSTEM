
import requests
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv
import pickle
import numpy as np
import streamlit as st
import json
from streamlit_lottie import st_lottie

loaded_model=pickle.load(open("C://Users//sanch//OneDrive//Desktop//multipage//Career_trained_model.sav" ,'rb'))
loaded_models=pickle.load(open('C://Users//sanch//OneDrive//Desktop//multipage//Stream_trained_model.sav','rb'))

with st.sidebar:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    
    lottie_coding = load_lottiefile("C://Users//sanch//OneDrive//Desktop//multipage//lotts//career.json")
    
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
    
def careerpred(inputarr):
    nparr=np.asarray(inputarr)
    print(nparr)
    nparr=nparr.astype('float32')
    nparr=nparr.reshape(1,-1)
    pred=loaded_model.predict(nparr)
    return pred
def careerpreds(inputarr):
    nparr=np.asarray(inputarr)
    nparr=nparr.astype('float32')
    nparr=nparr.reshape(1,-1)
    pred=loaded_models.predict(nparr)
    return pred
st.title('EdXperts - AI Based Career Counselling')
with open("C://Users//sanch//OneDrive//Desktop//multipage//reply.txt", "r") as file:
    Hourswork = float(file.readline().strip())
    canworklong = 1 if file.readline().strip().lower()=='yes' else 0
    selflearning = 1 if file.readline().strip().lower()=='yes' else 0
    Extracourses = 1 if file.readline().strip().lower()=='yes' else 0
    talenttests = 1 if file.readline().strip().lower()=='yes' else 0
    olympiads = 1 if file.readline().strip().lower()=='yes' else 0
    temp1=file.readline().strip().lower()
    if temp1=='system developer':
        interestedcareer=4
    elif temp1=='business process analyst':
        interestedcareer=0
    elif temp1=='developer':
        interestedcareer=2
    if temp1=='testing':
        interestedcareer=5
    elif temp1=='security':
        interestedcareer=3
    elif temp1=='cloud computing':
        interestedcareer=1
    else:
        interestedcareer=2

    HigherStudies = 1 if file.readline().strip().lower()=='higher studies' or file.readline().strip().lower()=='higherstudies' else 0
    Takeninputsfromseniors = 1 if file.readline().strip().lower()=='yes' else 0
    interestedingames = 1 if file.readline().strip().lower()=='yes' else 0
    temp=file.readline().strip().lower()
   
    if temp=='prayer books':
        booktype=21
    elif temp=='childrens':
        booktype=5
    elif temp=='travel':
        booktype=29
    elif temp=='romance':
        booktype=23
    elif temp=='cookbooks':
        booktype=7
    elif temp=='self help':
        booktype=27
    elif temp=='drama':
        booktype=10
    elif temp=='math':
        booktype=18
    elif temp=='religion-spirtuality':
        booktype=22
    elif temp=='anthology':
        booktype=1
    elif temp=='trilogy':
        booktype=30
    elif temp=='autobiographies':
        booktype=3
    elif temp=='mystery':
        booktype=19
    elif temp=='diaries':
        booktype=8
    elif temp=='journals':
        booktype=17
    elif temp=='history':
        booktype=15
    elif temp=='art':
        booktype=2
    elif temp=='dictionaries':
        booktype=9
    elif temp=='horror':
        booktype=16
    elif temp=='encyclopedias':
        booktype=11
    elif temp=='action' or temp=='adventure':
        booktype=0
    elif temp=='fantasy':
        booktype=12
    elif temp=='comics':
        booktype=6
    elif temp=='science fiction':
        booktype=26
    elif temp=='series':
        booktype=28
    elif temp=='guide':
        booktype=13
    elif temp=='biographies':
        booktype=4
    elif temp=='health':
        booktype=14
    elif temp=='satire':
        booktype=24
    elif temp=='science':
        booktype=25
    elif temp=='poetry':
        booktype=20
    else:
        booktype=2
    Tuff = 1 if file.readline().strip().lower()=='stubborn' else 0
    Management = 1 if file.readline().strip().lower()=='technical' else 0
    hardsmart = 1 if file.readline().strip().lower()=='smart worker' or file.readline().strip().lower()=='smartworker' else 0
    workedinteams = 1 if file.readline().strip().lower()=='yes' else 0
    Introvert = 1 if file.readline().strip().lower()=='yes' else 0
with open("C://Users//sanch//OneDrive//Desktop//multipage//result.txt", "r") as file1:
    Logicalqr = int(file1.readline().strip())
    publicspeak = int(file1.readline().strip())
    readingwritingskills = int(file1.readline().strip())
    memorycapabilityscore = int(file1.readline().strip())
    Communicationskills = int(file1.readline().strip())
    Marks=Communicationskills

if st.button('Predict my career'):
      res=careerpred([Marks,Communicationskills,Hourswork,Logicalqr,publicspeak,canworklong,selflearning,Extracourses,talenttests,olympiads,readingwritingskills,memorycapabilityscore,HigherStudies,Takeninputsfromseniors,interestedingames,Tuff,Management,hardsmart,workedinteams,Introvert,interestedcareer,booktype])
      stream=careerpreds([Marks,Communicationskills,Hourswork,Logicalqr,publicspeak,canworklong,selflearning,Extracourses,talenttests,olympiads,readingwritingskills,memorycapabilityscore,HigherStudies,Takeninputsfromseniors,interestedingames,Tuff,Management,hardsmart,workedinteams,Introvert,interestedcareer,booktype])
      import csv
      row=[Marks,Communicationskills,Hourswork,Logicalqr,publicspeak,canworklong,selflearning,Extracourses,talenttests,olympiads,readingwritingskills,memorycapabilityscore,HigherStudies,Takeninputsfromseniors,interestedingames,Tuff,Management,hardsmart,workedinteams,Introvert,res[0],temp1,temp]
      with open("C://Users//sanch//OneDrive//Desktop//multipage//roo_data.csv",'a') as file:
      	writer = csv.writer(file)
      	writer.writerow(row)
      st.success("Your Suitable Career is "+res[0])
      st.success("Your Suitable Stream is "+stream[0])

      career=res[0]
      user_input='Tell me about '+career+' and provide some detailed career insights of it ?'
    # Generate empty lists for generated and user.
    ## Assistant Response
      if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hi Student!!!\nHope you found your career"]

    ## user question
      if 'user' not in st.session_state:
        st.session_state['user'] = ['Hello']
    

    # Layout of input/response containers
      response_container = st.container()
      colored_header(label='', description='', color_name='red-30')
      input_container = st.container()

    #input_container = st.container()

    # get user input
      def get_text():
        input_text = st.text_input("You: ", "", key="input")
        return input_text
      with input_container:
          user_input='Tell me about '+career+' and provide some detailed career insights of it ?'
    ## Applying the user input box
    #with input_container:
    #   user_input = get_text()

      def chain_setup():


        template = """<|prompter|>{question}<|endoftext|>
        <|assistant|>"""
        
        prompt = PromptTemplate(template=template, input_variables=["question"])

        llm=HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens":1200})

        llm_chain=LLMChain(
            llm=llm,
            prompt=prompt
        )
        return llm_chain


    # generate response
      def generate_response(question, llm_chain):
        response = llm_chain.run(question)
        return response

    ## load LLM
      llm_chain = chain_setup()

    # main loop
      with response_container:
        if user_input:
            response = generate_response(user_input, llm_chain)
            st.session_state.user.append(user_input)
            st.session_state.generated.append(response)
            st.title(''
            +career+
            ':') 
            st.markdown(''
            +response+
            '') 

    

