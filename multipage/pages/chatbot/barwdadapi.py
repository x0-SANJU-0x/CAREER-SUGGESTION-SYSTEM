from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("bAhwNX4nIvVEAcjZ8BkWxj-HgI675ZCAxyX6rC2xFwH2wElh0-eEQsi0EeZ-igBx47hYsg.")

bard=Bard(token = token)

result = bard.get_answer("what is your name")
print(result)