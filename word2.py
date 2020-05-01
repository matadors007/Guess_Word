import sys
import random
import os

#créer une liste 
words=['banana','lemon'] 

#fonction pour vider le terminal ded nouveau
def clear():
    if (os.name=='nt'):
        os.system('cls')
    else:
        os.system('clear')

#fonction d'affichage
def draw(failed,Sucess,goal):
    clear()
    print('strikes {} /7 .'.format(len(failed))) #affiche un message
    print('')

    for lettre in failed :  #afficher les lettres fauts 
        print(lettre,end='')

    print('\n\n')


    for lettre in goal:    #afficher les lettres vrais
        if lettre in Sucess:
            print(lettre,end='')
        else:
            print('_',end='')
        
        
#fonction pour les propositions
def get_guess(failed,Sucess):
    while True:
        print('')
        guess=input(" Guess a lettre : ").lower()
        
        if(len(guess)!=1):
            print("you can only guess a single lettre :") #test pour donner un seule lettre pas plus
            continue
        elif ((guess in failed) or (guess in Sucess)): #test pour la repetition de  proposition
            print("You already guess that lettre")
            continue 
        elif not guess.isalpha:
            print('You can only guess lettre') 
        else:
            return guess

def play(done):
    clear()
    goal=random.choice(words) #choisir un mot au hazard de la liste
    failed =[]#liste pour les lettres fauts
    Sucess =[]#liste pour les lettres vrais

    while True:
        draw(failed,Sucess,goal)
        guess=get_guess(failed,Sucess)

        if(guess in goal):#test si le proposition vrai ajouter dans la liste des lettres vrais
            Sucess.append(guess)
            found=True
            for lettre in goal: #test si les lettres qui composent le mot cherché est comme les lettres vrais 
                if lettre not in Sucess:
                    found=False
            if found: #test si les tests tous vrais afficher you win
                print ('you win ')
                print('the secret word was {} '.format(goal))
                done=True
        else:  #test d'ajouter les lettres fauts dans la liste des lettres fauts
            failed.append(guess)
            if(len(failed)==7): #test si la longeur de liste est depasse 7 elements pour tester si il est passer le nbre de fois de donner des propositions
                draw(failed,Sucess,goal)

                print("you lost") 
                print('the secret word was {} '.format(goal))
                done=True

        if done: #done est un variable de la resultat finale et de le jeu se termine
            play_again=input('play again [y/n]').lower() #msg affiché

            if(play_again != 'n'): #test si le joueur veut  jouer une autre fois il suffit de composé la lettre diffeent de "n" pour rejouer le jeu
                return play(done=False)
            else:
                sys.exit() #terminer le jeu

#fonction de bienvenue 
def welcome():
    start= input('Press Enter To Start Or Q to exit ').lower()#msg affiché
    if(start=='q'): #si le joueur ne veut pas jouer il suffit de composer la lettre "Q"
        print('GoodBye')
        sys.exit()
    else: #si il compose n'importe quelle touche il passe au jeu
        return True
        


print('welcome to  lettre game ! ')
done=False
while True:
    clear()
    welcome()
    play(done)