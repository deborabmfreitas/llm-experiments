# Implementação básica de um chatbot que usa a API da OpenAI para gerar respostas em tempo real com streaming

import openai
from dotenv import load_dotenv
import os

# Acessando API
load_dotenv()
secret_key = os.getenv("OPEN_API_KEY")

# Instanciando 
client = openai.Client(api_key=secret_key)

def geracao_texto(mensagens):
    resposta = client.chat.completions.create(
        messages = mensagens,
        model = 'gpt-3.5-turbo-0125',
        temperature = 0,
        max_tokens = 1000,
        stream=True
    )
    print('Bot: ', end='')

    # Lógica para representar o texto stream
    texto_completo = ''
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    print()
    mensagens.append({'role':'assistant','content': texto_completo})

    return mensagens


# Garante que o código só será executado quando o script for executado diretamente (e não importado como um módulo em outro script)
if __name__ == '__main__':
    print('Bem-vindo(a) ao chatbot! 🤖')
    mensagens = []
    while True:
        in_user = input('User: ')
        if in_user.lower() in ['sair', 'exit', 'quit', 'bye']:
            print('Bot: Até mais! 😊')
            break  # Sai do loop e encerra o programa
        
        mensagens.append({'role':'user', 'content': in_user})
        mensagens = geracao_texto(mensagens)