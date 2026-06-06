# Pitch — TaxAdvisorAI

# TaxAdvisorAI 🧾

Assistente educacional baseado em Inteligência Artificial desenvolvido para tornar a Reforma Tributária brasileira mais acessível para estudantes, profissionais e pequenos empresários.

O TaxAdvisorAI combina IA Generativa, guardrails declarativos e uma base de conhecimento modular para fornecer respostas claras, contextualizadas e alinhadas às informações disponíveis sobre a Reforma Tributária, evitando alucinações e reduzindo o risco de informações incorretas.

## Principais diferenciais

* Arquitetura baseada em separação de responsabilidades entre comportamento, conhecimento e código.
* Guardrails editáveis para controle de escopo, honestidade e segurança das respostas.
* Base de conhecimento modular em Markdown, permitindo atualização contínua sem necessidade de alterar a aplicação.
* Interface conversacional desenvolvida em Gradio com respostas em streaming.
* Integração com OpenAI GPT-4o-mini para geração de respostas contextualizadas.

## Arquitetura

O agente é construído em três camadas:

1. Identidade do assistente
2. Regras de comportamento (Guardrails)
3. Base de conhecimento sobre a Reforma Tributária

A cada interação, essas camadas são combinadas dinamicamente para fornecer respostas consistentes e alinhadas ao domínio de conhecimento do projeto.

## Tecnologias

* Python
* OpenAI API
* Gradio
* Prompt Engineering
* Guardrails
* Knowledge Base em Markdown

## Objetivo

Demonstrar como técnicas de IA Generativa, governança de respostas e organização de conhecimento podem ser aplicadas para criar assistentes especializados capazes de transformar temas complexos em experiências acessíveis para o usuário final.

Projeto desenvolvido como desafio de IA Generativa da DIO.


