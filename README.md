# F1 Pit Strategy Analyzer 🏎️

A Python-based Formula 1 pit strategy visualization tool that analyzes tire strategies for the 2025 F1 season.

## Features

- **Interactive Race Selection**: Choose from 14 races of the 2025 F1 season
- **Tire Strategy Visualization**: Color-coded tire compounds (Soft, Medium, Hard, Intermediate, Wet)
- **Driver Performance**: Shows strategies sorted by finish position
- **Error Handling**: Robust input validation for race selection

## Technologies Used

- **Python 3.x**
- **FastF1**: Official F1 data analysis library
- **Matplotlib**: Data visualization
- **Pandas**: Data manipulation (via FastF1)

## Installation

1. Clone the repository
2. Install required packages:
```bash
pip install fastf1 matplotlib
```

## Usage

Run the script:
```bash
python pitstops.py
```

1. Select a Grand Prix (1-14)
2. View the tire strategy visualization
3. Analyze pit stop strategies by driver finish position

## Grand Prix List (2025 Season)

1. Australian Grand Prix
2. Chinese Grand Prix
3. Japanese Grand Prix
4. Bahrain Grand Prix
5. Saudi Arabian Grand Prix
6. Miami Grand Prix
7. Emilia Romagna Grand Prix
8. Monaco Grand Prix
9. Spanish Grand Prix
10. Canadian Grand Prix
11. Austrian Grand Prix
12. British Grand Prix
13. Belgian Grand Prix
14. Hungarian Grand Prix
15. Dutch Grand Prix *(upcoming)*
16. Italian Grand Prix *(upcoming)*
17. Azerbaijan Grand Prix *(upcoming)*
18. Singapore Grand Prix *(upcoming)*
19. United States Grand Prix *(upcoming)*
20. Mexican Grand Prix *(upcoming)*
21. São Paulo Grand Prix *(upcoming)*
22. Las Vegas Grand Prix *(upcoming)*
23. Qatar Grand Prix *(upcoming)*
24. Abu Dhabi Grand Prix *(upcoming)*

## Color Coding

- 🔴 **Red**: Soft tires
- 🟡 **Yellow**: Medium tires
- ⚪ **White**: Hard tires
- 🟢 **Green**: Intermediate tires
- 🔵 **Blue**: Wet tires

## How It Works

The script analyzes each driver's lap data to identify tire compound changes (pit stops) and visualizes them as horizontal colored lines. Each driver is positioned vertically according to their finish position, making it easy to correlate strategy with performance.

## Sample Output

The visualization shows:
- X-axis: Lap numbers
- Y-axis: Drivers (ordered by finish position)
- Color-coded horizontal lines representing tire stints

## Data Source

Data is sourced from the official F1 timing system via the FastF1 library, ensuring accuracy and real-time availability.
