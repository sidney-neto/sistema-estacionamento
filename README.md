## Sistema de Estacionamento em Django
Sistema de estacionamento para gerenciamento de entrada e saída de veículos e cálculo de diárias.

## Instalação
Clone este repositório.
```
git clone https://github.com/sidney-neto/sistema-estacionamento.git
```

### Crie um Virutal Environment
Após o clone, crie um ambiente virtual e instale os requisitos.

```
$ cd sistema-estacionamento
$ virtualenv -p python3.7 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Executar migrações
```
python manage.py migrate
```

## Iniciar Server
```
python manage.py runserver
```

## Demonstração no Heroku
- [Sistema de Estacionamento no Heroku](http://sistema-estacionamento.herokuapp.com/)
