Transactions de cartes bancaires (Données réelles)

• Une ligne est une transaction réalisée par une carte.

• Les variables de base sont :

• Le numero de carte

• La date de la transaction

• Le montant

• Le code du pays dans lequel la transaction a été réalisée
• Le code du commercant chez qui la transaction a été réalisée (MCC)
• Code réponse de la demande d’autorisation : 00 = Accepté, les autres codes sont des refus
• La variable fraude permet d’identifier les transactions frauduleuses


COMMENT LIRE NOTRE CODE : 

Les codes dans analyse sont classés de 1 à 3 afin de lire le code dans l'ordre de traitement.

Les modèles étudiés sont dans la partie modélisation.

Les bases de données parquet étant trop lourdes sont ignorées dans le gitignore
