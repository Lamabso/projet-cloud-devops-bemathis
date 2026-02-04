# 1) Base image slim (réduit la taille)
FROM python:3.11-slim

# 2) Bonnes pratiques Python en conteneur
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3) Dossier de travail
WORKDIR /app

# 4) Créer un utilisateur non-root
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# 5) Installer les dépendances (en optimisant le cache Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copier le code (et les data locales utilisées en dev/tests)
COPY app ./app
COPY data ./data

# 7) Permissions
RUN chown -R appuser:appgroup /app
USER appuser

# 8) Port exposé
EXPOSE 8080

# 9) Commande de démarrage (serveur prod)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app.main:create_app()"]
