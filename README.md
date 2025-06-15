# 🛡️ Warden 1.0 – File Security Auditor

**Warden 1.0** est un projet personnel développé en Python, avec une interface graphique moderne construite à l’aide de **Tkinter**.  
Ce logiciel simule un système d’audit de sécurité des fichiers : il analyse un dossier donné, calcule l’empreinte MD5 de chaque fichier, et les compare à une base de données contenant des hachages de virus connus.

---

## 🔍 Fonctionnalités principales

- Interface graphique stylisée (Tkinter + fond personnalisé)
- Analyse récursive de tous les fichiers dans un dossier (y compris sous-dossiers)
- Calcul MD5 pour chaque fichier
- Comparaison avec une liste de hachages signalés comme suspects
- Avertissement visuel si un virus est détecté
- Option de suppression des fichiers détectés comme infectés

---

## 🖥️ Utilisation

### 1. Prérequis

Assurez-vous d’avoir Python 3.9+ installé, ainsi que les bibliothèques suivantes :

```bash
pip install pandas Pillow
```

### 2. Lancer l'application

```bash
python antivirus.py
```

> L’application s’ouvre dans une fenêtre graphique. Elle vous proposera :
> - de scanner un dossier
> - de détecter des virus (via hachages)
> - de supprimer les fichiers infectés

---
## ⚠️ Limitations & évolutions prévues

Ce projet est un **prototype** fonctionnel à but pédagogique. Il n’intègre pas de moteur antivirus réel, mais une logique de comparaison par hachage.

Des améliorations sont prévues :
- Export du projet en `.exe` via PyInstaller (actuellement sur macOS, donc non généré)
- Affichage de logs détaillés dans un fichier
- Intégration de statistiques sur les fichiers scannés
- Interface plus responsive
- Ajout d’un menu de configuration ou d’une zone de sélection de dossier

---

## 💡 Objectif pédagogique

Ce projet a été réalisé dans le cadre d’un apprentissage personnel en cybersécurité et en développement logiciel.  
Il m’a permis de mettre en pratique :

- la gestion de fichiers et répertoires (`os`, `os.walk`)
- le hachage de fichiers (`hashlib`)
- les interactions graphiques (`tkinter`, `messagebox`, `PhotoImage`)
- la manipulation de données avec `pandas`
- la création d’interfaces modernes avec style

---

## 📦 Installation future

Un exécutable `.exe` Windows autonome sera généré via :

```bash
pyinstaller --onefile --windowed --icon=assets/warden.ico antivirus.py
```

---


