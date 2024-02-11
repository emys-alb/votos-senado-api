#!/bin/bash

#get scrapper folder
git clone "https://github.com/emys-alb/votos-senado"
cd votos-senado/

# get date time
datetime=$(date '+%m_%d_%Y_%H_%M_%S')
today=$(date "+%d/%m/%Y")
last_monday=$(date -d 'last-monday' '+%d/%m/%Y')
filename="votos.csv"

#define and update enviroment variable
echo -e FILENAME=$filename '\n'INIT_DATE=$last_monday '\n'FINISH_DATE=$today > .env

pipenv shell
pipenv install

#run the spider
cd scrapper/ & python paginas.py