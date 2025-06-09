from skyfield.api import load, EarthSatellite

def load_tle_from_lines(name, line1, line2):
    ts = load.timescale()
    return EarthSatellite(line1, line2, name, ts)

with open('data/iss.tle') as f:
    lines = [line.strip() for line in f]
    satellite = load_tle_from_lines(lines[0], lines[1], lines[2])
