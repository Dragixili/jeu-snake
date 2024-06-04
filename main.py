import sys,random
import pygame

class jeu:
    #contenir toutes les variablesd ainsi que toutes les fonctions utile pour le bon fonctionnement du jeu
    def __init__(self):
        self.ecran = pygame.display.set_mode((800,600))#taille ecran

        pygame.display.set_caption('jeu snake')#titre jeu
        self.jeu_encours = True#variable pour dire que le jeu est en cours

        #creer les variables de positions et direction du serpent 
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10

        # cree la position pour la pomme

        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,590,10)
        self.pomme = 10

        # fixer les fps

        self.clock = pygame.time.Clock()

        # creer une liste liste qui rescence toutes les positions du serpent

        self.position_serpent = []

        #creer la variable en rapport avce la taille du serpent

        self.taille_du_serpent = 1

        self.ecran_du_début = True

        #charger l'image

        self.image = pygame.image.load('image.jpg')

        #retrecir l'image

        self.image_titre = pygame.transform.scale(self.image,(200,100))

        #creer la variable score

        self.score = 0

    def fonction_principale(self):
        #permet de gerer les elements et d'afficher certain composant du jeu grâce au while loop

        while self.ecran_du_début:
             
             for evenement in pygame.event.get():#recupère les evenement réalisé
                if evenement.type == pygame.QUIT:#si les evenements sont egaux a quitter alors ça quit
                    sys.exit()
                
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:

                        self.ecran_du_début = False
                
                self.ecran.fill((0,0,0))

                self.ecran.blit(self.image_titre,(300,50,100,50))
                self.creer_message('petite','le but du jeu est de faire que le serpent se développe',
                                   (250,200,200,5), (240,240,240))
                self.creer_message('petite','pour cela , il a besoin de pomme ,mangez-en autant que possible !!',
                                   (190, 220, 200,5), (240,240,240))
                self.creer_message('moyenne','Appuyer sur Entrer pour commencer',
                                   (200, 450,200, 5), (255,255,255))

                pygame.display.flip()
             

        while self.jeu_encours:

            for evenement in pygame.event.get():#recupère les evenement réalisé
                if evenement.type == pygame.QUIT:#si les evenements sont egaux a quitter alors ça quit
                    sys.exit()

                #creer les events qui permet de bouger le serpent
                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_RIGHT:
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_LEFT:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_DOWN:
                        self.serpent_direction_y = 10
                        self.serpent_direction_x = 0

                    if evenement.key == pygame.K_UP:
                        self.serpent_direction_y = -10
                        self.serpent_direction_x = 0

            #faire bouger le serpent si il est en dehors de limite

            if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 \
                or self.serpent_position_y <= 100 or self.serpent_position_y >= 600 :

                sys.exit()

            self.serpent_mouvement()

            # cree la cond si le serpent mange la pomme  

            if self.pomme_position_y == self.serpent_position_y and self.pomme_position_x == self.serpent_position_x:


                self.pomme_position_x = random.randrange(110,690,10)
                self.pomme_position_y = random.randrange(110,590,10)


                #augmente la taille du serpent

                self.taille_du_serpent +=1
                #augmenter le score
                self.score += 1

            #creer une liste pour stocker les positions de la tete du serpent

            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)

            # append dans la liste des positions du serpend

            self.position_serpent.append(la_tete_du_serpent)

            # cond pour resoudre le problème des positions du serpent avec la taille du serpent

            if len(self.position_serpent) > self.taille_du_serpent:

                self.position_serpent.pop(0)

            self.afficher_les_éléments()
            self.se_mord(la_tete_du_serpent)

            self.creer_message('grande','Snake Game', (320,10,100,50), (255,255,255))
            self.creer_message('grande','{}'.format(str(self.score)),(375,50,50,50), (255,255,255))


            #affficher les limites
            self.creer_limites()
            self.clock.tick(30)


            pygame.display.flip()#mettre a jour l'ecran

    #creer un fonction qui permet de creer un rectangle qui represente les limites

    def creer_limites(self):

        pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)

    def serpent_mouvement(self):
            
         #faire bouger le serpent
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y

    def afficher_les_éléments(self):
    
            self.ecran.fill((0,0,0))#couleur de l'ecran

            #afficher le serpent
            pygame.draw.rect(self.ecran,(0,255,0),(self.serpent_position_x,self.serpent_position_y,self.serpent_corps,self.serpent_corps))

            #afficher la pomme

            pygame.draw.rect(self.ecran,(255,0,0),(self.pomme_position_x,self.pomme_position_y,self.pomme,self.pomme))

            
            self.afficher_serpent()
            

    def afficher_serpent(self):

        #afficher les autres parties du serpent
        for partie_du_serpent in self.position_serpent:
                pygame.draw.rect(self.ecran,(0,255,0),(partie_du_serpent[0],partie_du_serpent[1],self.serpent_corps,self.serpent_corps))
        

    
    def se_mord(self,la_tete_du_serpent):

        #le serpent se mord
        for partie_du_serpent in self.position_serpent [:-1]:   
            if la_tete_du_serpent == partie_du_serpent:

                sys.exit()   

    #fonction pour afficher les messages

    def creer_message(self,font,message,message_rectangle,couleur):
        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)
        
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message,True,couleur)#permet d'afficher le text

        self.ecran.blit(message,message_rectangle)




if __name__ == '__main__':#permet de lancer le jeu

    pygame.init()
    jeu().fonction_principale()
    pygame.quit()

