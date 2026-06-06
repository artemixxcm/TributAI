# src/

Código da aplicação TaxAdvisorAI.

| Arquivo | O que faz |
|---------|-----------|
| `app.py` | Monta a interface Gradio e conecta ao agente |
| `agent.py` | Carrega guardrails e base de conhecimento, chama a API da OpenAI |
| `config.py` | Lê o `.env` e centraliza as configurações do modelo |

## Como rodar

```bash
# A partir da raiz do projeto, com o .venv ativado:
python src/app.py
```

Acesse em http://localhost:7860

## Variáveis de ambiente

Crie um arquivo `.env` dentro desta pasta (`src/.env`) com:

```
OPENAI_API_KEY=sua-chave-aqui
```

Opcionais:

```
MODELO=gpt-4o-mini
TEMPERATURA=0.3
MAX_TOKENS=1200
```
