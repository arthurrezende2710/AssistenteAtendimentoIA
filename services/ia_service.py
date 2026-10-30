import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def gerar_resposta(pergunta, historico):

    chave_api = os.getenv("GROQ_API_KEY")

    if not chave_api:
        raise ValueError("Chave da API não configurada.")

    cliente = Groq(api_key=chave_api)

    mensagens = [
        {
            "role": "system",
            "content": (
                "Você é um assistente virtual de atendimento ao cliente. "
                "Responda sempre em português, com educação, clareza e objetividade. "
                "Ajude com dúvidas sobre compras, entregas, trocas e pagamentos. "
                "Você deve considerar o histórico da conversa para entender o contexto. "
                "Lembre-se das informações que o cliente forneceu nas mensagens anteriores. "
                "Se o cliente perguntar o que ele disse anteriormente, responda usando o histórico. "
                "Você não possui acesso a pedidos reais, sistemas de lojas ou bancos de dados. "
                "Não confunda informações fornecidas pelo cliente com dados consultados em sistemas. "
                "Nunca afirme que pode consultar, rastrear ou alterar pedidos reais. "
                "Não invente informações, prazos ou políticas específicas de lojas. "
                "Quando necessário, oriente o cliente a consultar os canais oficiais."
            )
        }
    ]

    mensagens.extend(historico)

    mensagens.append({
        "role": "user",
        "content": pergunta
    })

    resposta = cliente.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=mensagens
    )

    texto_resposta = resposta.choices[0].message.content

    historico.append({
        "role": "user",
        "content": pergunta
    })

    historico.append({
        "role": "assistant",
        "content": texto_resposta
    })

    return texto_resposta


    