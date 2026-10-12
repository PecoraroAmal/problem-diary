# Problem Diary

**Un piccolo sistema, indipendente dall'AI che usi, per tenere un diario consultabile dei problemi risolti, così il tuo assistente smette di dimenticare.**

Lingue: [tutte le lingue](../README.md)

## L'idea

Se parli con un assistente AI ogni giorno, risolvi sempre gli stessi tipi di problemi, su tanti dispositivi e progetti. L'assistente non ricorda i dettagli e tu spendi diverse richieste per ricostruire il contesto.

Questo progetto tiene un diario in semplice Markdown dentro un repository Git. Quando un problema è risolto, l'assistente scrive una voce breve: **qual era il problema, i passaggi che hanno davvero funzionato e la conclusione** (non tutta la chat, e senza i tentativi falliti). La volta dopo, l'assistente legge prima il diario e trova la risposta con meno richieste.

Serve a chi ha molti progetti e dispositivi. Se fai solo domande veloci e isolate, non ti serve.

## Come funziona

```
 chat con Claude ──"chiudi e salva"──▶ link precompilato ──▶ Claude Code sul web ──▶ commit + push
        ▲                                                                                 │
        └──────── Project di Claude (repo GitHub come conoscenza, premi Sync) ◀───────────┘
```

- **Scrittura:** Claude Code (terminale o web) crea la voce, fa `git pull`, commit e push.
- **Lettura:** il repo viene aggiunto a un Project di Claude come conoscenza. Dopo ogni nuova voce premi l'icona Sync.
- **Nessun server e nessun token in chat.** Il diario è fatto di file nel tuo repo, quindi funziona con qualsiasi strumento che sappia leggere Markdown.

## Cosa serve

- Un tuo repository GitHub (anche privato) creato da questo template.
- Un account Claude Pro, Max o Team (necessario per Claude Code sul web).
- GitHub collegato a [claude.ai/code](https://claude.ai/code), con l'app Claude autorizzata sul repo del diario.
- GitHub collegato a claude.ai (Integrazione GitHub), così un Project può leggere il repo.
- Per le voci lunghe create dalla chat: esecuzione del codice e creazione di file attive nelle impostazioni di Claude.

## Configurazione

1. Crea un repo **privato** da questo template, oppure copia questi file.
2. Collega GitHub a claude.ai/code e autorizza il repo (dai accesso solo a questo repo).
3. Crea un **Project** di Claude. Nella sezione conoscenza premi **+**, scegli **GitHub**, seleziona il repo e i file da includere.
4. Installa la skill in `skill/problem-diary/` e modifica la riga `REPO:` con il tuo `owner/nome-repo`.
5. Elenca i tuoi dispositivi in `diario/DEVICES.md`, con un solo nome ufficiale per dispositivo.

## Uso quotidiano

Quando un problema è risolto, scrivi all'assistente **"chiudi e salva"**. In base alla lunghezza si usa uno di tre percorsi:

| Situazione | Cosa succede |
|---|---|
| Voce breve, dalla chat | La skill prepara un link `claude.ai/code` con prompt e repo già compilati. Lo apri e premi invio. |
| Voce lunga, dalla chat | La skill crea il file `.md` con il nome giusto e ti dice la cartella esatta. Lo carichi dal sito di GitHub (*Add file > Upload files*). |
| Sei già in Claude Code | Scrive il file direttamente: `git pull`, commit, push. Nessun limite di lunghezza. |

Poi premi **Sync** nel Project di Claude, così le chat vedono la nuova voce.

## Struttura del repository

```
README.md                          indice dei README tradotti
CLAUDE.md                          istruzioni per l'agente di coding
docs/README.{lang}.md              README in ogni lingua
diario/
  DEVICES.md                       nomi ufficiali dei dispositivi (un nome per dispositivo)
  _TEMPLATE.md                     modello della voce
  {slug-dispositivo}/
    AAAA-MM-GG-titolo-breve.md     un file per problema risolto
skill/problem-diary/               la skill "chiudi e salva"
  SKILL.md                         flusso e regole
  scripts/build_link.py            costruisce il link precompilato, controlla lunghezza e segreti
  assets/entry-template.md         modello usato dalla skill (da tenere allineato con diario/_TEMPLATE.md)
```

I problemi che non appartengono a un dispositivo (un sito, un servizio condiviso) vanno in `diario/general/`.

## Formato della voce

Ogni voce ha gli stessi titoli fissi, così grep e la ricerca dell'AI funzionano in modo affidabile: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, più i facoltativi **Do not** e **Related**. Il contenuto lo scrivi nella tua lingua. Vedi `diario/_TEMPLATE.md`.

## Limiti e privacy

- Il link porta la voce dentro l'URL, quindi lo usano solo le voci brevi. Quelle più lunghe passano dal file.
- Aprire il link e premere invio resta manuale: non è un salvataggio completamente automatico, e nessuna voce viene salvata senza che tu la veda.
- Ogni voce salvata avvia una sessione di Claude Code sul web, che pesa sull'uso del tuo abbonamento.
- Tieni il repo privato. Le voci descrivono i tuoi sistemi nel dettaglio.
- **Non mettere mai password, token o chiavi in una voce.** Scrivi invece dove sono conservati.
- L'intero repo conta nella capacità della conoscenza del Project. Con voci brevi ce ne stanno centinaia.
- La sincronizzazione GitHub dei Project può a volte rallentare o bloccarsi. Se la chat non vede una nuova voce, premi di nuovo Sync e controlla.

## Licenza

Scegli una licenza per il tuo fork (MIT è una scelta comune per un progetto come questo).
