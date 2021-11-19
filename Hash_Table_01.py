class Weather:

    arr = []
    with open("nyc_weather.csv") as f:
        for line in f:
            token = line.split(',')
            try:
                temperature = int(token[1])
                arr.append(temperature)
            except:
                print("Invalid temperature. Ignore row")


if __name__ == '__main__':
    w = Weather()
    print(w.arr)

    # Average temperature in first week of Jan
    avg_temp = sum(w.arr[0:7])/ len(w.arr[0:7])
    print("Average Temperature: ", avg_temp)

    # Maximum temperature in 1st 10 days of January
    max_temp = max(w.arr[0:10])
    print("Maximum temperature: ", max_temp)