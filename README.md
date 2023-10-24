# Bataille-Navale
I. Règles du jeu
  On simule virtuellement une grille de bataille navale de 5x5
  cases. Deux bateaux, symbolisés chacun par une seule case,
  sont placés aléatoirement dans cette grille. Une case ne peut
  contenir qu'un seul bateau.
  Si le joueur choisit une case contenant un bateau, celui-ci est
  considéré « coulé » (le gain est alors de 10 points). Si un joueur
  choisit une case située sur la même ligne ou sur la même
  colonne qu'un bateau, on considère ce bateau « en vue » (le
  gain est alors de 2 points).
II. Cahier des charges
  1. Coder une fonction permettant de jouer un tour de jeu aléatoire.
  ◦ Un tour de jeu comprend trois coups au plus (il faut tenir compte de l’hypothèse des deux
  premiers coups gagnants, ce qui rendrait le troisième coup inutile), donc trois choix
  (différents) de cases au maximum.
  2. Coder l’importation des personnages inclus dans le fichier « Characters.csv ».
  ◦ Cet import doit aboutir, à minima, à un tableau incluant les noms des personnages.
  3. Coder une fonction permettant de faire jouer tous les personnages, tour à tour.
  ◦ Chaque score doit être conservé, en relation avec le personnage qui vient de jouer.
  4. Coder une IHM (Interface Homme-Machine) permettant :
  ◦ de faire jouer ou rejouer l’ensemble des personnages 10 fois.
  ◦ d’afficher le classement final des personnages (Nom : score), par ordre de score décroissant.
  ◦ d’afficher la moyenne de l’ensemble scores en fin de classement.
  5. Préparer un diaporama permettant de présenter votre projet à la classe en 5 - 10 minutes.
  ◦ Ce diaporama doit inclure un algorithme en pseudo-code, d’une petite partie de votre projet.
III. Bonus optionnels
  En fonction de votre motivation, de vos compétences et du temps que vous souhaitez y consacrer, voici
  quelques pistes optionnelles :
  • Effectuer un import plus large des personnages (incluant leurs caractéristiques).
  • Utiliser une structure de données plus complexe qu’un simple tableau pour stocker les
  personnages (enregistrement, table,...).
  • Afficher des caractéristiques du gagnant (sa « Maison », sa baguette,…).
  • Proposer un classement par « Maison » (Griffondor, Serpentard,…).
  • Ajouter des bateaux de différents types (2, 3 ou 4 cases), sur une grille plus grande.
  • Proposer une interface graphique pour afficher votre jeu (grille(s), coups, scores,...).
  • Proposer un jeu à deux, chaque joueur intervenant l'un après l'autre.
  • Proposer une IA (Intelligence Artificielle) permettant de jouer contre l'ordinateur.
  Les bonus ne se substituent pas au cahier des charges. Si vous ajoutez des bonus, ils doivent s’ajouter
  aux fonctionnalités de base, quitte à gérer deux modes de jeu dans une IHM adaptée.
