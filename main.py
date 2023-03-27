
import datetime
from dash import Dash, dash_table, html, dcc, Input, Output, State

from displayTable import evaluate

selection = ["Final Season Standings"]
today = datetime.date.today()
currentYear = today.year
year = []
year.extend(range(1960, currentYear+1))
year = [str(i) for i in year] # convert int list to str list

# App Creation
app = Dash(__name__)
app._favicon = ("F1.ico")

app.layout = html.Div([
    html.H1("Welcome to F1 Stats!",style={"textAlign":"center"}),

    html.Div([
        # Sidebar
        html.Div(children=[
            html.Label("What would you like to check?"),
            dcc.Dropdown(selection, id="selectionDD"),

            html.Br(),
            html.Label("Year"),
            dcc.Dropdown(year, id="yearDD"),

            html.Br(),
            html.Br(),
            html.Button("Check", id="button", n_clicks=0, style={"width":"30%", "margin":"auto", "display":"block"}),
        ], style={"padding": 20, "width":"250px"}),

        html.Div(style={"width":"50px"}),

        # Main Window (Placeholder)
        html.Div(id="displayResults", style={"width":"100%", "display": "flex", "flex-direction": "row"})
    ], style={"display": "flex", "flex-direction": "row"})

], style={"display": "flex", "flex-direction": "column"},)

# Callback for pressing the button
@app.callback(
    Output("displayResults", "children"),
    Input("button", "n_clicks"),
    State("selectionDD", "value"),
    State("yearDD", "value")
)

# What happens when the button is clicked
def buttonClick(clicked,selection,year):
    if clicked ==0:
        return None
    else:
        if selection==None or year ==None:
            return 'incorect'
        return evaluate(selection, year)

if __name__ == "__main__":
    app.run_server(debug=True)