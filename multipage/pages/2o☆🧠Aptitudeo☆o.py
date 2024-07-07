import streamlit as st
import random  
import pickle

# Define a list of 10 questions and their corresponding options and correct answers


logical_questions = [
    
        
        {
            "category": "Logical",
            "question": "If all Zips are Zaps, and some Zaps are Zops, can we conclude that some Zips are definitely Zops?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If John is twice as old as Alice, and Alice is 10 years old, how old is John?",
            "options": ["A) 5 years", "B) 10 years", "C) 20 years", "D) 30 years"],
            "correct_answer": "C) 20 years"
        },
        {
            "category": "Logical",
            "question": "If all cats have tails, and Fluffy is a cat, can we conclude that Fluffy has a tail?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If the train departs at 2:30 PM and arrives at 4:45 PM, how long is the train journey?",
            "options": ["A) 1 hour 45 minutes", "B) 2 hours", "C) 2 hours 15 minutes", "D) 3 hours 15 minutes"],
            "correct_answer": "A) 1 hour 45 minutes"
        },
        {
            "category": "Logical",
            "question": "If A implies B, and B implies C, can we conclude that A implies C?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all squares are rectangles, and some rectangles are not circles, can we conclude that some squares are not circles?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If today is Monday, and two days from now will be a Wednesday, what day was it yesterday?",
            "options": ["A) Saturday", "B) Sunday", "C) Monday", "D) Tuesday"],
            "correct_answer": "B) Sunday"
        },
        {
            "category": "Logical",
            "question": "If all birds can fly, and penguins cannot fly, can we conclude that penguins are not birds?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "B) No"
        },
        {
            "category": "Logical",
            "question": "If 3 people can paint 3 rooms in 3 hours, how many people are needed to paint 6 rooms in 6 hours?",
            "options": ["A) 3 people", "B) 6 people", "C) 9 people", "D) 12 people"],
            "correct_answer": "A) 3 people"
        },
        {
        "category": "Logical",
        "question": "In a town, there are two barbers. One barber has a neatly trimmed beard, while the other barber is clean-shaven. Each day, every man in the town must visit one of the barbers to get a haircut. The rule is that if a man arrives at a barber's shop and the barber has a neatly trimmed beard, he must leave and go to the clean-shaven barber. If the barber is clean-shaven, he must leave and go to the barber with a neatly trimmed beard. Given this scenario, can such a situation exist in the town?",
        "options": ["A) Yes", "B) No"],
        "correct_answer": "B) No"
        },

        {
            "category": "Logical",
            "question": "If all roses are flowers, and some flowers are red, can we conclude that some roses are red?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If Peter is taller than Mary, and Mary is taller than Sarah, who is the shortest among them?",
            "options": ["A) Peter", "B) Mary", "C) Sarah"],
            "correct_answer": "C) Sarah"
        },
        {
            "category": "Logical",
            "question": "If no mammals can fly, and bats are mammals, can we conclude that bats cannot fly?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "B) No"
        },
        {
            "category": "Logical",
            "question": "If the train travels at a speed of 60 mph and covers a distance of 120 miles, how long does the journey take?",
            "options": ["A) 1 hour", "B) 2 hours", "C) 3 hours", "D) 4 hours"],
            "correct_answer": "B) 2 hours"
        },
        {
            "category": "Logical",
            "question": "If all squares have four sides, and this shape has four sides, can we conclude that it is a square?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "B) No"
        },
        {
            "category": "Logical",
            "question": "If Jack is older than Jill, and Jill is older than Tom, who is the youngest among them?",
            "options": ["A) Jack", "B) Jill", "C) Tom"],
            "correct_answer": "C) Tom"
        },
        {
            "category": "Logical",
            "question": "If 5 books cost $25, how much do 8 books cost?",
            "options": ["A) $40", "B) $45", "C) $50", "D) $55"],
            "correct_answer": "A) $40"
        },
        {
            "category": "Logical",
            "question": "If no reptiles can swim, and turtles are reptiles, can we conclude that turtles cannot swim?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If it is rainy and John has an umbrella, will John use the umbrella?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all fruits are healthy, and some fruits are delicious, can we conclude that some healthy things are delicious?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },

        {
            "category": "Logical",
            "question": "If all birds can fly, and penguins are birds, can we conclude that penguins can fly?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "B) No"
        },
        {
            "category": "Logical",
            "question": "If every student in the class passed the math exam, and John is a student, can we conclude that John passed the math exam?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all triangles have three sides, and this shape has three sides, can we conclude that it is a triangle?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If it is snowing, and Mary has a snowball, can we conclude that Mary made the snowball?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If every apple is a fruit, and some fruits are red, can we conclude that some apples are red?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all dogs have tails, and Fido is a dog, can we conclude that Fido has a tail?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If it is daytime and the sun is shining, can we conclude that it is not nighttime?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If no insects have fur, and bees are insects, can we conclude that bees do not have fur?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If it is raining and Mary has an umbrella, can we conclude that Mary will use the umbrella?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        },
        {
            "category": "Logical",
            "question": "If all planets orbit the sun, and Earth is a planet, can we conclude that Earth orbits the sun?",
            "options": ["A) Yes", "B) No"],
            "correct_answer": "A) Yes"
        }





        # Add more questions here...
    
    # Add more questions here...
]
verbal_questions = [
    {
     "category": "Verbal",
     "question": "What is the synonym of 'Ubiquitous'?",
     "options": ["A) Rare", "B) Pervasive", "C) Limited", "D) Scarce"],
     "correct_answer": "B) Pervasive"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Innocuous'?",
     "options": ["A) Harmless", "B) Dangerous", "C) Safe", "D) Mild"],
     "correct_answer": "B) Dangerous"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'a brief and decisive statement or expression'?",
     "options": ["A) Elusive", "B) Facetious", "C) Ephemeral", "D) Epigram"],
     "correct_answer": "D) Epigram"
 },
 {
     "category": "Verbal",
     "question": "What is the synonym of 'Voracious'?",
     "options": ["A) Hungry", "B) Satisfied", "C) Ravenous", "D) Starving"],
     "correct_answer": "C) Ravenous"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Ubiquitous'?",
     "options": ["A) Rare", "B) Pervasive", "C) Limited", "D) Scarce"],
     "correct_answer": "A) Rare"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'lasting for a very short time'?",
     "options": ["A) Eternal", "B) Fleeting", "C) Permanent", "D) Lasting"],
     "correct_answer": "B) Fleeting"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Innocuous'?",
     "options": ["A) Harmless", "B) Dangerous", "C) Safe", "D) Mild"],
     "correct_answer": "B) Dangerous"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'lack of interest, enthusiasm, or concern'?",
     "options": ["A) Apathy", "B) Enthusiasm", "C) Detachment", "D) Passivity"],
     "correct_answer": "A) Apathy"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Serene'?",
     "options": ["A) Calm", "B) Peaceful", "C) Turbulent", "D) Tranquil"],
     "correct_answer": "C) Turbulent"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'a state of being pleasantly lost in one's thoughts; a daydream'?",
     "options": ["A) Reverie", "B) Nightmare", "C) Reality", "D) Fantasy"],
     "correct_answer": "A) Reverie"
 },
    {
       "category": "Verbal",
       "question": "What is the synonym of 'Ephemeral'?",
       "options": ["A) Lasting", "B) Fleeting", "C) Permanent", "D) Eternal"],
       "correct_answer": "B) Fleeting"
   },
   {
       "category": "Verbal",
       "question": "What is the antonym of 'Obfuscate'?",
       "options": ["A) Clarify", "B) Confuse", "C) Complicate", "D) Mystify"],
       "correct_answer": "A) Clarify"
   },
   {
       "category": "Verbal",
       "question": "Which word means 'a person who is new to a subject or activity'?",
       "options": ["A) Expert", "B) Veteran", "C) Novice", "D) Master"],
       "correct_answer": "C) Novice"
   },
   {
       "category": "Verbal",
       "question": "What is the synonym of 'Eloquent'?",
       "options": ["A) Fluent", "B) Inarticulate", "C) Charming", "D) Brief"],
       "correct_answer": "A) Fluent"
   },
   {
       "category": "Verbal",
       "question": "What is the antonym of 'Voracious'?",
       "options": ["A) Hungry", "B) Satisfied", "C) Ravenous", "D) Starving"],
       "correct_answer": "B) Satisfied"
   },
   {
       "category": "Verbal",
       "question": "Which word means 'intentionally exaggerated to emphasize a point or create humor'?",
       "options": ["A) Literal", "B) Hyperbolic", "C) Understated", "D) Accurate"],
       "correct_answer": "B) Hyperbolic"
   },
   {
       "category": "Verbal",
       "question": "What is the antonym of 'Precarious'?",
       "options": ["A) Stable", "B) Dangerous", "C) Secure", "D) Unsteady"],
       "correct_answer": "A) Stable"
   },
   {
       "category": "Verbal",
       "question": "Which word means 'a person who loves or is strongly attracted to something'?",
       "options": ["A) Apathetic", "B) Repellent", "C) Enthusiast", "D) Skeptic"],
       "correct_answer": "C) Enthusiast"
   },
   {
       "category": "Verbal",
       "question": "What is the synonym of 'Serene'?",
       "options": ["A) Calm", "B) Peaceful", "C) Turbulent", "D) Tranquil"],
       "correct_answer": "D) Tranquil"
   },
   {
       "category": "Verbal",
       "question": "What is the antonym of 'Eloquent'?",
       "options": ["A) Fluent", "B) Inarticulate", "C) Charming", "D) Brief"],
       "correct_answer": "B) Inarticulate"
   },
    {
     "category": "Verbal",
     "question": "What is the synonym of 'Ephemeral'?",
     "options": ["A) Lasting", "B) Fleeting", "C) Permanent", "D) Eternal"],
     "correct_answer": "B) Fleeting"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Obfuscate'?",
     "options": ["A) Clarify", "B) Confuse", "C) Complicate", "D) Mystify"],
     "correct_answer": "A) Clarify"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'a person who is new to a subject or activity'?",
     "options": ["A) Expert", "B) Veteran", "C) Novice", "D) Master"],
     "correct_answer": "C) Novice"
 },
 {
     "category": "Verbal",
     "question": "What is the synonym of 'Eloquent'?",
     "options": ["A) Fluent", "B) Inarticulate", "C) Charming", "D) Brief"],
     "correct_answer": "A) Fluent"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Voracious'?",
     "options": ["A) Hungry", "B) Satisfied", "C) Ravenous", "D) Starving"],
     "correct_answer": "B) Satisfied"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'intentionally exaggerated to emphasize a point or create humor'?",
     "options": ["A) Literal", "B) Hyperbolic", "C) Understated", "D) Accurate"],
     "correct_answer": "B) Hyperbolic"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Precarious'?",
     "options": ["A) Stable", "B) Dangerous", "C) Secure", "D) Unsteady"],
     "correct_answer": "A) Stable"
 },
 {
     "category": "Verbal",
     "question": "Which word means 'a person who loves or is strongly attracted to something'?",
     "options": ["A) Apathetic", "B) Repellent", "C) Enthusiast", "D) Skeptic"],
     "correct_answer": "C) Enthusiast"
 },
 {
     "category": "Verbal",
     "question": "What is the synonym of 'Serene'?",
     "options": ["A) Calm", "B) Peaceful", "C) Turbulent", "D) Tranquil"],
     "correct_answer": "D) Tranquil"
 },
 {
     "category": "Verbal",
     "question": "What is the antonym of 'Eloquent'?",
     "options": ["A) Fluent", "B) Inarticulate", "C) Charming", "D) Brief"],
     "correct_answer": "B) Inarticulate"
 }
    # Add more verbal questions here...
]
comprehensive_questions=[{
     "category": "Compre",
     "question": " Why did Mike and his family decide to rest under the thief’s tree? ",
     "options": ["A) Being a large family, they knew that they could easily defeat the thief ", "B) It was a convenient spot for taking a halt at night", "C)  There was a stream nearby and wood enough to build a house","D) That was the only large tree that could shelter their large family"],
     "correct_answer": " B) It was a convenient spot for taking a halt at night"
 },
    {
         "category": "Compre",
         "question": " Which of the following best describes Morris?  ",
         "options": ["A) He was a rich businessman  ", "B) He bullied his wife ", "C) He paid his servants well ","D) He was greedy and imitated Mike"],
         "correct_answer": " D)He was greedy and imitated Mike"
     },
    {
         "category": "Compre",
         "question": " What did Mike mean when he said “He is watching all this from above”?",
         "options": ["A)He had spotted the thief and wanted to scare him  ", "B) He was telling his wife to have faith in god ", "C)It was just a warning for his family members to stick together","D) He was begging the thief to help his famil"],
         "correct_answer": " B) It was a convenient spot for taking a halt at night"
     },
        

    {
        "category": "Compre",
        "question": " Why did the thief return to the tree?   ",
        "options": ["A)To wait for Mike to return   ", "B) To set up a trap ", "C) To wait for Morris’s family ","D)Not mentioned in the passage"],
        "correct_answer": " D) Not mentioned in the passage "
    },
    {
         "category": "Compre",
         "question": " How did the fellow villagers react to Mike getting rich overnight?   ",
         "options": ["A)They were jealous of him  ", "B)They were very excited ", "C)They followed his example ","D)They envied him "],
         "correct_answer": " B) They were very excited "
     },
    ]
read = [
    
        
        {
            "category": "Compre",
            "question": "What was the result of Napoleonic wars?",
            "options": ["A) A small part of the continent was occupied by French people", "B) Spain was occupied by the French", 
                        "C) War of independence was unable to yield any positive result", "D) American colonies were destroyed after the war"],
            "correct_answer": "B) Spain was occupied by the French"
        },
        {
            "category": "Compre",
            "question": "What is the meaning of the term ‘culminated’?",
            "options": ["A) Follow a particular path", "B) Guide or transform", "C) Reach the highest point", "D) Introduce on a grand scale"],
            "correct_answer": "B) Guide or transform"
        },
        {
            "category": "Compre",
            "question": "What is the summary of the passage??",
            "options": ["A) The rise and fall of a national empire", "B) The downfall of successive regimes in Spain", "C) The history of Spain", "D) Spain in eighteenth century"],
            "correct_answer": "C) The history of Spain"
        },
        {
            "category": "Compre",
            "question": "What occurred in the latter part of 17th century?",
            "options": ["A) War of succession confirmed the leading position of Spain", "B) Spain was no longer regarded as the ruling colonial power", "C) A vast empire was established in Europe", "D) Power steadily declined under Habsburg regime"],
            "correct_answer": "D) Power steadily declined under Habsburg regime"
        },
        {
            "category": "Compre",
            "question": "What would be the title of the above Passage?",
            "options": ["A) The Rise and Fall of the Spanish Empire", "B) Spain: A Travel Guide", "C) The Food of Spain", "D) Spanish Literature"],
            "correct_answer": "A) The Rise and Fall of the Spanish Empire"
        }

        # Add more questions here...
    
    # Add more questions here...
]
mc= [
    {
     "category": "Mc",
     "question": "What has a neck but no head, a back but no spine, and four legs but cannot walk?",
     "options": ["A) A shirt", "B)  A chair", "C) A tree", "D) A bird"],
     "correct_answer": "A) A shirt"
 },
 {
     "category": "Mc",
     "question": "I have no voice, but I can make you laugh. I have no hands, but I can build a castle. What am I??",
     "options": ["A) A dream", "B) A ghost", "C) A robot", "D) Imagination"],
     "correct_answer": "D) Imagination"
 },
 {
     "category": "Mc",
     "question": " What is full of holes but still holds water?",
     "options": ["A) A net", "B) A colander", "C) A sponge", "D) A sieve"],
     "correct_answer": "C) A sponge"
 },
 {
     "category": "Mc",
     "question": "What has a tongue but cannot speak?",
     "options": ["A) A shoe", "B) A belt", "C) A snake", "D) A fish"],
     "correct_answer": "A) A shoe"
 },
 {
     "category": "Mc",
     "question": "What has an eye but cannot see?",
     "options": ["A) A button", "B) A needle", "C) A lock", "D)  A mirror"],
     "correct_answer": "B) A needle"
 },
 {
     "category": "Mc",
     "question": "What has a bed but never sleeps?",
     "options": ["A) A river", "B)  A road", "C) A cloud", "D) A mountain"],
     "correct_answer": "A) A river"
 }
    # Add more verbal questions here...
]
gr = [
    {
     "category": "Grammar",
     "question": "Our country is spiritual country, theirs . . . . . . religious.",
     "options": ["A) is", "B)  are", "C)  also", "D) have"],
     "correct_answer": "A) is"
 },
 {
     "category": "Grammar",
     "question": "Which of the following sentences has an error?",
     "options": ["A) The cat sat on the mat.", "B) The dog barked at the mailman.", "C) The bird flew in the sky.", "D) I seen the movie yesterday."],
     "correct_answer": "D) I seen the movie yesterday."
 },
 {
     "category": "Grammar",
     "question": " What is the error in the sentence 'I seen the movie yesterday'?",
     "options": ["A) The subject and verb do not agree.", "B)The past tense of the verb 'see' is 'saw', not 'seen'. ", "C) The word 'seen' is used instead of the word 'watched'.", "D) All of the above."],
     "correct_answer": "B)The past tense of the verb 'see' is 'saw', not 'seen'."
 },
 {
     "category": "Grammar",
     "question": "Which of the following sentences is correct??",
     "options": ["A)  I seen the movie yesterday.", "B) I saw the movie yesterday.", "C)  I am seen the movie yesterday.", "D) I have seen the movie yesterday."],
     "correct_answer": "D) I have seen the movie yesterday"
 },
 {
     "category": "Grammar",
     "question": "What is the error in the sentence 'The dog is laying on the mat'?",
     "options": ["A) The subject and verb do not agree.", "B) The verb 'laying' should be 'lying'", "C) The word 'on' is unnecessary.", "D)  All of the above."],
     "correct_answer": "B) The verb 'laying' should be 'lying'"
 }
 
    # Add more verbal questions here...
]
st.title("Aptitude🤔💭")
with open("C://Users//sanch//OneDrive//Desktop//multipage//logi.txt", 'r') as file:
    one_line = file.readline()
if(one_line=='0'):
    logical_question = logical_questions.copy()
    random.shuffle(logical_question)
    with open("C://Users//sanch//OneDrive//Desktop//multipage//randomized_logical_questions.pkl", "wb") as f:
        pickle.dump(logical_question, f)
    with open("C://Users//sanch//OneDrive//Desktop//multipage//randomized_logical_questions.pkl", "rb") as f:
        logical_question = pickle.load(f)
    with open("C://Users//sanch//OneDrive//Desktop//multipage//logi.txt", 'w') as file:
        file.write("1")
else:
        with open("C://Users//sanch//OneDrive//Desktop//multipage//randomized_logical_questions.pkl", "rb") as f:
            logical_question = pickle.load(f)



 
st.header('🧮QUESTIONS ON LOGICAL!!!')
    # Create a dictionary to store user responses for Logical quiz
user_responses1 = {}
st.title("Logical Quiz")
i=0  
    # Loop through 10 logical questions
for i in range(10):
    question_data = logical_question[i]
    st.subheader(f"Question {i + 1}:")
    st.write(question_data["question"])  
        # Display multiple choice options and store user's choice with a unique key
    user_response1 = st.radio(f"Select an option {i}:", question_data["options"], key=f"radio_logical_{i}")
    user_responses1[i] = user_response1
    st.markdown('~~~~~~~~~~~~~~~~~~~~~~') 

    # Check answers and display results for Logical quiz


st.markdown('--------------------')
st.header('🔠QUESTIONS ON VERBAL!!!')
    # Create a dictionary to store user responses for Verbal quiz
user_responses = {}
    
st.title("Verbal Quiz")
    
    # Loop through 10 verbal questions
for i in range(10):
    question_data = verbal_questions[i]
    st.subheader(f"Question {i + 1}:")
    st.write(question_data["question"])
        
        # Display multiple choice options and store user's choice with a unique key
    user_response = st.radio(f"Select an option {i}:", question_data["options"], key=f"radio_verbal_{i}")
    user_responses[i] = user_response
    
st.markdown('--------------------')
st.header('📝QUESTIONS ON COMPREHENSION!!!')
    # Create a dictionary to store user responses for Verbal quiz

st.title("Read the passage and answer the questions that follow :")
st.subheader("COMPREHENSION-1")
st.write("""
Mike and Morris lived in the same village. While Morris owned the largest jewelry
 shop in the village, Mike was a poor farmer. Both had large families with many sons,
          daughters-in-law and grandchildren. One fine day, Mike, tired of not being able 
         to feed his family, decided to leave the village and move to the city where he was
          certain to earn enough to feed everyone. Along with his family, he left the village 
         for the city. At night, they stopped under a large tree. There was a stream running 
         nearby where they could freshen up themselves. He told his sons to clear the area below
          the tree, he told his wife to fetch water and he instructed his daughters-in-law to make
          up the fire and started cutting wood from the tree himself. They didn’t know that in the
          branches of the tree, there was a thief hiding. He watched as Mike’s family worked together
          and also noticed that they had nothing to cook. Mike’s wife also thought the same and asked
          her husband ” Everything is ready but what shall we eat?”. Mike raised his hands to 
         heaven and said ” Don’t worry. He is watching all of this from above. He will help us.”
          The thief got worried as he had seen that the family was large and worked well together.
          Taking advantage of the fact that they did not know he was hiding in the branches, he decided
          to make a quick escape. He climbed down safely when they were not looking and ran for his life.
          But, he left behind the bundle of stolen jewels and money which dropped into Mike’s lap. Mike opened
          it and jumped with joy when he saw the contents. The family gathered all their belongings 
         and returned to the village. There was great excitement when they told everyone how they got 
         rich. Morris thought that the tree was miraculous and this was a nice and quick way to earn 
         some money. He ordered his family to pack some clothes and they set off as if on a journey.
          They also stopped under the same tree and Morris started commanding everyone as Mike had done.
          But no one in his family was willing to obey his orders. Being a rich family, they were used
          to having servants all around. So, the one who went to the river to fetch water enjoyed a nice
          bath. The one who went to get wood for fire went off to sleep. Morris’s wife said ” Everything
          is ready but what shall we eat ?” Morris raised his hands and said, ” Don’t worry. He is watching
          all of this from above. He will help us.” As soon as he finished saying, the thief jumped down
          from the tree with a knife in hand. Seeing him, everyone started running around to save their
          lives. The thief stole everything they had and Morris and his family had to return to the village
          empty handed, having lost all their valuables that they had taken with them.
""")
user_responses2 = {}
for i in range(5):
    question_data = comprehensive_questions[i]
    st.subheader(f"Question {i + 1}:")
    st.write(question_data["question"])
        
        # Display multiple choice options and store user's choice with a unique key
    user_response2 = st.radio(f"Select an option {i}:", question_data["options"], key=f"radio_compre_{i}")
    user_responses2[i] = user_response2
st.subheader("COMPREHENSION-2")
st.write("""
The Kingdom of Spain was created in 1492 with the unification of the Kingdom of Castile and 
the Kingdom of Aragon. For the next three centuries, Spain was the most important colonial power 
in the world. It was the most powerful state in Europe and the foremost global power during the
16th century and the greater part of the 17th century. Spain established a vast empire in the Americas,
stretching from California to Patagonia, and colonies in the western Pacific.
Spain’s European wars, however, led to economic damage, and the latter part of the 17th century
saw a gradual decline of power under an increasingly neglectful and inept Habsburg regime. 
The decline culminated in the War of the Spanish Succession, where Spain’s decline 
from the position of a leading Western power to that of a secondary one, was confirmed, although it
remained the leading colonial power.
The eighteenth century saw a new dynasty, the Bourbons, which directed considerable effort towards
the institutional renewal of the state, with some success, peaking in a successful involvement in the
American War of Independence.
The end of the eighteenth and the start of the nineteenth centuries saw turmoil unleashed throughout
Europe by the French Revolutionary and Napoleonic Wars, which finally led to a French occupation of
much of the continent, including Spain. This triggered a successful but devastating war of independence
that shattered the country and created an opening for what would ultimately be the successful independence
of Spain’s mainland American colonies.
Following a period of growing political instability in the early twentieth century, in 1936 Spain was 
plunged into a bloody civil war. The war ended in a nationalist dictatorship, led by Francisco Franco
which controlled the Spanish government until 1975.
""")
user_responses3 = {}
for i in range(5):
    question_data = read[i]
    st.subheader(f"Question {i + 1}:")
    st.write(question_data["question"])
        
        # Display multiple choice options and store user's choice with a unique key
    user_response3 = st.radio(f"Select an option {i}:", question_data["options"], key=f"radio_compre1_{i}")
    user_responses3[i] = user_response3
    st.markdown('~~~~~~~~~~~~~~~~~~~~~~') 
    
st.markdown('--------------------')
st.header('🧠QUESTIONS ON MEMORY CAPABILITY!!!')
user_responses4 = {}
    
st.title("Quiz on Memory capability")
    
    # Loop through 10 verbal questions
for i in range(5):
    question_datas = mc[i]
    st.subheader(f"Question {i + 1}:")
    st.write(question_datas["question"])
        
        # Display multiple choice options and store user's choice with a unique key
    user_response4 = st.radio(f"Select an option {i}:", question_datas["options"], key=f"radio_mc_{i}")
    user_responses4[i] = user_response4
    st.markdown('~~~~~~~~~~~~~~~~~~~~~~') 
st.markdown('--------------------')

st.header('🎙️QUESTIONS ON COMMUNICATION SKILLS!!!')
user_responses7 = {}
    
st.title("Quiz on Communications skills:")
    
    # Loop through 10 verbal questions
for i in range(5):
    question_datass = gr[i]
    st.subheader(f"Question {i + 1}:")
    st.write(question_datass["question"])
        
        # Display multiple choice options and store user's choice with a unique key
    user_response7 = st.radio(f"Select an option {i}:", question_datass["options"], key=f"radio_gr_{i}")
    user_responses7[i] = user_response7
    st.markdown('~~~~~~~~~~~~~~~~~~~~~~') 

    

    # Check answers and display results for Verbal quiz
if st.button("Submit "):
    with open("C://Users//sanch//OneDrive//Desktop//multipage//logi.txt", 'w') as file:
        file.write("0")  
    st.subheader("Results for Logical Quiz:")
    correct_answers1 = 0
    for i in range(10):
         user_response1 = user_responses1[i]
         correct_answer1 = logical_question[i]["correct_answer"]

         if user_response1 == correct_answer1:
             correct_answers1 += 1
    st.success(f"You got {correct_answers1} out of 10 questions correct for the Logical quiz.")
    st.subheader("Results for Verbal Quiz:")
    correct_answers = 0
    for i in range(5):
        user_response = user_responses[i]
        correct_answer = verbal_questions[i]["correct_answer"]
 
        if user_response == correct_answer:
            correct_answers += 1
    st.success(f"You got {correct_answers} out of 10 questions correct for the Verbal quiz.")
    correct_answers2=0
    st.subheader("Results for Comprehensive Quiz:")
    for i in range(5):
        user_response2 = user_responses2[i]
        correct_answer2 = comprehensive_questions[i]["correct_answer"]
        if user_response2 == correct_answer2:
            correct_answers2 += 1

    correct_answers3=0
   
    for i in range(5):
        user_response3 = user_responses3[i]
        correct_answer3 = read[i]["correct_answer"]

        if user_response3 == correct_answer3:
            correct_answers3 += 1
    correctanstot=correct_answers2+correct_answers3
    st.success(f"You got {correctanstot} out of 10 questions correct for the comprehensive quiz.")
    
    st.subheader("Results for MemoryCapablity Quiz:")
    correct_answers4 = 0
    for i in range(5):
         user_response4 = user_responses4[i]
         correct_answer4 = mc[i]["correct_answer"]

         if user_response4 == correct_answer4:
             correct_answers4 += 1
    st.success(f"You got {correct_answers3} out of 6 questions correct for the MemoryCapablity quiz.")
    correct_answers41=int((correct_answers4/2))
    st.subheader("Results for Communication skills Quiz:")
    correct_answers7 = 0
    for i in range(5):
         user_response7 = user_responses7[i]
         correct_answer7 = gr[i]["correct_answer"]

         if user_response7 == correct_answer7:
             correct_answers7 += 1
    st.success(f"You got {correct_answers7} out of 5 questions correct for the  quiz.")
    correct_answers7per=(correct_answers7*10)
    with open("C://Users//sanch//OneDrive//Desktop//multipage//result.txt", 'w') as file1:
        file1.write(str(correct_answers1)+"\n")
        file1.write(str(correct_answers)+"\n")
        file1.write(str(correct_answers2)+"\n")
        file1.write(str(correctanstot)+"\n")
        file1.write(str(correct_answers7per)+"\n")

        
         