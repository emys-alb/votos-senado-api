#!/bin/bash

#get scrapper folder
git clone "https://github.com/emys-alb/votos-senado"
cd votos-senado/

pipenv shell
pipenv install

# get date time
datetime=$(date '+%m_%d_%Y_%H_%M_%S')
today=$(date "+%d/%m/%Y")
last_monday=$(date -d 'last-monday' '+%d/%m/%Y')
filename="novosvotos.csv"

#define and update enviroment variable
cp .env.sample .env
echo -e FILENAME=$filename '\n'INIT_DATE=$last_monday '\n'FINISH_DATE=$today > .env

#run the spider
cd scrapper/
python paginas.py

#check if new file is empty
cd ../out/
wc -c < "$filename"

if [ ! -s "$filename" ]; then
echo "The file $filename is empty."
fi