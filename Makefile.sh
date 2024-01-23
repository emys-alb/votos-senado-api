#!/bin/bash

# get date time
datetime=$(date '+%m_%d_%Y_%H_%M_%S')
today=$(date  "+%d/%m/%Y")
last_monday=$(date -d 'last-monday' '+%d/%m/%Y')

#get scrapper folder
git clone "https://github.com/emys-alb/votos-senado"
cd votos-senado/

pipenv shell

#define enviroment variable
cp .env.sample .env
filename="out/novosvotos.csv"

export FILENAME=S(filename) INIT_DATE=$(last_monday) LAST_DATE=$(today)

cd scrapper/

#run the spider
python scrapper.paginas.py