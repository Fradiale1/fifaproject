# olympics/load_data.py

import pandas as pd
from olympicproject.olympics.models import Airline, Airplane, fifa


def load_data():
    olympic_athletes_df = pd.read_csv('olympic_athletes.csv')
    olympic_hosts_df = pd.read_csv('olympic_hosts.csv')
    olympic_medals_df = pd.read_csv('olympic_medals.csv')
    olympic_results_df = pd.read_csv('olympic_results.csv')

    #for _, row in olympic_athletes_df.iterrows():
    #    Airline.objects.create(id=row['id'], name=row['name'], country=row['country'])

    #for _, row in airplanes_df.iterrows():
    #    Airplane.objects.create(id=row['id'], model=row['model'], capacity=row['capacity'])

    #for _, row in olympics_df.iterrows():
    #    fifa.objects.create(fifa_number=row['fifa_number'], airline=row['airline'],
    #                          destination=row['destination'], departure_date=row['departure_date'])