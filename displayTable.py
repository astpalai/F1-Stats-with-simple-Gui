import pandas as pd
import getStandings as getSt

from dash import dash_table, html


def evaluate(selection, year):

    match selection:
        case "Final Season Standings":
            drSt = getSt.drivers(year)
            constSt = getSt.constructors(year)
            children = [
            dash_table.DataTable(drSt.to_dict("records")),
            dash_table.DataTable(constSt.to_dict("records"))
            ]
            
        case "2":
            pass
    return children
