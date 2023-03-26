import pandas as pd
import json
import requests

def drivers(year):
    # API call
    urlDr = 'http://ergast.com/api/f1/'+str(year)+'/driverStandings.json'
    drivers = requests.request("GET", urlDr)
    drivers = drivers.json()
    
    drivers = drivers['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    pos = []; points = []; name = []; team = []
    for index,value in enumerate(drivers):        
        pos.append(value['positionText'])
        points.append(value['points'])
        name.append(value['Driver']['givenName'] + ' ' + value['Driver']['familyName'])
        team.append(value['Constructors'][0]['name'])

    standings = {'Pos':pos,'Name':name, 'Points':points, 'Constructor':team}

    df = pd.DataFrame(standings)
    return df

def constructors(year):
    # API call
    urlConstr = 'http://ergast.com/api/f1/'+str(year)+'/constructorStandings.json'
    constr = requests.request("GET", urlConstr)
    constr = constr.json()


    constr = constr['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    pos = []; team = []; country = []; points = [];
    for index,value in enumerate(constr):        
                pos.append(value['positionText'])
                team.append(value['Constructor']['name'])
                country.append(value['Constructor']['nationality'])
                points.append(value['points'])

    standings = {'Pos':pos,'Constructor':team, 'Points':points, 'Nationality':country}

    df = pd.DataFrame(standings)
    return df


    


