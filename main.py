from google import genai 
from app.prompt.system_prompt import SYSTEM_PROMPT
from google.genai.types import GenerateContentConfig


class ChatService:
    def _init_(self, client,model_name:str,max_history:int=5):

        self.client=client
        self.model=model_name
        self.max_history=max_history
        self.history=[]
    def _build_prompt(self,user_input:str)->str:

        self.history=self.history[-self.max_history:]
        conversation="\n".join(self.history)
        prompt= f""" 
{SYSTEM_PROMPT} \n
conversation so far: {conversation} \n
User Input :{ user_input}

"""
        return prompt
    
    async def chatbot(self,user_input:str)->str:
        if not user_input.strip():
            raise ValueError("Prompt cannot be empty ")
        
        final_prompt=self._build_prompt(user_input)

        try:
            response=self.client.models.generate_content(
                model=self.model,
                contents=final_prompt,
                config=GenerateContentConfig(
                    max_output_tokens=500
                )
            )
            bot_reply=response.text.strip()

        except Exception:

            raise RuntimeError("Gemini Service not available")
        
        self.history.append(f"user Input {user_input}")
        self.history.append(f" Bot {bot_reply}")
        return bot_reply
    
    async def  summarize_bot(self,bot_reply:str)->str:

        if not bot_reply.strip():
            raise ValueError("bot reply cannot be empty ")
        
        summarize_prompt=f"""
        You are helpful writer your job is to summarize the following text :\n {bot_reply}"""
        summary=self.client.models.generate_content(
            model=self.model,
            contents=summarize_prompt
        )
        return summary.text.strip()
    # main.py


from fastapi import FastAPI, HTTPException
from google import genai
from app.services.chat_service import ChatService

from dotenv import load_dotenv

load_dotenv()
client=genai.Client()
chat_service=ChatService(client,"gemini-3-flash-preview")
app=FastAPI()

@app.post("/chat/")

async def chat_endpoint(user_input:str):

    try:
        bot_response=await chat_service.chatbot(user_input)
        summarize_response=await chat_service.summarize_bot(bot_response)
        return { "Main Content":bot_response,
                "Summarize Content":summarize_response}
    
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=500,detail=str(e))

system_prompt.py
SYSTEM_PROMPT="""

YOU are helpful assistant 

Rules you have to follow

- Give clear and concise answer to user 
- Do not hallucinate 
- Do not give irrelevant answer to user if you don't know anything 
- Give clear and concise output

"""