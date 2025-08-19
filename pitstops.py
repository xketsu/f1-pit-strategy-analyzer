"""
F1 Pit Strategy Analyzer
========================
Visualizes tire strategies for Formula 1 races from the 2025 season.
Shows color-coded tire compound usage across race distance for each driver.

"""

from matplotlib import pyplot as plt
from matplotlib import patheffects
import fastf1
import os

# create cache directory
if not os.path.exists('cache'):
    os.makedirs('cache')
fastf1.Cache.enable_cache('cache')

# tire colors
TIRE_COLOR_MAP = {
    "SOFT": "#ff2d2d",          
    "MEDIUM": "#f7e600",        
    "HARD": "#d9d9d9",          
    "INTERMEDIATE": "#00a650",  
    "WET": "#0072ff",           
}

# team colors for driver names
TEAM_COLOR_MAP = {
    "Red Bull Racing": "#003773",
    "Ferrari": "#821729", 
    "Mercedes": "#C8CCCE",
    "McLaren": "#FF6A13",
    "Aston Martin": "#037A68",
    "Haas F1 Team": "#EB0A1E",
    "Alpine": "#F1A7D1",
    "Kick Sauber": "#53FC18",
    "Racing Bulls": "#6667AB",
    "Williams": "#00A0DE"
}

# 2025 grand prix names
GRAND_PRIX_NAMES = [
    "Australian Grand Prix",      # 1
    "Chinese Grand Prix",         # 2
    "Japanese Grand Prix",        # 3
    "Bahrain Grand Prix",         # 4
    "Saudi Arabian Grand Prix",   # 5
    "Miami Grand Prix",           # 6
    "Emilia Romagna Grand Prix",  # 7
    "Monaco Grand Prix",          # 8
    "Spanish Grand Prix",         # 9
    "Canadian Grand Prix",        # 10
    "Austrian Grand Prix",        # 11
    "British Grand Prix",         # 12
    "Belgian Grand Prix",         # 13
    "Hungarian Grand Prix",       # 14
    # "Dutch Grand Prix",         # 15
    # "Italian Grand Prix",       # 16
    # "Azerbaijan Grand Prix",    # 17
    # "Singapore Grand Prix",     # 18
    # "United States Grand Prix", # 19
    # "Mexican Grand Prix",       # 20
    # "São Paulo Grand Prix",     # 21
    # "Las Vegas Grand Prix",     # 22
    # "Qatar Grand Prix",         # 23
    # "Abu Dhabi Grand Prix"      # 24
]

# load session data (year, round, session_type(R=race))
while True:
    try:
        race_number = input("Choose a Grand Prix from the 2025 (1-14): ")
        race_num = int(race_number)
        if 1 <= race_num <= 14:
            break
        else:
            print("Error: Please enter a number between 1 and 14.")
    except ValueError:
        print("Error: Please enter a valid number.")

session = fastf1.get_session(2025, race_num, 'R')  
session.load()

# get grand prix name
grand_prix_name = GRAND_PRIX_NAMES[race_num - 1]

# results
results = session.results.sort_values('Position')
drivers = results['Abbreviation'].tolist()  # driver codes
driver_names = [session.get_driver(d)['LastName'] for d in drivers]

plt.figure(figsize=(12, 7))

for i, drv in enumerate(drivers):
    laps = session.laps.pick_driver(drv)
    if laps.empty:
        continue

    current_compound = None
    stint_start = None

    # draw stint lines for each lap
    for _, lap in laps.iterlaps():
        compound = lap['Compound']
        lap_num = lap['LapNumber']

        if compound != current_compound:
            # draw previous stint line
            if current_compound is not None and stint_start is not None:
                plt.plot([stint_start, lap_num-1], [i, i],
                         color=TIRE_COLOR_MAP.get(current_compound, "black"),
                         linewidth=6, solid_capstyle="butt")
            # start new stint
            current_compound = compound
            stint_start = lap_num

    # draw last stint line
    if current_compound is not None and stint_start is not None:
        last_lap = laps["LapNumber"].max()
        plt.plot([stint_start, last_lap], [i, i],
                 color=TIRE_COLOR_MAP.get(current_compound, "black"),
                 linewidth=6, solid_capstyle="butt")
        

# colored driver names on y-axis
plt.yticks(range(len(drivers)), driver_names)
ax = plt.gca()

# color each driver name according to their team
for i, drv in enumerate(drivers):
    team_name = session.get_driver(drv)['TeamName']
    team_color = TEAM_COLOR_MAP.get(team_name, "black")
    label = ax.get_yticklabels()[i]
    label.set_color(team_color)
    # add black outline around driver names
    label.set_path_effects([patheffects.withStroke(linewidth=1, foreground='black')])

plt.xlabel("Lap Number")
plt.ylabel("Drivers (Finish Order)")
plt.title(f"Pit Strategies by Driver ({grand_prix_name})")
plt.grid(True, linestyle="--", alpha=0.3)
plt.gca().invert_yaxis()


plt.tight_layout()
plt.show()
