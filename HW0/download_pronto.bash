mkdir pronto
cd pronto
touch README.txt
"This directory contains, among other things, a folder of data from pronto bike share. It contains four csv files including bike status data, station data, individual trip data, and daily weather data." >> README.txt
mkdir data
cd data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head 2015_trip_data.csv


