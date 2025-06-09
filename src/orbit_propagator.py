from skyfield.api import load

def propagate_orbit(satellite, start_hour=0, duration_minutes=60):
    ts = load.timescale()
    times = ts.utc(2024, 6, 9, range(start_hour * 60, start_hour * 60 + duration_minutes))
    positions = [satellite.at(t).position.km for t in times]
    return positions