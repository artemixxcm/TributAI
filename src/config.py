"""Configurações da aplicação TributAI.

Centraliza o carregamento das variáveis de ambiente (.env) e os
parâmetros do modelo. Sempre importe a partir daqui, em vez de ler
variáveis de ambiente soltas pelo código.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Carrega o .env que fica na mesma pasta deste arquivo (src/)
load_dotenv(Path(__file__).resolve().parent / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Parâmetros do modelo (com valores padrão caso não estejam no .env)
MODELO = os.getenv("MODELO", "gpt-4o-mini")
TEMPERATURA = float(os.getenv("TEMPERATURA", "0.3"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1200"))

if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY não encontrada. "
        "Crie um arquivo .env em src/ com base no .env.example."
    )