# JP Multimarcas - Revendas

Sistema web de gerenciamento de revendas de carros, desenvolvido com Django, uWSGI e Nginx.

🔒 A aplicação é servida com HTTPS usando certificados gratuitos do Let's Encrypt, e está disponível via domínio DuckDNS:  
**https://jpmultimarcas-revendas.duckdns.org**

---

## 🧰 Tecnologias Utilizadas

- Python 3
- Django
- uWSGI
- Nginx
- PostgreSQL (ou outro banco suportado pelo Django)
- DuckDNS
- Certbot (Let's Encrypt)

---

## 🚀 Deploy em Produção (com HTTPS)

### Estrutura do Projeto

```
/var/www/carros/
├── carros/                 # Projeto Django
├── venv/                  # Ambiente virtual Python
├── carros-uwsgi.ini       # Configuração do uWSGI
└── deploy.sh              # Script de deploy automático
```

### Etapas de Instalação no Servidor

1. **Atualizar IP no DuckDNS**
   > DuckDNS precisa apontar para o IP público da máquina (exemplo: `13.218.1.228`)
   ```bash
   curl "https://www.duckdns.org/update?domains=jpmultimarcas-revendas&token=SEU_TOKEN_AQUI&ip=13.218.1.228"
   ```

2. **Instalar Certbot (HTTPS via Let's Encrypt)**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d jpmultimarcas-revendas.duckdns.org
   ```

3. **Configurar uWSGI (`carros-uwsgi.ini`)**
   ```ini
   [uwsgi]
   chdir           = /var/www/carros
   module          = carros.wsgi:application
   master          = true
   processes       = 5
   socket          = /run/uwsgi/carros.sock
   chmod-socket    = 660
   vacuum          = true
   die-on-term     = true
   env             = DJANGO_SETTINGS_MODULE=carros.settings
   ```

4. **Configurar Nginx (`/etc/nginx/sites-available/carros`)**
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
   }
   ```

5. **Reiniciar Nginx**
   ```bash
   sudo systemctl restart nginx
   ```

---

## 💻 Deploy Automático

Criamos um script `deploy.sh` que automatiza todo o processo:

```bash
#!/bin/bash

echo "🚀 Iniciando deploy do Django..."

PROJECT_DIR="/var/www/carros"
VENV_DIR="$PROJECT_DIR/venv"

cd $PROJECT_DIR
source $VENV_DIR/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

touch $PROJECT_DIR/carros/wsgi.py

echo "✅ Deploy concluído com sucesso!"
```

Torne executável e rode sempre que precisar atualizar:

```bash
chmod +x deploy.sh
./deploy.sh
```

---

## ✅ Acesso

Acesse o sistema online em:  
🔗 [https://jpmultimarcas-revendas.duckdns.org](https://jpmultimarcas-revendas.duckdns.org)

---

## 👨‍🔧 Manutenção

- **Atualizar certificado SSL (se necessário)**:
  ```bash
  sudo certbot renew
  ```

- **Verificar logs**:
  ```bash
  sudo journalctl -u nginx
  sudo journalctl -u uwsgi
  tail -f /var/log/nginx/error.log
  ```

---
