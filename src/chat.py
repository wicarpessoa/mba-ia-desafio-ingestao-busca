from search import search_prompt                                                                                                                                                            
   
def main():                                                                                                                                                                                 
    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    while True:
        pergunta = input("\nPERGUNTA: ")
        if not pergunta:
            continue
        resposta = chain.invoke(pergunta)
        print(f"\nRESPOSTA: {resposta}")

if __name__ == "__main__":
    main()

