# Problem Diary

**Un petit système, indépendant de l'IA que vous utilisez, pour tenir un journal consultable des problèmes que vous avez résolus, afin que votre assistant arrête d'oublier.**

Langues : [toutes les langues](../README.md)

## L'idée

Si vous parlez chaque jour à un assistant IA, vous résolvez sans cesse les mêmes types de problèmes, sur de nombreux appareils et projets. L'assistant ne retient pas les détails et vous dépensez plusieurs requêtes pour reconstituer le contexte.

Ce projet conserve un journal en simple Markdown dans un dépôt Git. Quand un problème est résolu, l'assistant écrit une courte entrée : **quel était le problème, les étapes qui ont réellement fonctionné et la conclusion** (pas toute la conversation, ni les tentatives ratées). La fois suivante, l'assistant lit d'abord le journal et trouve la réponse avec moins de requêtes.

C'est utile si vous avez beaucoup de projets et d'appareils. Si vous ne posez que des questions rapides et isolées, vous n'en avez pas besoin.

## Fonctionnement

```
 chat avec Claude ──"close and save"──▶ lien prérempli ──▶ Claude Code sur le web ──▶ commit + push
        ▲                                                                                  │
        └──────── Project Claude (dépôt GitHub comme connaissance, appuyez sur Sync) ◀─────┘
```

- **Écriture :** Claude Code (terminal ou web) crée l'entrée, exécute `git pull`, commit et push.
- **Lecture :** le dépôt est ajouté à un Project Claude comme connaissance. Après chaque nouvelle entrée, appuyez sur l'icône Sync.
- **Aucun serveur et aucun token dans le chat.** Le journal n'est qu'un ensemble de fichiers dans votre dépôt ; il fonctionne donc avec tout outil capable de lire du Markdown.

## Prérequis

- Votre propre dépôt GitHub (privé convient) créé à partir de ce modèle.
- Un compte Claude Pro, Max ou Team (nécessaire pour Claude Code sur le web).
- GitHub connecté à [claude.ai/code](https://claude.ai/code), avec l'application Claude autorisée sur votre dépôt de journal.
- GitHub connecté à claude.ai (l'intégration GitHub) pour qu'un Project puisse lire le dépôt.
- Pour les entrées longues créées depuis le chat : exécution de code et création de fichiers activées dans les paramètres de Claude.

## Installation

1. Créez un dépôt **privé** à partir de ce modèle, puis clonez ou importez ces fichiers.
2. Connectez GitHub à claude.ai/code et autorisez le dépôt (accès à ce seul dépôt).
3. Créez un **Project** Claude. Dans sa section de connaissances, appuyez sur **+**, choisissez **GitHub**, sélectionnez votre dépôt et les fichiers à inclure.
4. Installez la skill de `skill/problem-diary/` et modifiez sa ligne `REPO:` avec votre `owner/nom-du-depot`.
5. Listez vos appareils dans `diario/DEVICES.md`, avec un seul nom officiel par appareil.

## Utilisation quotidienne

Quand un problème est résolu, dites à l'assistant **"close and save"**. Selon la longueur, l'un des trois chemins est utilisé :

| Situation | Ce qui se passe |
|---|---|
| Entrée courte, depuis le chat | La skill prépare un lien `claude.ai/code` avec le prompt et le dépôt déjà renseignés. Ouvrez-le et appuyez sur Entrée. |
| Entrée longue, depuis le chat | La skill crée le fichier `.md` avec le bon nom et vous indique le dossier exact. Importez-le depuis le site GitHub (*Add file > Upload files*). |
| Vous êtes déjà dans Claude Code | Il écrit le fichier directement : `git pull`, commit, push. Aucune limite de longueur. |

Appuyez ensuite sur **Sync** dans le Project Claude pour que les chats voient la nouvelle entrée.

## Structure du dépôt

```
README.md                          index des README traduits
CLAUDE.md                          instructions pour l'agent de code
docs/README.{lang}.md              README dans chaque langue
diario/
  DEVICES.md                       noms officiels des appareils (un nom par appareil)
  _TEMPLATE.md                     modèle d'entrée
  {device-slug}/
    YYYY-MM-DD-short-title.md      un fichier par problème résolu
skill/problem-diary/               la skill "close and save"
  SKILL.md                         flux de travail et règles
  scripts/build_link.py            construit le lien prérempli, vérifie longueur et secrets
  assets/entry-template.md         modèle utilisé par la skill (à garder synchronisé avec diario/_TEMPLATE.md)
```

Les problèmes qui ne dépendent d'aucun appareil (un site web, un service partagé) vont dans `diario/general/`.

## Format d'une entrée

Chaque entrée a les mêmes titres fixes, pour que grep et la recherche par IA restent fiables : **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus les optionnels **Do not** et **Related**. Le contenu est écrit dans votre langue. Voir `diario/_TEMPLATE.md`.

## Limites et confidentialité

- Un lien contient l'entrée dans l'URL ; seules les entrées courtes l'utilisent. Les plus longues passent par le fichier.
- Ouvrir le lien et appuyer sur Entrée reste manuel : ce n'est pas entièrement automatique, et aucune entrée n'est enregistrée sans que vous la voyiez.
- Chaque entrée enregistrée lance une session Claude Code sur le web, qui compte dans l'utilisation de votre abonnement.
- Gardez le dépôt privé. Les entrées décrivent vos systèmes en détail.
- **Ne mettez jamais de mots de passe, tokens ou clés dans une entrée.** Indiquez plutôt où ils sont stockés.
- Tout le dépôt compte dans la capacité de connaissances du Project. Des centaines d'entrées courtes y tiennent.
- La synchronisation GitHub des Projects peut parfois être lente ou échouer. Si le chat ne voit pas une nouvelle entrée, appuyez de nouveau sur Sync et vérifiez.

## Licence

Choisissez une licence pour votre fork (MIT est un choix courant pour un projet comme celui-ci).
