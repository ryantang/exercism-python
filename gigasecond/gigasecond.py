from datetime import datetime, timedelta

GIGASECONDS = 1_000_000_000

def add(moment):
    return moment + timedelta(seconds = GIGASECONDS)
