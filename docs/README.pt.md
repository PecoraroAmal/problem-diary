# Problem Diary

**Um pequeno sistema, independente da IA que usas, para manter um diário pesquisável dos problemas que resolveste, para que o teu assistente deixe de esquecer.**

Idiomas: [todos os idiomas](../README.md)

## A ideia

Se falas com um assistente de IA todos os dias, resolves vezes sem conta os mesmos tipos de problemas, em muitos dispositivos e projetos. O assistente não se lembra dos detalhes e gastas vários pedidos a reconstruir o contexto.

Este projeto mantém um diário em Markdown simples num repositório Git. Quando um problema é resolvido, o assistente escreve uma entrada curta: **qual era o problema, os passos que realmente funcionaram e a conclusão** (não a conversa toda, nem as tentativas falhadas). Da próxima vez, o assistente lê primeiro o diário e encontra a resposta com menos pedidos.

É útil se tiveres muitos projetos e dispositivos. Se só fizeres perguntas rápidas e isoladas, não precisas dele.

## Como funciona

```
 chat com o Claude ──"close and save"──▶ link pré-preenchido ──▶ Claude Code na web ──▶ commit + push
        ▲                                                                                  │
        └──────── Project do Claude (repo do GitHub como conhecimento, prime Sync) ◀───────┘
```

- **Escrita:** o Claude Code (terminal ou web) cria a entrada, executa `git pull`, faz commit e push.
- **Leitura:** o repo é adicionado a um Project do Claude como conhecimento. Depois de cada nova entrada, prime o ícone Sync.
- **Sem servidor e sem tokens no chat.** O diário são apenas ficheiros no teu próprio repo, por isso funciona com qualquer ferramenta que leia Markdown.

## Requisitos

- Um repositório GitHub teu (privado serve) criado a partir deste modelo.
- Uma conta Claude Pro, Max ou Team (necessária para o Claude Code na web).
- GitHub ligado a [claude.ai/code](https://claude.ai/code), com a app Claude autorizada no repo do diário.
- GitHub ligado ao claude.ai (a integração com o GitHub) para que um Project possa ler o repo.
- Para entradas longas criadas a partir do chat: execução de código e criação de ficheiros ativadas nas definições do Claude.

## Configuração

1. Cria um repo **privado** a partir deste modelo e clona ou carrega estes ficheiros.
2. Liga o GitHub em claude.ai/code e autoriza o repo (dá acesso apenas a este repo).
3. Cria um **Project** do Claude. Na secção de conhecimento prime **+**, escolhe **GitHub**, seleciona o teu repo e os ficheiros a incluir.
4. Instala a skill de `skill/problem-diary/` e edita a linha `REPO:` com o teu `owner/nome-do-repo`.
5. Lista os teus dispositivos em `diario/DEVICES.md`, com um único nome oficial por dispositivo.

## Uso diário

Quando um problema for resolvido, diz ao assistente **"close and save"**. Consoante o tamanho, é usado um de três caminhos:

| Situação | O que acontece |
|---|---|
| Entrada curta, a partir do chat | A skill prepara um link `claude.ai/code` com o prompt e o repo já preenchidos. Abre-o e prime Enter. |
| Entrada longa, a partir do chat | A skill cria o ficheiro `.md` com o nome certo e diz-te a pasta exata. Carrega-o no site do GitHub (*Add file > Upload files*). |
| Já estás no Claude Code | Escreve o ficheiro diretamente: `git pull`, commit, push. Sem limite de tamanho. |

Depois prime **Sync** no Project do Claude, para que os chats vejam a nova entrada.

## Estrutura do repositório

```
README.md                          índice dos README traduzidos
CLAUDE.md                          instruções para o agente de código
docs/README.{lang}.md              README em cada idioma
diario/
  DEVICES.md                       nomes oficiais dos dispositivos (um nome por dispositivo)
  _TEMPLATE.md                     modelo de entrada
  {device-slug}/
    YYYY-MM-DD-short-title.md      um ficheiro por problema resolvido
skill/problem-diary/               a skill "close and save"
  SKILL.md                         fluxo de trabalho e regras
  scripts/build_link.py            constrói o link pré-preenchido, verifica tamanho e segredos
  assets/entry-template.md         modelo usado pela skill (manter sincronizado com diario/_TEMPLATE.md)
```

Os problemas que não pertencem a nenhum dispositivo (um site, um serviço partilhado) vão para `diario/general/`.

## Formato da entrada

Cada entrada tem os mesmos títulos fixos, para que o grep e a pesquisa por IA funcionem de forma fiável: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, mais os opcionais **Do not** e **Related**. O conteúdo é escrito no teu próprio idioma. Vê `diario/_TEMPLATE.md`.

## Limites e privacidade

- Um link leva a entrada dentro do URL, por isso só as entradas curtas o usam. As mais longas usam o ficheiro.
- Abrir o link e premir Enter continua a ser manual: não é totalmente automático e nenhuma entrada é guardada sem que a vejas.
- Cada entrada guardada inicia uma sessão do Claude Code na web, que conta para o uso da tua subscrição.
- Mantém o repo privado. As entradas descrevem os teus sistemas em detalhe.
- **Nunca ponhas palavras-passe, tokens ou chaves numa entrada.** Escreve, em vez disso, onde estão guardados.
- Todo o repo conta para a capacidade de conhecimento do Project. Cabem centenas de entradas curtas.
- A sincronização do GitHub nos Projects pode por vezes atrasar-se ou falhar. Se o chat não vir uma nova entrada, prime Sync outra vez e verifica.

## Licença

Escolhe uma licença para o teu fork (MIT é uma escolha comum para um projeto como este).
