# Trace - Étape 1 (Architecture & Repo)

## Binôme
- Benjamin E
- Mathis A

## Stratégie Git
- Trunk-based (branche principale: main)
- Branches courtes: feat/*, test/*, ci/*

## Environnement local
- OS:
- git version:
- python version:
- éditeur:



# Étape 2 - Flask local (lecture fichiers + cache TTL + UI)

## Objectif
- Lire JSON/YAML localement (simulation Blob)
- Endpoints API conformes + cache TTL + UI minimale

## Environnement
- Windows 11
- PowerShell

# Trace - Étape 3 (Tests Flask)

## Objectif
- Couvrir health checks + endpoints API (events/news/faq)
- Tests rapides, reproductibles, sans dépendance Azure

## Outil
- pytest (+ éventuellement pytest-cov)

## Résultats attendus
- Tous les tests passent en local et plus tard en CI

# Trace - Étape 4 (Docker)

## Objectif
- Dockerfile optimisé (slim, non-root)
- Conteneur stateless
- Test local obligatoire

## Environnement
- Windows 11
- Docker Desktop
- docker version:

