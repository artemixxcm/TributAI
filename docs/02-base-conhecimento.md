# Base de Conhecimento — TaxAdvisorAI

## Como eu pensei nisso

Quando fui montar a base de conhecimento, a primeira ideia foi usar algum sistema de busca vetorial tipo FAISS ou ChromaDB. Mas aí percebi que, pra esse projeto, seria complexidade desnecessária: a base de conhecimento sobre a reforma tributária não é tão grande assim, e o GPT-4o-mini aguenta receber o conteúdo completo no contexto sem problema.

Então optei por uma abordagem bem mais simples: carregar todos os arquivos `.md` da pasta `docs/knowledge/` e injetar tudo direto no system prompt. Sem banco vetorial, sem embeddings, sem servidor rodando em paralelo. Funciona, é fácil de manter e qualquer pessoa consegue editar o conteúdo sem precisar entender de IA.

---

## O que tem na base

Dividi o conteúdo em quatro arquivos, cada um com um tema específico:

**`01-visao-geral.md`** — começa pelo começo: o que é a reforma, por que ela foi necessária, o que muda na estrutura geral. É o arquivo que responde "mas afinal, o que é isso?"

**`02-novos-tributos.md`** — entra nos detalhes de CBS, IBS e Imposto Seletivo. Quem arrecada cada um, o que substitui, como funciona o crédito. A parte mais técnica da base.

**`03-transicao.md`** — o cronograma de 2026 a 2033, como funciona a coexistência dos sistemas antigo e novo, e o que acontece com o Simples Nacional.

**`04-impactos.md`** — o que muda na prática pra consumidores, empresas e setores específicos. Também lista o que ainda não foi regulamentado — importante pra o agente não inventar respostas sobre esses pontos.

---

## Como o carregamento funciona

O `agent.py` tem uma função que faz isso automaticamente:

```python
def _carregar_base_conhecimento() -> str:
    pasta = RAIZ / "docs" / "knowledge"
    arquivos = sorted(pasta.glob("*.md"))
    partes = [arq.read_text(encoding="utf-8").strip() for arq in arquivos]
    return "\n\n---\n\n".join(partes)
```

Ela busca todos os `.md` dentro da pasta, ordena pelo nome do arquivo (por isso usei numeração no começo — `01-`, `02-`...) e junta tudo num bloco só separado por `---`. Esse bloco vai pro system prompt quando o agente é iniciado.

---

## Por que separei em arquivos ao invés de um só

Poderia ter colocado tudo num arquivo enorme. Mas ficou mais fácil de manter assim: se sair uma nova lei complementar sobre a transição, eu sei exatamente onde editar (`03-transicao.md`). Se quiser adicionar um novo tema, crio um `05-setor-servicos.md` e ele é carregado automaticamente na próxima vez que o app subir.

Não precisa mexer em nenhuma linha de código pra isso.

---

## Limitação que vale mencionar

O conteúdo foi escrito com base na EC 132/2023 e no que estava regulamentado até o momento em que o projeto foi feito. A Reforma Tributária ainda tem vários pontos sendo definidos por leis complementares — então partes da base podem ficar desatualizadas conforme o processo avança. Manter os arquivos atualizados faz parte da manutenção do projeto.

Por isso o `04-impactos.md` tem uma seção específica sobre "o que ainda está em aberto" — o agente é instruído a usar essa informação em vez de inventar algo que ainda não existe.
