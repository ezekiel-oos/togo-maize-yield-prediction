# Prédiction du rendement du maïs au Togo (1961–2024)

Analyse et prédiction du rendement agricole du maïs au Togo à partir de données 
historiques FAOSTAT, avec comparaison de modèles Machine Learning.

---

## 🎯 Objectif

Analyser l'évolution du rendement du maïs au Togo sur 64 ans et construire 
un modèle de prédiction capable d'estimer le rendement futur (kg/ha).

---

## 📊 Données

- **Source** : FAOSTAT (FAO, Nations Unies)
- **Période** : 1961 à 2024 — 64 observations
- **Variable cible** : Rendement en kg/ha
- **Variable prédictive** : Année

---

## 🛠️ Outils utilisés

- Python, Pandas, NumPy
- Matplotlib (visualisation)
- Scikit-learn (Machine Learning)
- Plotly Dash (dashboard interactif)
- Google Colab

---

## 🤖 Modèles comparés

| Modèle | MAE (kg/ha) | R² |
|---|---|---|
| Régression linéaire | 173.92 | 0.36 |
| **Random Forest** | **98.79** | **0.74** |

➡️ Le Random Forest réduit l'erreur de **43%** par rapport à la régression linéaire.

---

## 📈 Résultats clés

- Tendance haussière confirmée sur 64 ans
- Rendement moyen : 1 019 kg/ha
- Meilleur modèle : Random Forest (R² = 0.74)
- Dashboard interactif permettant de prédire le rendement jusqu'en 2035

---

## 🚀 Dashboard interactif

Le fichier `dashboard.py` contient un dashboard Plotly Dash avec :
- Graphique interactif du rendement réel vs prédit
- Slider pour prédire les années 2025–2035
- Affichage dynamique de la prédiction

Pour lancer le dashboard localement :
```bash
pip install dash plotly pandas scikit-learn
python dashboard.py
```
Accès sur `http://127.0.0.1:8050/`

---

## ⚠️ Limites et améliorations possibles

Le modèle utilise uniquement l'année comme variable prédictive.  
Des améliorations sont possibles en ajoutant :
- Pluviométrie annuelle
- Consommation d'engrais
- Politiques agricoles nationales
- Séries temporelles (ARIMA / Prophet)

---

## 👤 Auteur

**Ezekiel Hoffer Koffi** — Analyste de données, Lomé, Togo  
GitHub : [github.com/ezekiel-oos](https://github.com/ezekiel-oos)
