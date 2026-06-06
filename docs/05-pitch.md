# Pitch — TaxAdvisorAI

> Dica: slides ajudam, mas não precisa exagerar. Fundo limpo, pouco texto por slide, uma imagem quando fizer sentido. O que convence é você falando com segurança e mostrando o projeto rodando.

---

## Roteiro (3 minutos)

### 1. O problema — 30 segundos

Em dezembro de 2023 o Brasil aprovou a maior reforma no sistema tributário desde a Constituição de 1988. Todo mundo ficou sabendo. Mas aí vem a pergunta: você entende o que de fato muda?

Cinco impostos vão desaparecer. Três novos vão surgir. O período de transição vai até 2033. E a maioria das pessoas que vão ser afetadas por isso — pequenos empresários, trabalhadores, consumidores — não tem a menor ideia do que esperar.

O problema não é falta de informação. É que a informação disponível é ou técnica demais — texto de lei que ninguém lê — ou rasa demais — manchete que não explica nada.

*Slide sugerido: uma frase grande — "A maior reforma tributária do Brasil. E quase ninguém entende o que muda."*

---

### 2. A solução — 1 minuto

O TaxAdvisorAI é um chatbot educativo. A pessoa digita qualquer dúvida sobre a reforma — o que é IBS, o que muda pra pequenas empresas, como funciona a transição — e recebe uma resposta em linguagem normal, com exemplos práticos.

Mas o que diferencia ele de só abrir o ChatGPT e perguntar são dois pontos:

**Guardrails.** O agente tem regras explícitas: ele não inventa alíquota quando a lei ainda não definiu. Quando não sabe, ele fala que não sabe. Quando a pergunta está fora do escopo, ele redireciona em vez de tentar responder de qualquer jeito. Essas regras ficam num arquivo de texto separado — dá pra editar o comportamento do agente sem mexer em nenhuma linha de código.

**Base de conhecimento editável.** O conteúdo sobre a reforma fica em arquivos `.md` organizados por tema. Quando uma nova lei complementar sair, é só atualizar o arquivo certo. O agente carrega tudo automaticamente.

*Slide sugerido: diagrama de arquitetura + os dois diferenciais em destaque*

---

### 3. Demonstração — 1 minuto

Abrir o app rodando em `localhost:7860` e mostrar:

1. Clicar num exemplo pronto — *"Qual a diferença entre IBS e CBS?"* — e deixar a resposta chegar em streaming
2. Fazer uma pergunta fora do escopo ao vivo — *"Me ajuda a declarar o IR"* — e mostrar o guardrail funcionando
3. Perguntar sobre alíquota — *"Qual vai ser o percentual do IBS?"* — e mostrar o agente sendo honesto sobre a indefinição em vez de inventar um número

> Grave um vídeo de backup antes da apresentação. Demo ao vivo é ótimo, mas API e internet podem trair na hora errada.

---

### 4. Diferencial e impacto — 30 segundos

O que me preocupou desde o começo foi construir algo que não alucinasse. Um chatbot que inventa alíquotas ou datas em assunto tributário pode prejudicar quem confia na resposta.

A solução foi separar o comportamento do agente do código. Os guardrails são um arquivo de texto que qualquer pessoa — um professor, um contador, um jurista — consegue editar sem precisar saber programar. Isso torna o projeto mais fácil de manter e mais fácil de adaptar conforme a regulamentação avança.

O impacto que eu queria com isso é simples: que qualquer pessoa possa começar a entender a reforma sem precisar contratar um especialista ou ter paciência pra ler legislação.

*Slide sugerido: frase de fechamento — "Informação tributária acessível pra todo mundo."*

---

## Checklist antes de apresentar

- [ ] App rodando e testado (não confiar na última hora)
- [ ] Vídeo de backup gravado
- [ ] Cronômetro ensaiado — 3 minutos passa rápido
- [ ] Exemplos de perguntas prontos pra clicar na demo
- [ ] Áudio sem ruído de fundo

---

## Link do vídeo

*(cole aqui o link quando gravar — YouTube, Loom ou Google Drive funcionam bem)*
