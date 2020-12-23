# LEVANTAMENTO E CARACTERIZAÇÃO DE COLEÇÕES DE DOCUMENTOS PARA MINERAÇÃO DE TEXTOS EM PORTUGUÊS


## Planilha do projeto
A planilha com as bases e artigos analizados do presente projeto está disponibilizada pelo link: [https://docs.google.com/spreadsheets/d/1sGK7D46YxuOJ2xekIbkdXBJv51yQLkQUu4pui3JK9do/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1sGK7D46YxuOJ2xekIbkdXBJv51yQLkQUu4pui3JK9do/edit?usp=sharing)


## Instalação 

Primeiro você precisa criar uma virtual  env:
```
    virtualenv NAME
    source NAME/bin/active
```

Instalar dependecias do projeto
```
 pip3 install -r requirements.txt
```



## preprocess.py 

| Alias | Command      | required | help                   |
|-------|--------------|----------|------------------------|
| -o    | --outpu_dir  | False    | Output data directory  |
| -l    | --language   | False    | Language used in files |
| -d    | --database   | False    | Database name.         |
| -f    | --file       | True     | Csv file               |
| -sw   | --stopwords  | False    | Stopwords list file    | 
|  -cl  | --classes    | True     |  Class list file.      |
|  -sp  | --separator  |  True    |  Separator list file.  | 
|  -vl  | ----value    |  True    |  Column of value.      | 
