#Problème de papier de questions
Une feuille de questions contient 𝑁 questions. Les points attribués à chaque bonne réponse
sont 𝑎. Pour chaque mauvaise réponse, vous perdrez 𝑏 des marques. Trouvez le nombre de
notes différentes qui peuvent être obtenues à l'examen.
Remarque : la note 0 sera attribuée à une question non tentée.

## Format d'entrée
• Première ligne: 𝑇 indiquant le nombre de cas de test. <br>
• Chacune des prochaines 𝑇 lignes : trois nombres entiers séparés par des espaces 𝑁, 𝑎 ,
et 𝑏

## Format de sortie
• Imprimez la réponse à chaque cas de test sur une ligne différente. (Le nombre de notes différentes que l'on peut obtenir à un examen). <br>
<br>
• Contraintes <br>
	1 ≤ 𝑇 ≤ 50 <br>
	1 ≤ 𝑁 ≤ 5 × 103 <br>
	1 ≤ 𝑎, 𝑏  ≤ 20 <br>
<br>
• Entrée d'échantillon <br>
2 <br>
1 4 3 <br>
2 1 1 <br>
<br>
• Sortie d'échantillon <br>
3 <br>
5 <br>
<br>
• Explication <br>
Pour le cas de test 1, vous obtiendrez 0 pour n'avoir tenté aucune question, 4 pour la bonne réponse et -3 pour la mauvaise réponse.
Pour le cas de test 2, vous obtiendrez -2, -1, 0, 1, 2.
