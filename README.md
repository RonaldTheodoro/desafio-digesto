# Desafio Digesto


## Instruções de instalação
```
$ git clone git@github.com:RonaldTheodoro/desafio-digesto.git
$ cd desafio-digesto
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```

Caso voce use o pipenv
```
$ git clone git@github.com:RonaldTheodoro/desafio-digesto.git
$ cd desafio-digesto
$ pipenv install
$ pipenv shell
```

## Baixando as informações
```
$ python main.py --down
```

## Selecionando os sites
```
$ python main.py --down --service digitalocean
```

## Salvando os registros no banco de dados
```
$ python main.py --down --save
```

## Exibindo os dados salvos
```
$ python main.py --show
```

## Excluindo todos os dados
```
$ python main.py --delete
```

## Exibindo os argumentos aceitos
```
$ python main.py -h
```