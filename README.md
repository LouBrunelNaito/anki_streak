# Anki Kawaii Streak Add-on 🌸🔥

Greffon Anki basique permettant de visualiser sa « streak » actuelle.

Un greffon léger et mignon (style kawaii) pour **Anki** qui calcule et affiche directement sur l'écran principal le nombre de jours d'affilés où vous avez effectué vos révisions. 

---

## Fonctionnalités

* **Calcul dynamique de la série (Streak) :** Analyse votre historique de révision (`revlog`) en prenant en compte le décalage horaire d'Anki.
* **Bannière dynamique :** Affiche un message d'encouragement personnalisé selon si vous avez déjà révisé aujourd'hui ou non.
* **Style Kawaii :** Design doux et animations fluides (pulsation du feu) directement intégrés à l'interface d'accueil.
* **Hook Officiel Anki :** Utilise `deck_browser_will_render_content` pour une intégration propre et sans conflit.

---

## Installation pas à pas

Puisque ce greffon est fourni sous la forme d'un script Python direct (`__init__.py`), voici comment l'installer manuellement dans votre logiciel Anki :

### Étape 1 : Localiser le dossier des add-ons d'Anki

1. Ouvrez l'application **Anki** sur votre ordinateur.
2. Dans le menu supérieur, cliquez sur **Outils** (ou *Tools*) puis sur **Greffons** (ou *Add-ons*). *(Raccourci : `Ctrl + Shift + A` sur Windows/Linux ou `Cmd + Shift + A` sur Mac)*.
3. Dans la fenêtre qui s'ouvre, cliquez sur le bouton **Afficher les fichiers** (ou *View Files*) en bas à droite.
4. Cela ouvre le dossier des greffons Anki (`addons21`) dans votre explorateur de fichiers.

### Étape 2 : Créer le dossier pour le greffon

1. À l'intérieur du dossier `addons21`, créez un nouveau dossier.
2. Nommez ce dossier de manière explicite, par exemple : `kawaii_streak`.

### Étape 3 : Ajouter le fichier `__init__.py`

1. Récupérez le fichier `__init__.py` présent à la racine de ce dépôt GitHub.
2. Copiez ce fichier `__init__.py` directement dans le dossier `kawaii_streak` que vous venez de créer.

> **Remarque :** L'arborescence finale doit ressembler à ceci :
> ```text
> Anki2/
> └── addons21/
>     └── kawaii_streak/
>         └── __init__.py
> ```

### Étape 4 : Redémarrer Anki

1. Fermez complètement l'application **Anki**.
2. Relancez **Anki**.
3. La bannière **Kawaii Streak** apparaît désormais au-dessus de la liste de vos paquets ! 🎉
