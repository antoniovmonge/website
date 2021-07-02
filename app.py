import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.GRID]
app = dash.Dash(__name__,
                meta_tags=[{
                    "name": "viewport",
                    "content": "width=device-width"
                }],
                external_stylesheets=external_stylesheets)
app.title = "Antonio VM - Data Analyst"
server = app.server

app.layout = dbc.Container([
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Button('LinkedIn',
                       href='https://www.linkedin.com/in/antonio-v-monge/',
                       color='light'),
        ], ),
        dbc.Col([
            dbc.Button('GitHub',
                       href='https://github.com/antoniovmonge',
                       color='light')
        ],
                style=dict(textAlign='right'))
    ]),
    html.Br(),
    dbc.Row(
        dbc.Col(
            [
                # html.Br(),
                # html.Br(),
                html.Img(src=app.get_asset_url('antonio_green.svg')),
            ],
            style=dict(textAlign='center'),
        )),
    # html.Br(),
    # html.Br(),
    dbc.Row([
        dbc.Card(  # CARD 1
            [
                dbc.CardBody([
                    dbc.CardImg(src="assets/Psycovid_logo.svg", top=True),
                    html.H4("PsyCovid DS", className="card-title"),
                    html.H6("Data Analysis + Machine Learning",
                            className="card-subtitle"),
                    html.
                    P("Analysis and Predictions over the Human Emotions based\
                        on personality traits and demographic variables.",
                      className="card-text"),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button(
                                "App",
                                href="https://psycovid-dash.herokuapp.com/",
                                color="primary",
                                # style=dict(margin=15),
                                block=True),
                        ]),
                        dbc.Col([
                            dbc.Button(
                                "Repo",
                                href=
                                "https://github.com/antoniovmonge/psycoviddash",
                                color="primary",
                                # style=dict(marginRight=12),
                                block=True,
                            ),
                        ])
                    ]),
                ]),
            ],
            style={"width": "18rem"},
        ),
        dbc.Card(  # CARD 2
            [
                dbc.CardBody([
                    dbc.CardImg(src="assets/Financial_analysis.svg", top=True),
                    html.H4("Financial Analysis", className="card-title"),
                    html.H6("Data Analysis", className="card-subtitle"),
                    html.Br(),
                    html.P("Project under construction... 😇",
                           className="card-text"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button(
                                "App",
                                href=
                                "https://olist-dash-antonio.herokuapp.com/",
                                color="primary",
                                # style=dict(margin=15),
                                block=True),
                        ]),
                        dbc.Col([
                            dbc.Button(
                                "Repo",
                                href=
                                "https://github.com/antoniovmonge/olist-dash",
                                color="primary",
                                # style=dict(margin=15),
                                block=True,
                            ),
                        ])
                    ]),
                ]),
            ],
            style={"width": "18rem"},
        ),
        dbc.Card(
            [
                dbc.CardBody([
                    dbc.CardImg(src="assets/antonio_green.svg", top=True),
                    html.Br(),
                    html.Br(),
                    html.H4("Comming soon", className="card-title"),
                    html.H6("Card subtitle", className="card-subtitle"),
                    html.Br(),
                    html.P("More projects are coming soon!  :)",
                           className="card-text"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button(
                                "App",
                                href="#",
                                color="primary",
                                # style=dict(margin=15),
                                block=True),
                        ]),
                        dbc.Col([
                            dbc.Button(
                                "Repo",
                                href="#",
                                color="primary",
                                # style=dict(margin=15),
                                block=True,
                            ),
                        ])
                    ]),
                ]),
            ],
            style={"width": "18rem"},
        ),
    ]),
    dbc.Row([
        dbc.Card(
            [
                dbc.CardBody([
                    dbc.CardImg(src="assets/antonio_green.svg", top=True),
                    html.Br(),
                    html.Br(),
                    html.H4("Comming soon", className="card-title"),
                    html.H6("Card subtitle", className="card-subtitle"),
                    html.Br(),
                    html.P("More projects are coming soon!  :)",
                           className="card-text"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button(
                                "App",
                                href="#",
                                color="primary",
                                # style=dict(margin=15),
                                block=True),
                        ]),
                        dbc.Col([
                            dbc.Button(
                                "Repo",
                                href="#",
                                color="primary",
                                # style=dict(margin=15),
                                block=True,
                            ),
                        ])
                    ]),
                ]),
            ],
            style={"width": "18rem"},
        ),
        dbc.Card(
            [
                dbc.CardBody([
                    dbc.CardImg(src="assets/antonio_green.svg", top=True),
                    html.Br(),
                    html.Br(),
                    html.H4("Comming soon", className="card-title"),
                    html.H6("Card subtitle", className="card-subtitle"),
                    html.Br(),
                    html.P("More projects are coming soon!  :)",
                           className="card-text"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button(
                                "App",
                                href="#",
                                color="primary",
                                # style=dict(margin=15),
                                block=True),
                        ]),
                        dbc.Col([
                            dbc.Button(
                                "Repo",
                                href="#",
                                color="primary",
                                # style=dict(margin=15),
                                block=True,
                            ),
                        ])
                    ]),
                ]),
            ],
            style={"width": "18rem"},
        ),
        dbc.Card(
            [
                dbc.CardBody([
                    dbc.CardImg(src="assets/antonio_green.svg", top=True),
                    html.Br(),
                    html.Br(),
                    html.H4("Comming soon", className="card-title"),
                    html.H6("Card subtitle", className="card-subtitle"),
                    html.Br(),
                    html.P("More projects are coming soon!  :)",
                           className="card-text"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button(
                                "App",
                                href="#",
                                color="primary",
                                # style=dict(margin=15),
                                block=True),
                        ]),
                        dbc.Col([
                            dbc.Button(
                                "Repo",
                                href="#",
                                color="primary",
                                # style=dict(margin=15),
                                block=True,
                            ),
                        ])
                    ]),
                ]),
            ],
            style={"width": "18rem"},
        ),
    ])
])


if __name__ == "__main__":
    app.run_server(debug=True)