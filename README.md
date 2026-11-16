# Projet QA — Tests manuels et automatisation sur LocaVélo

Dans le cadre de ma formation en test logiciel (ENI), j'ai mené une campagne complète de recette sur **LocaVélo**, une application web de location de vélos. L'objectif était de vérifier le bon fonctionnement du site de bout en bout, de suivre les anomalies dans **Jira**, puis d'automatiser les cas de test principaux avec **Python et Selenium**.

---

## Démarche suivie

1. **Recette manuelle (V1.0) :** J'ai exécuté les 40 cas de test du cahier de recette (`LocaVelo_plan_de_recette.xlsx`) sur Google Chrome : validation des champs, calcul des tarifs, remise de 10 %, codes promo et accessibilité (navigation clavier, lecteur d'écran **VoiceOver** sur macOS et mesure des contrastes RGAA).
2. **Suivi des bugs (Jira) :** Pour chaque écart constaté, j'ai ouvert un ticket d'anomalie détaillé dans mon projet Jira (`LOC`) et relié sa référence dans mon cahier de recette.
3. **Retest (V1.1) :** J'ai rejoué les cas en échec sur la version corrigée (`?v=1.1`). Les 4 anomalies principales étant toujours présentes, j'ai maintenu les tickets ouverts et émis un avis **No-Go** pour la mise en production.
4. **Automatisation (Python + Selenium) :** J'ai écrit le script `test_locavelo.py` pour rejouer automatiquement les scénarios clés avec les mêmes données que mon cahier manuel (`TC-01`, `TC-02`, `TC-07` et `TC-26`).

---

## Bilan des anomalies relevées (Jira)

| Ticket | Cas de test | Anomalie constatée | Résultat retest V1.1 |
| :--- | :--- | :--- | :--- |
| **`LOC-1`** | `TC-09` | Une adresse e-mail sans point dans le domaine (`jean.dupont@exemple`) est acceptée. | Non corrigé (Ouvert) |
| **`LOC-2`** | `TC-19` | Une location de `15 jours` est validée alors que le maximum autorisé est de `14 jours`. | Non corrigé (Ouvert) |
| **`LOC-3`** | `TC-26` | La remise de 10 % ne s'applique pas à `7 jours` pile (`84,00 €` affichés au lieu de `75,60 €`). | Non corrigé (Ouvert) |
| **`TC-38`** | `TC-38` | Contraste insuffisant (`2,05:1` au lieu de `4,5:1` minimum) sur le texte d'aide *(RGAA 3.2)*. | Non corrigé (Ouvert) |

---

## Contenu du dossier

- `index.html` : L'application locale LocaVélo.
- `LocaVelo_plan_de_recette.xlsx` : Mon cahier de recette complété (`V1.0` et `V1.1`).
- `test_locavelo.py` : Mon script de tests automatisés avec Selenium.

---

## Lancer les tests automatisés

1. Installer Selenium :
   ```bash
   pip3 install selenium
   ```
2. Exécuter le script :
   ```bash
   python3 test_locavelo.py
   ```
## Aperçu du suivi Jira
![Tableau Jira LocaVelo](capture_Jira.png)
