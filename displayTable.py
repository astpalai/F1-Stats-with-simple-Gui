import pandas as pd
import getStandings as getSt

from dash import dash_table, html


def evaluate(selection, year):

    match selection:
        case "Final Season Standings":
            drSt = getSt.drivers(year)
            constSt = getSt.constructors(year)
            result = [
                html.Div(children=[
                html.H2("Driver Standings",style={"textAlign":"center", "padding": 5}),
                dash_table.DataTable(drSt.to_dict("records")),
                ]),

                html.Div(style={"width":"25px"}),

                html.Div(children=[
                    html.H2("Constructors Standings",style={"textAlign":"center", "padding": 5}),
                    dash_table.DataTable(constSt.to_dict("records"))
                ])
            ]
            
        case "2":
            pass
    return result
