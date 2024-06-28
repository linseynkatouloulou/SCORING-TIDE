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



EXPLICATION

Le code nettoyage_data sert a nettoyer les data pour qu'on utilise un dataframe clean des le debut. Il est ensuite sauvergarder dans un parquet (comme un csv) mais que tu ne verra pas car je l'ai pas push sur github. C'est en lancant le code data_exploration que le fichier est utilisé. Si tu veux continuer lance donc d'abord nettoyage_data puis tu pourras travailler sur data_exploration.

____

quelles variables conisèdere t-on comme catégorielles ? j'hesite pour les fm 

Je me suis inspirée du tp. Pour la partie multivariée a par une matrice de corrélation et nuage de point, je ne vois pas ce qu'on peut faire de plus 

Aussi pour fm_difference je ne vois rien de pertinent à faire

_____

