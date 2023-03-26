import pandas as pd

from dash import dash_table, html


def evaluate(selection, year):

    # Testing Response
    response = {'MRData': {'xmlns': 'http://ergast.com/mrd/1.5', 'series': 'f1', 'url': 'http://ergast.com/api/f1/2000/constructors.json', 'limit': '30', 'offset': '0', 'total': '11', 'ConstructorTable': {'season': '2000', 'Constructors': [{'constructorId': 'arrows', 'url': 'http://en.wikipedia.org/wiki/Arrows_Grand_Prix_International', 'name': 'Arrows', 'nationality': 'British'}, {'constructorId': 'bar', 'url': 'http://en.wikipedia.org/wiki/British_American_Racing', 'name': 'BAR', 'nationality': 'British'}, {'constructorId': 'benetton', 'url': 'http://en.wikipedia.org/wiki/Benetton_Formula', 'name': 'Benetton', 'nationality': 'Italian'}, {'constructorId': 'ferrari', 'url': 'http://en.wikipedia.org/wiki/Scuderia_Ferrari', 'name': 'Ferrari', 'nationality': 'Italian'}, {'constructorId': 'jaguar', 'url': 'http://en.wikipedia.org/wiki/Jaguar_Racing', 'name': 'Jaguar', 'nationality': 'British'}, {'constructorId': 'jordan', 'url': 'http://en.wikipedia.org/wiki/Jordan_Grand_Prix', 'name': 'Jordan', 'nationality': 'Irish'}, {'constructorId': 'mclaren', 'url': 'http://en.wikipedia.org/wiki/McLaren', 'name': 'McLaren', 'nationality': 'British'}, {'constructorId': 'minardi', 'url': 'http://en.wikipedia.org/wiki/Minardi', 'name': 'Minardi', 'nationality': 'Italian'}, {'constructorId': 'prost', 'url': 'http://en.wikipedia.org/wiki/Prost_Grand_Prix', 'name': 'Prost', 'nationality': 'French'}, {'constructorId': 'sauber', 'url': 'http://en.wikipedia.org/wiki/Sauber', 'name': 'Sauber', 'nationality': 'Swiss'}, {'constructorId': 'williams', 'url': 'http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering', 'name': 'Williams', 'nationality': 'British'}]}}}
    response = response['MRData']['ConstructorTable']['Constructors']

    df = pd.DataFrame(response)
    df = df.drop(['constructorId', 'url'], axis=1)
    df = df.rename(columns={"name":"Name", "nationality":"Nationality"})
    
    # THIS IS HOW I MUST RETURN AS TO GET ACCURATE RESULTS
    children = [
    dash_table.DataTable(df.to_dict('records')),
    html.Button("Check", id="button2", n_clicks=0, style={"width":"75%", "align":"center"}),  
    ]
    return children