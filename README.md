```
'##::::'##:'##:::'##::::::::::'##::'#######::'########:::::'########::'########::
 ###::'###:. ##:'##::::::::::: ##:'##.... ##: ##.... ##:::: ##.... ##: ##.... ##:
 ####'####::. ####:::::::::::: ##: ##:::: ##: ##:::: ##:::: ##:::: ##: ##:::: ##:
 ## ### ##:::. ##::::::::::::: ##: ##:::: ##: ########::::: ##:::: ##: ########::
 ##. #: ##:::: ##:::::::'##::: ##: ##:::: ##: ##.... ##:::: ##:::: ##: ##.... ##:
 ##:.:: ##:::: ##::::::: ##::: ##: ##:::: ##: ##:::: ##:::: ##:::: ##: ##:::: ##:
 ##:::: ##:::: ##:::::::. ######::. #######:: ########::::: ########:: ########::
..:::::..:::::..:::::::::......::::.......:::........::::::........:::........:::
```

## 🏗️ Estrutura


```

MyJobDB
 ├── README.md
 ├── queries
 │   └── phone_number.sql
 ├── scripts
 │   └── create_tables.py
 └── tables
     └── 001_phone_number.sql
     
```


### 𝄜  tables

Diretório para colocar todos os scripts sql de criação de tables.

O nome do arquivo deve seguir o padrão:

```
001_phone_number.sql
 │  └── Nome da tabela que será separado por underscore "_"
 │
Número do arquivo que será incrementado a cada novo arquivo para identificarmos a ordem.
```

### 🔎  queries

Diretório para colocar todos os scripts sql que envolve consultas(SELECT) e modificações da tabela(UPDATE, INSERT, DELETE).

O nome do arquivo basicamente será o nome da tabela envolvida:

### 🛠️ scripts

É um diretório de utilitários usando o Python como linguagem de programação.

O arquivo `create_tables.py` basicamente irá unir todos os arquivos que estão dentro do diretório `tables` em um só script sql

## 👨🏻‍💻 Fluxo de trabalho

Para trabalharmos em equipe, será usado algumas funcionalidades que do Git e do Github que são usados por empresas:

1. Crie uma branch a partir da branch `main`
2. Faça os commits que forem necessário
3. Faça o push para o Github
4. Abra uma pull request
5. Selecione a sua branch e faça com que ela aponte para a branch `main`
6. Chame alguém para revisar e então aprovar a pull request e fazer o merge


### Como criar uma branch a partir da main?

Execute esses comandos:

```shell
git checkout main
```
```shell
git pull origin main
```
```shell
git checkout -b "NOME_DA_SUA_BRANCH"
```

### Como realizar um commit?

[https://youtu.be/rRL9lm-a4ms?feature=shared](https://youtu.be/rRL9lm-a4ms?feature=shared)

### Como criar um pull request?

[https://youtu.be/HCdnqjsSyRc?feature=shared](https://youtu.be/HCdnqjsSyRc?feature=shared)
