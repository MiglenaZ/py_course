def parse_and_clean(line: str):
    data=line.split('|')
    data_clean = [item.strip() for item in data]
    if len(data_clean) != 5:
        return None
    elif data_clean[-1] != 'ACTIVE':
        return None
    elif 'ERROR' in data_clean or 'N/A' in data_clean:
        return None
    else:
        return data_clean


def celsius_converter(f_temp: str | float):
    if type(f_temp) == str:
        f_temp = float(f_temp)
    
    if type(f_temp) == float:
        c_temp = round((f_temp - 32) / 1.8, 2)
        return c_temp
    else:
        return 'Input not float or str.'

with open('environmental_raw.txt', 'rt') as in_file:
    with open('environmental_clean.txt', 'wt') as out_file:
        corrupt=0
        out_file.write(f'Timestamp, StationID, Temp(C), Humidity(%), Sensor_Status\n')
        for line in in_file:
            data = parse_and_clean(line)
            if data is None:
                corrupt+=1
            else:
                data[2] = celsius_converter(data[2])
                str_data = ''
                for index,item in enumerate(data):
                    str_data += str(item)
                    if index != 4:
                        str_data += ', '
                out_file.write(f'{str_data}\n')
        print(f'Corrupt lines: {corrupt}')