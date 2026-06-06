# Base de Conhecimento — TaxAdvisorAI

## Estratégia adotada

A base de conhecimento do TaxAdvisorAI usa uma abordagem chamada **RAG simples por injeção de contexto**: os arquivos com o conteúdo sobre a reforma são carregados e inseridos diretamente no system prompt a cada conversa.

Não há banco vetorial nem embeddings — o modelo recebe o conteúdo completo como contexto. Isso funciona bem porque:
- A base cabe confortavelmente no contexto do GPT-4o-mini (bem abaixo do limite de tokens)
- É fácil de manter: basta editar os arquivos `.md`, sem precisar reindexar nada
- Garante que o agente use o conteúdo como fonte prioritária nas respostas

---

## Estrutura dos arquivos

Os arquivos ficam em `docs/knowledge/` e são carregados em ordem alfabética pelo nome do arquivo:

| Arquivo | Conteúdo |
|---------|---------|
| `01-visao-geral.md` | O que é a Reforma Tributária, por que ela foi necessária, o que muda na estrutura (EC 132/2023) |
| `02-novos-tributos.md` | CBS, IBS e Imposto Seletivo em detalhe: quem arrecada, o que substitui, cronograma |
| `03-transicao.md` | Cronograma completo 2026–2033, Simples Nacional, fundos criados |
| `04-impactos.md` | Impactos para consumidores, empresas e setores com regime diferenciado; o que ainda está em aberto |

---

## Como os dados são carregados

O arquivo `src/agent.py` contém a função `_carregar_base_conhecimento()`, que:
1. Busca todos os arquivos `.md` dentro de `docs/knowledge/`
2. Ordena por nome (para garantir a sequência lógica)
3. Concatena o conteúdo separado por `---`
4. Injeta tudo na seção "Base de conhecimento" do system prompt

```python
# Trecho simplificado do agent.py
def _carregar_base_conhecimento() -> str:
    pasta = RAIZ / "docs" / "knowledge"
    arquivos = sorted(pasta.glob("*.md"))
    partes = [arq.read_text(encoding="utf-8").strip() for arq in arquivos]
    return "\n\n---\n\n".join(partes)
```

---

## Como os dados são usados no prompt

O system prompt final tem três camadas:

```
[Identidade do agente]
    → Quem é o TaxAdvisorAI e o que ele faz

[Guardrails — docs/guardrails.md]
    → Regras de escopo, frases de honestidade, o que não pode fazer

[Base de conhecimento — docs/knowledge/*.md]
    → Conteúdo sobre a reforma, usado como fonte prioritária
```

A instrução para o modelo é: use a base de conhecimento como fonte principal. Se a pergunta não for coberta por ela, diga isso antes de responder com conhecimento geral.

---

## Exemplo de contexto montado

```
# Base de conhecimento

Use as informações abaixo como fonte principal. Se a pergunta não for
coberta por elas, diga isso claramente antes de responder com conhecimento geral.

# Visão Geral da Reforma Tributária

## O que é
A Reforma Tributária do consumo foi aprovada pela Emenda Constitucional nº 132,
promulgada em 20 de dezembro de 2023...

---

# Os Novos Tributos: CBS, IBS e Imposto Seletivo

## CBS — Contribuição sobre Bens e Serviços
- Esfera: federal (substitui PIS e COFINS)
...
```

---

## Como expandir a base

Para adicionar um novo tema (ex.: impacto no setor de saúde), basta criar um novo arquivo:

```
docs/knowledge/05-setor-saude.md
```

Na próxima vez que o agente for iniciado, o arquivo é carregado automaticamente. Sem precisar mexer em nenhuma linha de código.

---

## Limitação importante

O conteúdo da base reflete o estado da legislação no momento em que os arquivos foram escritos. Como a Reforma Tributária ainda está sendo regulamentada por leis complementares, **alguns pontos ficam desatualizados conforme novas regras são publicadas**. Manter os arquivos de `knowledge/` atualizados é parte da manutenção do projeto.
