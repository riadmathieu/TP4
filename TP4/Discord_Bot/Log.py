# import logging
import logging

class Log(): # declaration de la classe
    def __init__(self): #self est le premier argument de la classe
        logging.basicConfig(filename='l.log', format='%(filename)s: %(message)s', lvl=logging.DEBUG) # on utulise DEBUG pour obtenir des information detailles. C'est utile quand on diagnostique un probleme

    def ErrorMsg(self):
        logging.warning("message d'alerte") # on utulise warning pour dire que quelque chose d'innatendue a eu lieu
    
    
    def infolog(self,messages):
        logging.info(str(messages)) # on utilise info pour dire que tous c'est passé comme prevu
        print(str(messages))

    def SaveMsg(self,auteur,messages):
        logging.debug(str(auteur)+": "+str(messages))
