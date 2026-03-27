# django-istat-deploy

Wrapper Django pronto per il cloud che espone `django-istat-italian-places`
come public REST API, deployato su **Koyeb** con CI via GitHub Actions.

## Endpoint

| Endpoint | Descrizione |
|---|---|
| `GET /health/` | Healthcheck |
| `GET /comuni-italiani/` | Indice API |
| `GET /comuni-italiani/regioni/` | Elenco regioni |
| `GET /comuni-italiani/province/` | Elenco province |
| `GET /comuni-italiani/comuni/` | Elenco comuni (paginato) |

## Setup locale

```bash
git clone https://github.com/TUO_USER/django-istat-deploy
cd django-istat-deploy
docker compose up --build -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py import_istat_data --force
```

L'API è disponibile su http://localhost:8000.

## Deploy su Koyeb

### 1. Crea il database

Nel [Koyeb dashboard](https://app.koyeb.com):
**Databases → Create Database Service** → regione Frankfurt consigliata.
Copia la `DATABASE_URL` fornita.

### 2. Crea il web service

**Services → Create Web Service → GitHub** → seleziona questo repo.

| Campo | Valore |
|---|---|
| Builder | Dockerfile |
| Branch | `main` |
| Port | `8000` |
| Health check path | `/health/` |
| Run command | `sh -c "python manage.py migrate --noinput && python manage.py import_istat_data --force && gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2 --timeout 120"` |

### 3. Environment variables

| Variabile | Valore |
|---|---|
| `DJANGO_SECRET_KEY` | `python -c "import secrets; print(secrets.token_urlsafe(50))"` |
| `DATABASE_URL` | stringa copiata dal DB Koyeb |
| `ALLOWED_HOSTS` | `.koyeb.app` |

### 4. CI/CD

Koyeb rideploya automaticamente ad ogni push su `main`.
Il workflow CI su GitHub Actions fa lint + Docker build check prima.

## Throttling

Rate limiting via DRF `AnonRateThrottle`.
Formato `THROTTLE_ANON_RATE`: `N/second|minute|hour|day`.
Risposta al limite: `429 Too Many Requests` + header `Retry-After`.
