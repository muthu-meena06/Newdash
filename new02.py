import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc, Input, Output


# Read the temperature data from the CSV file
df = pd.read_csv('C:\\Users\\Lenovo T480\\Downloads\\city_temperature.csv',low_memory=False)

# Create the Dash app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Temperature Data Dashboard'),
    
    # Dropdown for selecting the city
    dcc.Dropdown(
        id='CITY-dropdown',
        options=[{'label': CITY, 'value': CITY} for CITY in df['CITY'].unique()],
        value=df['CITY'].unique()[0],
        multi=True
    ),
    
    # Radio items for selecting the plot type
    dcc.RadioItems(
        id='plot-type',
        options=[
            {'label': 'Line Plot', 'value': 'line'},
            {'label': 'Bar Plot', 'value': 'bar'}
        ],
        value='line',
        labelStyle={'display': 'inline-block'}
    ),
    
    # Graph component for displaying the temperature data
    dcc.Graph(id='temperature-graph')
])

# Define the callback to update the graph based on the selected city and plot type
@app.callback(
    Output('temperature-graph', 'figure'),
    [Input('CITY-dropdown', 'value'),
     Input('plot-type', 'value')]
)
def update_temperature_graph(selected_cities, plot_type):
    # Filter the data based on the selected cities
    filtered_data = df[df['CITY'].isin([selected_cities])]


    # Create the figure based on the selected plot type
    if plot_type == 'line':
        fig = px.line(filtered_data, x='YEAR', y='AVGTEMPERATURE', color='CITY',
                      title='Average Temperature Over Time')
    elif plot_type == 'bar':
        fig = px.bar(filtered_data, x='YEAR', y='AVGTEMPERATURE', color='CITY',
                     title='Average Temperature Comparison')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
