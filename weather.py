import pyowm


class Weather:
    own = pyowm.OWM('1237be710b874a074192f625ce23a943')

    def __init__(self, nameWithCountryCode):
        self.nameWithCountryCode = nameWithCountryCode

    def temperature(self, own=own):
        degree_sign = u'\N{DEGREE SIGN}'
        temperature = own.weather_at_place(self.nameWithCountryCode).get_weather().get_temperature('celsius')['temp']
        t = f"{temperature}{degree_sign}"
        return t

    def temperatureMax(self, own=own):
        degree_sign = u'\N{DEGREE SIGN}'
        temperatureMax = own.weather_at_place(self.nameWithCountryCode).get_weather().get_temperature('celsius') \
            ['temp_max']
        t = f"{temperatureMax}{degree_sign}"
        return t

    def temperatureMin(self, own=own):
        degree_sign = u'\N{DEGREE SIGN}'
        temperatureMin = own.weather_at_place(self.nameWithCountryCode).get_weather().get_temperature('celsius') \
            ['temp_min']
        t = f"{temperatureMin}{degree_sign}"
        return t

    def wind(self, own=own):
        windSpeed = own.weather_at_place(self.nameWithCountryCode).get_weather().get_wind('meters_sec')['speed']
        w = f"{windSpeed} m/s"
        return w

    def cloudcoverage(self, own=own):
        percentage = own.weather_at_place(self.nameWithCountryCode).get_weather().get_clouds()
        s = f"{percentage}%"
        return s

    def pressure(self, own=own):
        pressure = own.weather_at_place(self.nameWithCountryCode).get_weather().get_pressure()['press']
        p = f"{pressure} HPa"
        return p

    def humidity(self, own=own):
        humidity = own.weather_at_place(self.nameWithCountryCode).get_weather().get_humidity()
        h = f'{humidity}%'
        return h

    def status(self, own=own):
        status = own.weather_at_place(self.nameWithCountryCode).get_weather().get_detailed_status()
        s = f"{status}"
        return s

    def icon(self, own=own):
        percentage = own.weather_at_place(self.nameWithCountryCode).get_weather().get_weather_icon_url()
        return percentage
