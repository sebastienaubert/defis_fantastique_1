# Le sorcier de la montagne de Feu
# NSI Mermoz 2019

import random

def paragraphe_rumeurs():
    texte=["Seul un aventurier téméraire entreprendrait une quête aussi périlleuse",
           "sans avoir préalablement essayé de savoir le plus de choses possibles",
           "sur la montagne au sommet de feu et ses trésors. Avant d'arriver au pied",
           "de la montagne, vous avez passé plusieurs jours avec les habitants d'un",
           "village des environs qui se trouve à deux jours de marche. Comme vous",
           "êtes sympathique, vous n'avez pas eu de difficultés à vous faire des",
           "amis parmi les paysans du coin. Bien qu'ils vous aient raconté",
           "beaucoup d'histoires au sujet du mystérieux sanctuaire du sorcier, vous",
           "ne pouvez pas avoir la certitude que tous ces récits - ni même un seul",
           "d'entre eux - se fondent sur des faits réels. Les villageois ont vu passer",
           "de nombreux aventuriers qui s'en allaient vers la montagne, mais très",
           "peu en sont revenus. C'est un voyage extrêmement dangereux, voilà au",
           "moins quelque chose dont vous êtes sûr. Parmi ceux qui ont reparu au",
           "village, il n'en est pas un seul qui ait envisagé de retourner dans la",
           "montagne au sommet de feu.",
           "Il semble qu'il y ait quelque vérité dans la rumeur selon laquelle le",
           "trésor du Sorcier serait enfermé dans un coffre somptueux doté de deux",
           "serrures dont les clés sont gardées par diverses créatures à l'intérieur",
           "des souterrains. Le Sorcier lui-même disposerait d'un puissant pouvoir.",
           "Certains le décrivent comme un vieillard, d'autres comme un jeune",
           "homme. D'après certains villageois, son pouvoir lui viendrait d'un jeu",
           "de cartes magique, mais d'autres prétendent que sa force réside dans les",
           "gants de soie noire qu'il porte en permanence.",
           "L'accès à la montagne est gardé, paraît-il, par des lutins au visage",
           "constellé de verrues, des créatures stupides qui ne pensent qu'à manger",
           "et à boire. A mesure qu'on avance à l'intérieur, les créatures deviennent",
           "plus redoutables. Pour atteindre les salles intérieures, il faut franchir",
           "une rivière. Il y a un bac qui la traverse régulièrement, mais le passeur,",
           "à ce qu'on dit, tient à recevoir le prix de ses services, et il convient donc",
           "de se munir d'une Pièce d'Or pour le voyage (inscrivez-la sur votre",
           "Feuille d'Aventure). Les gens du cru vous conseillent également de",
           "dresser une bonne carte au fur et à mesure de vos déambulations, car",
           "sans cela vous seriez irrémédiablement perdu au cœur de la montagne.",
           "Quand arrive enfin le jour du départ, tout le village vient vous souhaiter",
           "un voyage sans encombre. Beau-coup de femmes, ainsi que des enfants",
           "et des vieillards, ont la larme à l'œil. Vous ne pouvez vous empêcher de",
           "vous demander si ce ne sont pas des larmes de tristesse versées par des",
           "yeux qui ne vous reverront plus jamais vivant...",
           "Et maintenant, tournez la page !"]
    for loop in range(len(texte)):
        print(texte[loop])

    choix=input("ET maintenant, appuyer sur entrée pour continuer")
    print()
    paragraphe_1()

# paragraphe 1
def paragraphe_1():
    texte=["Vos deux jours de marche sont enfin terminés. Après avoir ôté votre",
           "épée de son fourreau, vous la déposez sur le sol et vous poussez un",
           "soupir de soulagement en vous asseyant sur un rocher couvert de",
           "mousse pour prendre quelques instants de repos. Vous vous étirez, vous",
           "vous frottez les yeux, puis vous levez votre regard vers la montagne au",
           "sommet de feu. La montagne elle-même paraît menaçante. Son flanc",
           "escarpé, face à vous, semble avoir été déchiqueté par les griffes de",
           "quelque créature gigantesque. Il est hérissé d'à-pics rocheux aux angles",
           "tranchants dont on a peine à croire qu'ils aient été façonnés par la",
           "nature. Au sommet, on aperçoit une couleur d'un rouge sinistre - sans",
           "doute l'effet d'une étrange végétation - qui a donné son nom à la",
           "montagne. Personne, peut-être, ne saura jamais ce qui pousse là-haut,",
           "car il est certainement impossible d'escalader ce pic.",
           "Votre quête commence maintenant. De l'autre côté de la clairière, il y a",
           "l'entrée d'une caverne sombre. Vous ramassez votre épée, vous vous",
           "relevez et vous pensez à tous les dangers qui vous attendent. Puis, avec",
           "détermination, vous remettez l'épée dans son fourreau et vous vous",
           "avancez vers l'entrée de la caverne. Vous jetez un coup d'œil dans les",
           "ténèbres et vous apercevez des parois suintantes et sombres ainsi que",
           "des flaques d'eau sur le sol de pierre. L'air est froid et humide. Vous",
           "allumez votre lanterne et vous faites prudemment quelques pas dans",
           "l'obscurité. Des toiles d'araignées vous balaient le visage et vous",
           "entendez le bruit que font sur le sol des pattes minuscules ; ce sont",
           "probablement des rats qui prennent la fuite. Vous entrez dans la",
           "caverne. Après avoir parcouru quelques mètres, vous arrivez à une",
           "bifurcation."]
    
    for loop in range(len(texte)):
        print(texte[loop])

    print("Après avoir parcouru quelques mètres, vous arrivez à une bifurcation. Irez-vous vers l'ouest ou vers l'est ?")
    
    choix=input("Entrez votre choix ouest ou est:")

    print()
    if choix=="est":
        paragraphe_278()
    elif choix=="ouest":
        paragraphe_71()

# paragraphe 33
def paragraphe_33():
    print("33 à faire")

# paragraphe 71
def paragraphe_71():
    global chance # pour que chance du programme principal soit connu de cette procedure

    # système de chance à améliorer
    texte=["Le passage forme un virage à droite en direction du nord. Vous vous",
           "approchez prudemment d'une guérite qui se trouve au coin et en jetant",
           "un coup d'oeil à l'intérieur, vous apercevez une étrange créature qui",
           "ressemble à un Lutin, vêtue d'une armure de cuir et endormie à son",
           "poste. Vous essayez de passer devant sur la pointe des pieds."]
    for loop in range(len(texte)):
        print(texte[loop])

    choix=random.randint(1,6)+random.randint(1,6)
    if choix<=chance:
        resultat=True
    else:
        resultat=False
    chance=chance-1 

    print()
    if resultat:
        print("Vous etes chanceux, le Lutin ne se réveille pas et continue à ronfler bruyamment.")
        paragraphe_301()
    else:
        print("Vous etes malchanceux, vous faites en marchant un bruit qui le réveille, et il ouvre les yeux.")
        paragraphe_248()        

# paragraphe 82
def paragraphe_82():
    global chance
    texte=["La porte s'ouvre sur une petite pièce où règne une forte odeur. Au",
           "milieu se trouve une table bancale sur laquelle est posée une bougie",
           "allumée. Sous la table, il y a une petite boîte en bois. Une créature de",
           "petite taille, à la silhouette trapue, le visage laid et couvert de verrues,",
           "don sur une paillasse posée dans un coin, à l'autre bout de la pièce ;",
           "c'est une créature semblable à celle que vous avez trouvée endormie",
           "dans la guérite. C'est probablement le veilleur de nuit. Vous pouvez",
           "choisir de regagner le couloir et de continuer vers le nord",
           "ou de ramper sur le sol de la pièce pour essayer de vous",
           "emparer de la boîte sans réveiller la créature."]
    for loop in range(len(texte)):
        print(texte[loop])

    choix=input("Choisissez regagner ou tenter")

    if choix=="regagner":
        print("Vous décidez de regagner le couloir et continuer vers le Nord.")
        paragraphe_208()

    choix=random.randint(1,6)+random.randint(1,6)
    if choix<=chance:
        resultat=True
    else:
        resultat=False
    chance=chance-1

    if resultat:
        print("La créature ne se réveille pas.")
        paragraphe_147()
    else:
        paragraphe_33()

# paragraphe 92
def paragraphe_92():
    texte=["Vous êtes de retour au croisement. Vous regardez sur votre gauche vers",
           "l'entrée de la caverne qui vous apparaît au lointain dans l'obscurité,",
           "mais vous marchez droit devant vous."]
    for loop in range(len(texte)):
        print(texte[loop])
        
    choix=input("ET maintenant, appuyer sur entrée pour continuer")
    print()
    paragraphe_71()

# paragraphe 147
def paragraphe_147():
    print("147 à faire")
    
# paragraphe 156
def paragraphe_156():
    texte=["Vous essayez d'enfoncer la porte à coups d'épaule. Jetez deux dés. Si le",
           "chiffre obtenu est égal ou inférieur au total de vos points d'HABILETÉ,",
           "vous avez réussi et vous allez au 343. Si le chiffre obtenu est supérieur",
           "à vos points d'HABILETÉ, vous frottez votre épaule endolorie et vous",
           "décidez de ne pas faire de seconde tentative. Retournez à la bifurcation",
           "en vous rendant au 92."]
    for loop in range(len(texte)):
        print(texte[loop])

    print("156 à finir manque test d'habilité, pour l'instant random")
    choix=random.randint(6)
    if choix<=3:
        print("Vous avez réussi !")
        print()
        paragraphe_343()
    else:
        print("Vous frottez votre épaule épaule endolorie et vous décidez de ne pas faire de seconde tentative. Vous retournez à la bifurcation.")
        print()
        paragraphe_92()

# paragraphe 248
def paragraphe_248():

    # système de combat à inclure
    texte=["La créature qui vient de s'éveiller est un FARFADET ! Il se met",
           "péniblement debout, et attrape une corde qui doit probablement",
           "actionner une sonnette d'alarme. Il vous faut l'attaquer vite.",
           "FARFADET HABILETÉ: 6 ENDURANCE: 5"]
    for loop in range(len(texte)):
        print(texte[loop])
        
    print("Vous etes vainqueur, vous pouvez continuer votre chemin le long du passage.")
    choix=input("Appuyer sur entrée pour continuer.") # pour faire une pause
    print()
    paragraphe_301()    

# paragraphe 278
def paragraphe_278():

    texte=["Le passage aboutit bientôt à une porte fermée à clé. Vous collez votre",
           "oreille contre le panneau, mais vous n'entendez rien. Voulez-vous",
           "essayer d'enfoncer la porte ? Vous préférez peut être rebrousser",
           "chemin et retourner au croisement ?"]
    
    for loop in range(len(texte)):
        print(texte[loop])

    choix=input("Choisissez rebrousser ou enfoncer.")

    print()
    if choix=="enfoncer":
        paragraphe_156()
    elif choix=="rebrousser":
        paragraphe_92()

# paragraphe_301
def paragraphe_301():
    print("301 à faire")

# paragraphe_343
def paragraphe_343():
    texte=["La porte s'ouvre à la volée et vous tombez en avant, tête la première.",
           "Vous avez soudain un coup au coeur en réalisant que vous ne tombez",
           "pas sur le sol, mais dans une fosse. Par chance, celle-ci n'est pas très",
           "profonde et vous atterrissez moins de deux mètres plus bas. Vous",
           "perdez 1 point d'ENDURANCE en raison des contusions provoquées",
           "par cette chute, vous vous hissez hors de la fosse, et vous sortez de la",
           "pièce par la porte en prenant la direction de l'ouest. Rendez-vous au 92"]

    for loop in range(len(texte)):
        print(texte[loop])
        
    print("343 endurance à gerer pas fini")

    choix=input("Pour continuer appuyer sur une touche")

    paragraphe_92()    
    
# run
chance=6+random.randint(1,6)
print("Vous avez une chance de :",chance)
print()
# pour tester vite changer de place le #
paragraphe_82()
#paragraphe_rumeurs()
