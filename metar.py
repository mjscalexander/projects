import requests, bs4

def get_aviation_wx(airport):
    res = requests.get('https://www.aviationweather.gov/metar/data?ids={}&format=decoded&date=&hours=0'.format(airport))
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser")
    td_elmt = noStarchSoup.select('td')
    arpt = td_elmt[1].get_text()
    metar_raw = td_elmt[3].get_text()
    temp_label = td_elmt[4].get_text()
    temp_data = td_elmt[5].get_text()
    dewpoint_label = td_elmt[6].get_text()
    dewpoint_data = td_elmt[7].get_text()
    press_alt_label = td_elmt[8].get_text()
    press_alt_data = td_elmt[9].get_text()
    wind_label = td_elmt[10].get_text()
    wind_data = td_elmt[11].get_text()
    visi_label = td_elmt[12].get_text()
    visi_data = td_elmt[13].get_text()
    ceil_label = td_elmt[14].get_text()
    ceil_data = td_elmt[15].get_text()
    cloud_label = td_elmt[16].get_text()
    cloud_data = td_elmt[17].get_text()
    try:
        weather_label = td_elmt[18].get_text()
        weather_data = td_elmt[19].get_text()
    except IndexError:
        pass
    print('\n', "Airport: " + arpt)
    print('\n', metar_raw)
    print('\n', temp_label, temp_data)
    print('\n', dewpoint_label, dewpoint_data)
    print('\n', press_alt_label, press_alt_data)
    print('\n', wind_label, wind_data)
    print('\n', visi_label, visi_data)
    print('\n', ceil_label, ceil_data)
    print('\n', cloud_label, cloud_data)
    try:
        print('\n', weather_label, weather_data)
    except UnboundLocalError:
        pass
airport = input("Please enter airport you wish to get weather for (ie. KORD): ")

if __name__== "__main__":
    get_aviation_wx(airport)
