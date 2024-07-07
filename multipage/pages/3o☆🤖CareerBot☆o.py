import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv

# load the Environment Variables.
load_dotenv()
st.set_page_config(page_title="OpenAssistant Powered Chat App")

# Sidebar contents
with st.sidebar:
    st.title('📚🤖CAREERBOT')
    st.markdown('''
    ## About
            WELCOME TO THE CAREERBOT
            
    - THIS INTERACTIVE BOT HELPS TO CHOOSE YOUR CAREER
    - HAVE A FREE CONVERSATION WITH THE CAREERBOT
    - HELPS YOU TO GAIN MORE INFORMATION ON NEW CAREERS

    ''')
    add_vertical_space(3)
    st.write('Made with ❤️ by EdXperts')

st.header("Your Personal CareerBot 💬")
with st.sidebar:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    
    lottie_coding = load_lottiefile("C://Users//sanch//OneDrive//Desktop//multipage//lotts//robo.json")
    
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


with open("C://Users//sanch//OneDrive//Desktop//multipage//result.txt", "r") as file1:
    Logicalqr = int(file1.readline().strip())
if Logicalqr>=0 and Logicalqr <3: 
    input_file = open("C://Users//sanch//OneDrive//Desktop//multipage//Questions.txt", "r")
if Logicalqr>=3 and Logicalqr <5: 
    input_file = open("C://Users//sanch//OneDrive//Desktop//multipage//Question1.txt", "r")
if Logicalqr>=5 and Logicalqr <8: 
    input_file = open("C://Users//sanch//OneDrive//Desktop//multipage//Question2.txt", "r")
if Logicalqr>=8 and Logicalqr <=10: 
    input_file = open("C://Users//sanch//OneDrive//Desktop//multipage//Question3.txt", "r")

def main():
    global flag
    # Generate empty lists for generated and user.
    # Assistant Response
    
    if 'generated' not in st.session_state:
        st.session_state['generated'] = [
            "HEY!!! , I'm CareerBot! \n If you could design your ideal future career, how many hours per day would you like to work(1 -24)?"]
        output_file = open("C://Users//sanch//OneDrive//Desktop//multipage//nn.txt", "w")
        file_pat="C://Users//sanch//OneDrive//Desktop//multipage//reply.txt"
        with open(file_pat, "w") as file:
            pass 
        for line in input_file:
          output_file.write(line)

        input_file.close()
        output_file.close()

    # user question
    if 'user' not in st.session_state:
        st.session_state['user'] = ['Hi!']

    # Layout of input/response containers
    response_container = st.container()
    colored_header(label='', description='', color_name='red-30')
    input_container = st.container()

    # get user input
    def get_text():
        input_text = st.text_input("You: ", "", key="input")
        return input_text

    # Applying the user input box
    with input_container:
        user_input = get_text()

    def chain_setup():

        template = """<|prompter|>{question}<|endoftext|>
        <|assistant|>"""

        prompt = PromptTemplate(
            template=template, input_variables=["question"])

        llm = HuggingFaceHub(
            repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens": 1200})

        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt
        )
        return llm_chain

    
    file_path = "C://Users//sanch//OneDrive//Desktop//multipage//nn.txt"
    # generate response
    def generate_response(question, llm_chain):
        response = llm_chain.run(question)
        one_line=""
        if(response=="Hello! How can I help you today?" or response=="I'm sorry, I don't understand what you mean by \"gentle\". Could you please rephrase your question or provide more context?"or 
           response=="Hello! How can I help you?" or 
           response=="I am a language model trained by LAION-AI. I can answer questions, generate text, and perform other tasks." or 
           response=="I'm sorry, I don't understand what you mean by \"horror\". Could you please rephrase your question or provide more context?"
           ):
                response=" "
        
        file_path = "C://Users//sanch//OneDrive//Desktop//multipage//nn.txt"
        with open(file_path, 'r') as file:
          one_line = file.readline()
          lines = file.readlines()
        if lines:
            first_line = lines[0]
            lines = lines[1:]
            lines.append(first_line)
            with open(file_path, 'w') as file:
                file.writelines(lines)

            return response+"\n"+one_line

    # load LLM
    llm_chain = chain_setup()

    # main loop
    with response_container:
        if user_input:
            with open("C://Users//sanch//OneDrive//Desktop//multipage//reply.txt", "a") as file:
                file.writelines(user_input)
                file.writelines("\n")
                file.close()
            response = generate_response(user_input, llm_chain)
            st.session_state.user.append(user_input)
            st.session_state.generated.append(response)
            

        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['user'][i],
                        is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))
    
    

if __name__ == '__main__':
  main()
  
