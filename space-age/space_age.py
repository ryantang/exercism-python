class SpaceAge:

    SECONDS_TO_EARTH_YEAR = 31557600
    ORBITAL_PERIOD_EARTH_YEARS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds
        self.years = seconds / SpaceAge.SECONDS_TO_EARTH_YEAR


    def on_earth(self):
        return round(self.years, 2)
    
    def on_mercury(self):
        raw_years = self.years / SpaceAge.ORBITAL_PERIOD_EARTH_YEARS['mercury']
        return round(raw_years, 2)
    
    def on_venus(self):
        raw_years = self.years / SpaceAge.ORBITAL_PERIOD_EARTH_YEARS['venus']
        return round(raw_years, 2)

    def on_mars(self):
        raw_years = self.years / SpaceAge.ORBITAL_PERIOD_EARTH_YEARS['mars']
        return round(raw_years, 2)
    
    def on_jupiter(self):
        raw_years = self.years / SpaceAge.ORBITAL_PERIOD_EARTH_YEARS['jupiter']
        return round(raw_years, 2)
    
    def on_uranus(self):
        raw_years = self.years / SpaceAge.ORBITAL_PERIOD_EARTH_YEARS['uranus']
        return round(raw_years, 2)

    def on_saturn(self):
        raw_years = self.years / SpaceAge.ORBITAL_PERIOD_EARTH_YEARS['saturn']
        return round(raw_years, 2)

    def on_neptune(self):
        raw_years = self.years / SpaceAge.ORBITAL_PERIOD_EARTH_YEARS['neptune']
        return round(raw_years, 2)