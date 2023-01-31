import matplotlib.pyplot as plt
import csv
from datetime import datetime

# zdefiniowanie sciezek dla parsowanych plikow
file_path_1 = "E:\VSC Python\Data_Visualisation_project\sitka_weather_2018_simple.csv"
file_path_2 = "E:\VSC Python\Data_Visualisation_project\death_valley_2018_simple.csv"

# puste listy na parsowane dane
dates1, highs1, lows1, rainfall1 = [], [], [] ,[]
dates2, highs2, lows2, rainfall2 = [], [], [] ,[]
        
# definicja parsera plikow
def parser(file_path, dates, highs, lows, rainfall):
    with open(file_path) as file:
        reader = csv.reader(file)
        header = next(reader)
        date = header.index('DATE')
        tmax = header.index('TMAX')
        tmin = header.index('TMIN')
        rnf = header.index('PRCP')

        #logika parsowania danych z readera csv, uzylem plikow z szkolenia ktore celowo byly z bledem, stad implementacja warunkow do instrukcji
        
        for row in reader:
            current_date = datetime.strptime(row[date], '%Y-%m-%d')
            try:
                high = int(row[tmax])
                low = int(row[tmin])
                rain = float(row[rnf])
            except ValueError:
                print((f'Missing data for {current_date}'))
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                rainfall.append(rain)
        return dates, highs, lows, rainfall
                
    

parser(file_path_1, dates1, highs1, lows1, rainfall1)
parser(file_path_2, dates2, highs2, lows2, rainfall2)

# logika kreslenia wykresow, ja wiem ze sporo boilerplate, ale nie do konca czuje jak dziala metoda subplots, wiec wolalem bezpiecznie do tego podejsc
plt.style.use('seaborn-v0_8')
fig, ((ax1, ax2), (ay1, ay2))= plt.subplots(2, 2)
ax1.plot(dates1, highs1, c='red', alpha=0.5)
ax1.plot(dates1, lows1, c='blue', alpha=0.5)
ax1.set_title('Daily high and low temperatures - 2018\nSitka, AL')
ax1.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.1)

ax2.plot(dates2, highs2, c='red', alpha=0.5)
ax2.plot(dates2, lows2, c='blue', alpha=0.5)
ax2.set_title('Daily high and low temperatures - 2018\nDeath Valley, CA')
ax2.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)

ay1.plot(dates1, rainfall1, c='green', alpha=0.5)
ay1.set_title('Daily rainfall - 2018\nSitka, AL')

ay2.plot(dates2, rainfall2, c='green', alpha=0.5)
ay2.set_title('Daily rainfall - 2018\nDeath Valley, CA')

fig.autofmt_xdate()

ay1.set_xlabel('Dates')
ay2.set_xlabel('Dates')
ax1.set_ylabel('Temperature [F]')
ay1.set_ylabel('Milimeters per m^2')

plt.show()
