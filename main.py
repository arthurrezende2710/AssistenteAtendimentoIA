from services.ia_service import gerar_resposta

def exibir_boas_vindas():
    print("=== Assistente Inteligente de Atendimento ===")

def obter_nome_usuario():
    nome = input("digite seu nome: ").strip()
    return nome

def receber_pergunta():
    pergunta = input("Digite sua pergunta: ").strip()
    return pergunta



def main():
    exibir_boas_vindas()

    nome = obter_nome_usuario()
    historico = []

    print(f"Olá, {nome}! Bem-vindo ao Assistente Inteligente de Atendimento.")
    print("Digite 'sair' quando quiser encerrar o atendimento.\n")

    while True:
        pergunta = receber_pergunta()

        if pergunta.strip().lower() == "sair":
            print("Atendimento encerrado. Até logo!")
            break

        if not pergunta.strip():
            print("Você precisa digitar uma pergunta.\n")
            continue

        try:
            print("Aguarde, estou consultando a IA...")

            resposta = gerar_resposta(pergunta, historico)

            print(f"\nAssistente: {resposta}\n")

        except Exception as erro:
            print(f"Não foi possível gerar a resposta: {erro}\n")



if __name__ == "__main__":
    main()



    