"""TaxAdvisorAI — chat educativo sobre a Reforma Tributária.

Interface em Gradio que consome o agente definido em agente.py.

Como rodar (a partir da pasta src/):
    python app.py

A aplicação sobe em http://localhost:7860
"""

import gradio as gr

from agent import responder

DESCRICAO = (
    "Assistente educativo sobre a **Reforma Tributária** brasileira. "
    "Tire dúvidas sobre IBS, CBS, Imposto Seletivo, transição e o que muda "
    "no dia a dia. Conteúdo educativo — não substitui orientação de um "
    "contador ou advogado."
)

EXEMPLOS = [
    "O que é a Reforma Tributária em poucas palavras?",
    "Qual a diferença entre IBS e CBS?",
    "Quais impostos vão deixar de existir?",
    "O que é o Imposto Seletivo?",
    "Como vai funcionar o período de transição?",
]

tema = gr.themes.Soft(primary_hue="emerald", secondary_hue="teal")

demo = gr.ChatInterface(
    fn=responder,
    type="messages",
    title="🧾 TaxAdvisorAI",
    description=DESCRICAO,
    examples=EXEMPLOS,
    cache_examples=False,
    theme=tema,
    chatbot=gr.Chatbot(type="messages", height=520),
    textbox=gr.Textbox(
        placeholder="Pergunte algo sobre a Reforma Tributária...",
        scale=7,
    ),
)

if __name__ == "__main__":
    # share=True gera um link público temporário, caso queira compartilhar
    demo.launch()