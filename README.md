# 🚗 Projeto Carros - Django

Este projeto é um sistema de gerenciamento de carros (revenda) desenvolvido com Django e Flet, com deploy em servidor Linux utilizando Nginx, uWSGI e Let's Encrypt.

---

### ✅ Funcionalidades

- Cadastro, edição e exclusão de carros
- Autenticação de usuários com backends personalizados
- Interface web com Django Admin
- Interface mobile com Flet (via OpenAI API)

---

### 🛠️ Tecnologias utilizadas

- **Backend:** Python, Django
- **Servidor Web:** Nginx + uWSGI
- **Deploy:** Ubuntu Server + DuckDNS + HTTPS (Let's Encrypt)
- **Mobile App:** Flet + Flutter (build Android)

---

### 🌐 Acesso ao sistema

Sistema em produção (com HTTPS):\
🔗 [https://jpmultimarcas-revendas.duckdns.org](https://jpmultimarcas-revendas.duckdns.org)

---

### 📁 Estrutura do Projeto

```
carros/
├── accounts/                 # App de autenticação e usuários
│   ├── templates/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── auth_backends.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── app/                      # Configurações principais do projeto
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
├── cars/                     # App principal para gerenciamento de carros
│   ├── templates/
│   ├── migrations/
│   ├── templatetags/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── media/                    # Arquivos de mídia (uploads)
├── openai_api/               # Provável integração com OpenAI (ex: Flet App)
├── static/                   # Arquivos estáticos (CSS, JS, imagens)
├── staticfiles/              # Pasta de coleta de arquivos estáticos para produção
├── templates/                # Templates base do projeto
├── venv/                     # Ambiente virtual Python
└── manage.py
```

---


### 🧪 Como rodar localmente

```bash
# Clone o projeto
$ git clone https://github.com/seu-usuario/carros.git

# Acesse o diretório
$ cd carros

# Crie e ative o ambiente virtual
$ python3 -m venv venv
$ source venv/bin/activate

# Instale as dependências
$ pip install -r requirements.txt

# Rode as migrações
$ python manage.py migrate

# Crie um superusuário (admin)
$ python manage.py createsuperuser

# Rode o servidor
$ python manage.py runserver
```

---

### ⚙️ Deploy no Ubuntu com DuckDNS + Nginx + HTTPS

1. **Atualize seu IP no DuckDNS**

```bash
curl "https://www.duckdns.org/update?domains=jpmultimarcas-revendas&token=SEU_TOKEN&ip=SEU_IP"
```

2. **Instale e configure o Certbot para HTTPS**

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d jpmultimarcas-revendas.duckdns.org
```

3. **Configure o uWSGI** (`carros-uwsgi.ini`):

```ini
[uwsgi]
module = app.wsgi:application
master = true
processes = 5
socket = /run/uwsgi/carros.sock
chmod-socket = 660
vacuum = true
die-on-term = true
env = DJANGO_SETTINGS_MODULE=app.settings
```

4. **Configure o Nginx** (`/etc/nginx/sites-available/carros`):

```nginx
server {
    listen 80;
    server_name jpmultimarcas-revendas.duckdns.org;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name jpmultimarcas-revendas.duckdns.org;

    ssl_certificate /etc/letsencrypt/live/jpmultimarcas-revendas.duckdns.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/jpmultimarcas-revendas.duckdns.org/privkey.pem;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/run/uwsgi/carros.sock;
    }

    location /static/ {
        alias /var/www/carros/static/;
    }

    location /media/ {
        alias /var/www/carros/media/;
    }
}
```

5. **Recarregue os serviços**

```bash
sudo systemctl restart nginx
sudo systemctl restart uwsgi
```

---

### 🔐 Segurança

- Nenhuma `SECRET_KEY`, token do DuckDNS ou variável sensível está neste repositório.
- `.env` e configurações sensíveis devem ser mantidas no servidor e ignoradas no Git.
- Adicione ao `.gitignore`:

```
venv/
*.pyc
__pycache__/
*.sqlite3
.env
```

---


### 📦 Autor

Feito por [Johnn].



# 🚗 Cars Project - Django Application (English Version)

This is a Django-based project designed to manage car dealership operations. It includes user authentication, car registration, and an administration interface integrated with Django Admin.

## 🌐 Live Domain

Application running at: [https://jpmultimarcas-revendas.duckdns.org](https://jpmultimarcas-revendas.duckdns.org)

---

## 🛠️ Tech Stack
- Python 3.11+
- Django 5+
- SQLite (development database)
- Nginx (reverse proxy)
- uWSGI (application server)
- Certbot + Let's Encrypt (HTTPS support)

---

## 📁 Project Structure

```
CARKROS/
├── accounts/               # Handles user authentication
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── auth_backends.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── app/                   # Core project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── cars/                  # Cars app: manages cars and related data
│   ├── migrations/
│   ├── templates/
│   ├── templatetags/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/                 # Uploaded media files
├── openai_api/            # (Optional) AI integration module
├── static/                # Static assets
├── staticfiles/           # Collected static files
├── templates/             # Global templates
├── venv/                  # Virtual environment (excluded from Git)
```

---

## 🚀 Deployment Summary

1. **Secure your production secret key**  
   Generate a secure key using:
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

2. **DNS Configuration**  
   Configure your domain on [DuckDNS](https://www.duckdns.org):
   - Chosen subdomain: `jpmultimarcas-revendas`
   - Update DuckDNS with your EC2 public IP using:
     ```bash
     curl "https://www.duckdns.org/update?domains=jpmultimarcas-revendas&token=YOUR_TOKEN&ip=YOUR_PUBLIC_IP"
     ```

3. **HTTPS Setup with Certbot**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx
   ```
   - Choose the correct domain when prompted.

4. **Systemd and uWSGI**
   Configure a `carros-uwsgi.ini` and service file to keep your app running.

5. **Firewall and Ports**
   Allow HTTP (80) and HTTPS (443) on your server.

---

## 📦 Install & Run

```bash
# Clone repository
$ git clone https://github.com/your-user/your-repo.git
$ cd your-repo

# Create virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run migrations
$ python manage.py migrate

# Create superuser (optional)
$ python manage.py createsuperuser

# Collect static files
$ python manage.py collectstatic

# Run locally
$ python manage.py runserver
```

---

## 🔐 Notes on Security

Avoid publishing secrets in `README.md`. Make sure to:
- **Ignore `.env` or `settings.py` in `.gitignore`** if they contain secrets
- **Use environment variables** in production
- **Never expose private DuckDNS or Certbot tokens**

---

## 📬 Contact
If you have any questions or suggestions, feel free to open an issue or contact the maintainer.

