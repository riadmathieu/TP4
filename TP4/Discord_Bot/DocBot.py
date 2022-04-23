# ce que l'on doit importer

import logging
from Log import Log
from discord import Client


class DocBot(Client): # class DocBot
    def __init__(self): #self est le premier argument de la classe
        super().__init__()
        self.log = Log()


    async def on_ready(self): # def on_ready (evenement on_ready)
        print("Hi") # affiche hi
        self.log.infolog(f"{self.user} c'est connecte a Discord!") # confirme que la personne c'est connecte au serveur
        
    async def on_message(self,msg): # on_message(evenemnet on_message)
        print(msg.content)# affiche
        if msg.author != self.user: # si different alors
            self.log.SaveMsg(msg.author,msg.content)
            await msg.channel.send(f"{msg.author} : {msg.content}")
    
        if msg.content == 'Bonjour': # if 'Bonjour'
            await msg.channel.send(f"Salut {msg.author}") # Salut
            self.log.SaveMsg(msg.author,msg.content)



client = DocBot() # classe DocBot
client.run("OTY1MTY4NDEzODQ2NjY3Mjk1.YlvRIQ.k3mqCrYKIpoSN0m3iTHkbvQwx_c") #lancer le client
