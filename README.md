# Desafio MBA Engenharia de Software com IA - Full Cycle

Solução de ingestão e busca semântica com LangChain, PostgreSQL + pgVector e OpenAI.

## Pré-requisitos

- Python 3.10+
- Docker e Docker Compose
- API Key da OpenAI

## Configuração

1. Clone o repositório:
```bash
git clone https://github.com/wicarpessoa/mba-ia-desafio-ingestao-busca.git
cd mba-ia-desafio-ingestao-busca
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

Preencha o `.env` com suas credenciais:
```
OPENAI_API_KEY=sk-...
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=documents
PDF_PATH=document.pdf
```

## Execução

1. Suba o banco de dados:
```bash
docker compose up -d
```

2. Execute a ingestão do PDF:
```bash
python src/ingest.py
```

3. Inicie o chat:
```bash
python src/chat.py
```

## Exemplo de uso

```
PERGUNTA: Qual o faturamento da empresa Dourado Logística ME?
RESPOSTA: O faturamento da Dourado Logística ME foi de R$ 3.485.635.733,90.

PERGUNTA: Qual a capital da França?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.
```

## Tecnologias

- **LangChain** — pipeline de RAG
- **PostgreSQL + pgVector** — armazenamento de vetores
- **OpenAI** — embeddings (`text-embedding-3-small`) e LLM (`gpt-4o-mini`)
- **Docker** — execução do banco de dados