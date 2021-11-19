class Weather:

    w_dict = {}
    with open("nyc_weather.csv") as f:
        for line in f:
            tokens = line.split(',')
            day = tokens[0]
            try:
                temperature = int(tokens[1])
                w_dict[day] = temperature
            except:
                print("Invalid temperature. Ignore row")

if __name__ == '__main__':
    w = Weather()
    print(w.w_dict)

    # Temperature on January 9 and January 4
    print("temperature on Jan 9: ", w.w_dict['Jan 9'])
    print("Temperature on Jan 4: ", w.w_dict['Jan 4'])
