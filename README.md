# SIF - System Information Financial:
## _Forma simples e rápida para se obter dados financeiros._

## O que é o SIF:
SIF é uma aplicação Desktop feita em totalmente em Python e desenhada em clean architecture, utilizando-se de requisições de alguns sites para obter dados de Ações e Opções.

## Objetivo: 
Este trabalho tem como objetivo atender a necessidade do trabalho de conclusão de curso do MBA - Data Science e analytics pela PECE POLI.

## Motivação:
Sendo que a motivação principal é o fato da dificuldade de obter dados financeiras de forma rápida e consolidada para Ações e Opções. 

## Requerimentos:
SIF necessita de Python 3.10 ou superior para rodar.
Instale todas dependêcias a partir do requirements.txt usando o comando abaixo.



```sh
pip install -r /your_path/SIF_System_information_financial/requirements.txt
```

OBS: De preferencia instale em um ambiente virtual separado para não ter conflitos de dependências.

## Forma de uso:
- **Rodar direto no terminal**

```sh
python app.py
```

- **Criando uma aplicação**

Instale o pyinstaller 

```sh
pip install pyinstaller
```

Rode o seguinte comando dentro da pasta que contém o app.py
```sh
pyinstaller -F --add-data "icon.ico;." --icon=icon.ico --windowed "app.py"
```

Será criado um executável na pasta dentro da pasta dist.
