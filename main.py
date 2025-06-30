from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
import logging #because Hum suppress karna chahte haen logging from the OpenAI library
logging.getLogger("openai").setLevel(logging.ERROR)


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client= provider
)

agent = Agent(
    name="Academic Research Assistant",
    instructions="You are an academic research assistant. Your task is to assist with research tasks, provide summaries, and answer questions based on academic literature, and answer only about the academic questions other than say sorry, like i am a student agent so ask me only about academic related questions and when someone says Hi, you should respond with Assalamualaikum and some friendly words.",
    model=model,
)

user_question = input( "Please Enter your question: " )

result = Runner.run_sync(agent, user_question)
print(result.final_output)