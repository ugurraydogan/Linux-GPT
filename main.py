import openai
import os
from dotenv import load_dotenv

# API Anahtarını daha sonra gireceğim eğer bir zafiyet tespit ederseniz lütfen iletişime geçin / ugurraydogan24@icloud.com
load_dotenv()

# API anahtarını çevre değişkeninden al problem yaşarsın
openai.api_key = os.getenv("OPENAI_API_KEY")

# Sohbet başlatma fonksiyonu
def chat_with_assistant(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # GPT-3.5 modelini kullanalım ilerki zamanlarda değiştiririz
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response['choices'][0]['message']['content']

    except Exception as e:
        print(f"Error: {e}")
        return None

# Ana fonksiyon
def main():
    try:
        user_message = "Hos Geldin Patron"  # Burada istediğiniz mesajı kullanabilirsiniz ben böyle bişeyler yaptım
        print(f"User: {user_message}")

        assistant_response = chat_with_assistant(user_message)
        print(f"Assistant: {assistant_response}")

    except Exception as e:
        print(f"Error: {e}")

# Programı başlatma
if __name__ == "__main__":
    main()
