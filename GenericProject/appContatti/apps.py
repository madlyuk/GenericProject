"""
Specifiche APP:
 - serve un modello per il form in modo da poter gestire a backoffice le richieste
 - il modello va pensato anche con un campo parent_id per le successive risposte
 - nella prima fase verrà proposto un form semplice
 - evolvere il form con la possibilità di poter specificare nell'oggetto
        > una richiesta generica
        > iscrizione ad un corso --> deve essere valorizzato l'id del corso
        > richiesta informazioni su un corso non trovato
 - in una futura evoluzione va previsto un sistema di notifiche di questo tipo:
        > notifica admin (opzionale) all'invio di una richiesta
        > notifica user al suo invio di una richiesta
        > possibilità di rispondere per mail direttamente da area admin
        > le risposte devono essere inserite come "figlie" della richiesta sfruttando un parent_id
"""

from django.apps import AppConfig

class AppcontattiConfig(AppConfig):
    name = 'appContatti'
