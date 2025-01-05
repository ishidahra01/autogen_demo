import os
from dotenv import load_dotenv

from autogen import ConversableAgent

# Load environment variables
load_dotenv(override=True)

model = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")	

print(api_key)
print(endpoint)

Student = ConversableAgent(
    "Student",
    system_message=(
        "あなたは関西に住む20代の若者で、将来の働き方について迷っています。"
        "フリーランスとして自分のペースで働きたい気持ちと、安定した収入が得られる会社員の働き方に魅力を感じています。"
        "家族や趣味を大切にしたいと思っており、どちらの働き方が自分に合っているのかを明確にする必要があります。"
        "積極的に質問をし、自分の価値観を先生に伝えながら、将来の働き方を一つに決めてください。"
    ),
    llm_config={"config_list": [{
        "model": model,
        "api_key": api_key,
        "api_type": "azure",
        "base_url": endpoint,
        "api_version": api_version,
    },]},
    human_input_mode="NEVER",
)

Teacher = ConversableAgent(
    "Teacher",
    system_message=(
        "あなたはキャリアアドバイザーで、将来の働き方に悩む生徒をサポートしています。"
        "フリーランスと会社員、それぞれのメリットとデメリットを生徒に説明し、最終的に生徒が自分の価値観に合った選択をできるように導いてください。"
        "ただし、あなた自身は会社員として働くことの安定性を重視する考えを持っています。"
        "生徒が自分の将来について納得できる結論を出すことがゴールです。"
    ),
    llm_config={"config_list": [{
        "model": model,
        "api_key": api_key,
        "api_type": "azure",
        "base_url": endpoint,
        "api_version": api_version,
    },]},
    human_input_mode="NEVER",
)

result = Teacher.initiate_chat(
    Student,
    message=(
        "こんにちは！将来の働き方について考えていきましょう。"
        "フリーランスで自由な働き方を目指すのか、それとも会社員として安定したキャリアを築くのか、どちらに興味がありますか？"
        "あなたの価値観や目指したい生活スタイルについて教えてください。それをもとに一緒に考えていきましょう！"
    ),
    max_turns=3
)
print(result)
