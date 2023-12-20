import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Paths to HTML plots and images
paths = {
    'Pres-Mid(585_National)': 'assets/map1.html',  # SSP 585 Global Map 1
    'Pres-End(585_National)': 'assets/map2.html',  # SSP 585 Global Map 2
    'Pres-Mid(245_National)': 'assets/map3.html',  # SSP 245 Global Map 3
    'Pres-End(245_National)': 'assets/map4.html',  # SSP 245 Global Map 4
    'Pres-Mid(585_Regional)': 'assets/State_map_585_1.html',  # SSP 585 State-wise Map 1
    'Pres-End(585_Regional)': 'assets/State_map_585_2.html',  # SSP 585 State-wise Map 2
    'Pres-Mid(245_Regional)': 'assets/State_map_245_1.html',  # SSP 245 State-wise Map 1
    'Pres-End(245_Regional)': 'assets/State_map_245_2.html'   # SSP 245 State-wise Map 2
}

seasonal_paths = {
    'January': {'SSP585': 'assets/decadal_January.png', 'SSP245': 'assets/decadal_January_245.png'},
    'April': {'SSP585': 'assets/decadal_April.png', 'SSP245': 'assets/decadal_April_245.png'},
    'July': {'SSP585': 'assets/decadal_July.png', 'SSP245': 'assets/decadal_July_245.png'},
    'October': {'SSP585': 'assets/decadal_October.png', 'SSP245': 'assets/decadal_October_245.png'}
}

# App layout with two main tabs, nested tabs, and dropdowns
app.layout = html.Div([
    html.H1("Climate Change Assessment & Visualization", style={'textAlign': 'center'}),
    html.P("This project utilizes the AWI-CM 1.1 MR climate model datasets to analyze temperature variations under "
           "two Representative Concentration Pathways (SSP585 and SSP245) across three key decades (Present ("
           "2015-2024), mid-century (2050-2059) and end-century (2090-2099)). Seasonal analysis of specific months "
           "across these periods highlights temporal shifts, while a granular look at global temperature changes "
           "offers insights into regional impacts. The dashboard below synthesizes these findings, providing an "
           "interactive platform for users to visualize climate projections, and enhance decision-making "
           "capabilities in response to climate change challenges."),
    html.P("The dashboard features two primary tabs dedicated to the scenarios SSP 585 and SSP 245. Nested "
           "within these are the 'Seasonal' and 'Global' sub-tabs. Under the 'Seasonal' sub-tab, users can view the "
           "temperature changes for each season—January, April, July, and October—across the three decades. Within "
           "the 'Global' sub-tab, additional nested tabs provide the option to switch between country-wise and "
           "state-wise analysis results, offering a comprehensive overview of the temperature shifts and climate "
           "projections."),
    html.Label(html.B('Choose a Scenario: ')),
    dcc.Tabs([
        dcc.Tab(label='SSP 585', children=[
            html.Br(),
            html.Br(),
            html.Label(html.B('Choose an Analysis: ')),
            dcc.Tabs(id='tabs-585', children=[
                dcc.Tab(label='Seasonal', children=[
                    html.Br(),
                    html.Br(),
                    html.Label(html.B('Choose a Month:')),
                    dcc.Dropdown(
                        id='seasonal-dropdown-585',
                        options=[
                            {'label': 'January', 'value': 'January'},
                            {'label': 'April', 'value': 'April'},
                            {'label': 'July', 'value': 'July'},
                            {'label': 'October', 'value': 'October'}
                        ],
                        value='January'
                    ),
                    html.Br(),
                    html.Br(),
                    html.Div(id='seasonal-content-585', style={'textAlign': 'center'})
                ]),
                dcc.Tab(label='Global', children=[
                    html.Br(),
                    html.Br(),
                    html.Label(html.B('Choose a Scale: ')),
                    dcc.Tabs(id='global-tabs-585', children=[
                        dcc.Tab(label='Country-wise', children=[
                            html.Br(),
                            html.Br(),
                            html.Label(html.B('Choose the Decades for Comparison: ')),
                            dcc.Dropdown(
                                id='country-dropdown-585',
                                options=[
                                    {'label': 'Pres-Mid(585_National)', 'value': 'Pres-Mid(585_National)'},
                                    {'label': 'Pres-End(585_National)', 'value': 'Pres-End(585_National)'}
                                ],
                                value='Pres-Mid(585_National)'
                            ),
                            html.Br(),
                            html.Br(),
                            html.Div(id='country-content-585')
                        ]),
                        dcc.Tab(label='State-wise', children=[
                            html.Br(),
                            html.Br(),
                            html.Label(html.B('Choose the Decades for Comparison: ')),
                            dcc.Dropdown(
                                id='state-dropdown-585',
                                options=[
                                    {'label': 'Pres-Mid(585_Regional)', 'value': 'Pres-Mid(585_Regional)'},
                                    {'label': 'Pres-End(585_Regional)', 'value': 'Pres-End(585_Regional)'}
                                ],
                                value='Pres-Mid(585_Regional)'
                            ),
                            html.Br(),
                            html.Br(),
                            html.Div(id='state-content-585')
                        ])
                    ])
                ])
            ])
        ]),
        dcc.Tab(label='SSP 245', children=[
            html.Br(),
            html.Br(),
            html.Label(html.B('Choose an Analysis: ')),
            dcc.Tabs(id='tabs-245', children=[
                dcc.Tab(label='Seasonal', children=[
                    html.Br(),
                    html.Br(),
                    html.Label(html.B('Choose a Month: ')),
                    dcc.Dropdown(
                        id='seasonal-dropdown-245',
                        options=[
                            {'label': 'January', 'value': 'January'},
                            {'label': 'April', 'value': 'April'},
                            {'label': 'July', 'value': 'July'},
                            {'label': 'October', 'value': 'October'}
                        ],
                        value='January'
                    ),
                    html.Br(),
                    html.Br(),
                    html.Div(id='seasonal-content-245', style={'textAlign': 'center'})
                ]),
                dcc.Tab(label='Global', children=[
                    html.Br(),
                    html.Br(),
                    html.Label(html.B('Choose a Scale: ')),
                    dcc.Tabs(id='global-tabs-245', children=[
                        dcc.Tab(label='Country-wise', children=[
                            html.Br(),
                            html.Br(),
                            html.Label(html.B('Choose the Decades for comparison: ')),
                            dcc.Dropdown(
                                id='country-dropdown-245',
                                options=[
                                    {'label': 'Pres-Mid(245_National)', 'value': 'Pres-Mid(245_National)'},
                                    {'label': 'Pres-End(245_National)', 'value': 'Pres-End(245_National)'}
                                ],
                                value='Pres-Mid(245_National)'
                            ),
                            html.Br(),
                            html.Br(),
                            html.Div(id='country-content-245')
                        ]),
                        dcc.Tab(label='State-wise', children=[
                            html.Br(),
                            html.Br(),
                            html.Label(html.B('Choose the Decades for comparison: ')),
                            dcc.Dropdown(
                                id='state-dropdown-245',
                                options=[
                                    {'label': 'Pres-Mid(245_Regional)', 'value': 'Pres-Mid(245_Regional)'},
                                    {'label': 'Pres-End(245_Regional)', 'value': 'Pres-End(245_Regional)'}
                                ],
                                value='Pres-Mid(245_Regional)'
                            ),
                            html.Br(),
                            html.Br(),
                            html.Div(id='state-content-245')
                        ])
                    ])
                ])
            ])
        ])
    ]),
    html.H3("< Thank you >", style={'textAlign': 'center'}),
])

# Callbacks for updating content based on dropdown selections
@app.callback(
    Output('seasonal-content-585', 'children'),
    [Input('seasonal-dropdown-585', 'value')]
)
def update_seasonal_585(month):
    image_path = seasonal_paths[month]['SSP585']
    return html.Img(src=image_path, style={"height": "2000px", "width": "90%"})

@app.callback(
    Output('seasonal-content-245', 'children'),
    [Input('seasonal-dropdown-245', 'value')]
)
def update_seasonal_245(month):
    image_path = seasonal_paths[month]['SSP245']
    return html.Img(src=image_path, style={"height": "2000px", "width": "90%"})

@app.callback(
    Output('country-content-585', 'children'),
    [Input('country-dropdown-585', 'value')]
)
def update_country_585(value):
    return html.Iframe(srcDoc=open(paths[value], 'r').read(), style={"height": "750px", "width": "100%"})

@app.callback(
    Output('country-content-245', 'children'),
    [Input('country-dropdown-245', 'value')]
)
def update_country_245(value):
    return html.Iframe(srcDoc=open(paths[value], 'r').read(), style={"height": "750px", "width": "100%"})

@app.callback(
    Output('state-content-585', 'children'),
    [Input('state-dropdown-585', 'value')]
)
def update_state_585(value):
    return html.Iframe(srcDoc=open(paths[value], 'r').read(), style={"height": "750px", "width": "100%"})

@app.callback(
    Output('state-content-245', 'children'),
    [Input('state-dropdown-245', 'value')]
)
def update_state_245(value):
    return html.Iframe(srcDoc=open(paths[value], 'r').read(), style={"height": "750px", "width": "100%"})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
