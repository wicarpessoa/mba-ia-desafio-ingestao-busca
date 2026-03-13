import os 
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Você pode realizar cálculos simples (soma, média, divisão) usando dados presentes no CONTEXTO.
- Se a informação não estiver no CONTEXTO e não puder ser calculada a partir dele, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.


EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt(question=None):
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL"))
    db = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL")
    )
    retriever = db.as_retriever(search_kwargs={"k": 10})

    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)

    llm = ChatOpenAI(model="gpt-4o-mini")
    def format_docs(docs):
          return "\n\n".join(doc.page_content for doc in docs)
    chain = (
      {"contexto": retriever | format_docs, "pergunta": RunnablePassthrough()}
      | prompt
      | llm
      | StrOutputParser()
    )

    return chain


