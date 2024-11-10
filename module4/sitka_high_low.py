import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

def read_weather_data(filename):
    """
    Reads dates, high temperatures, and low temperatures from the CSV file.
    """
    dates, highs, lows = [], [], []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Extract data from the CSV file
            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    high = int(row[5])
                    low = int(row[6])
                except ValueError:
                    # Skip rows with missing or invalid data
                    continue
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    return dates, highs, lows

def plot_data(dates, temperatures, title, color):
    """
    Plots the temperature data using Matplotlib.
    """
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'

    dates, highs, lows = read_weather_data(filename)

    while True:
        print("\nWeather Data Viewer")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")
        choice = input("Select an option (1, 2, or 3): ")

        if choice == '1':
            plot_data(dates, highs, "Daily High Temperatures - 2018", 'red')
        elif choice == '2':
            plot_data(dates, lows, "Daily Low Temperatures - 2018", 'blue')
        elif choice == '3':
            print("Exiting program. Thank you!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
