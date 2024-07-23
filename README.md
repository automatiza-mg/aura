# SIMA - Sistema de Monitoramento e Automação de Minas Gerais.


## Setup

- Clonar repositário.
- Criar ambiente virtual python e instalar pacotes

```python
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

- Rodar migrações

```python
$ python manage.py migrate
$ python manage.py createsuperuser
```
