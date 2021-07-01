import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.LITERA]
app = dash.Dash(__name__,
                meta_tags=[{
                    "name": "viewport",
                    "content": "width=device-width"
                }],
                external_stylesheets=external_stylesheets)
app.title = "Antonio VM - Data Analyst"
server = app.server
# CARDS

card_1 = dbc.Card(
    [
        dbc.CardBody([
            dbc.CardImg(src="assets/Psycovid_project_logo_4.png", top=True),
            html.H4("PsyCovid DS", className="card-title"),
            html.H6("Data Analysis + Machine Learning",
                    className="card-subtitle"),
            html.P(
                "Analisis and Predictions over the Human Emotions based on\
                personality traits and demographical variables.",
                className="card-text"),
            dbc.Button("Go to App",
                       href="https://psycovid-dash.herokuapp.com/",
                       color="primary",
                       block=True),
            # dbc.CardLink("External link", href="https://google.com"),
        ]),
    ],
    # style={"width": "18rem"},
)

card_2 = dbc.Card(
    [
        dbc.CardBody([
            dbc.CardImg(src="assets/antonio_logo_SVG_3.svg", top=True),
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text"),
            dbc.Button("Go to App",
                       href="https://google.com",
                       color="primary",
                       block=True),
            # dbc.CardLink("External link", href="https://google.com"),
        ]),
    ],
    # style={"width": "18rem"},
)

card_3 = dbc.Card(
    [
        dbc.CardBody([
            dbc.CardImg(src="assets/antonio_logo_SVG_3.svg", top=True),
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text"),
            dbc.Button("Go to App",
                       href="https://google.com",
                       color="primary",
                       block=True),
            # dbc.CardLink("External link", href="https://google.com"),
        ]),
    ],
    # style={"width": "18rem"},
)

card_4 = dbc.Card(
    [
        dbc.CardImg(src="assets/antonio_logo_SVG_3.svg", top=True),
        dbc.CardBody([
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text"),
            dbc.Button("Go to App",
                       href="https://google.com",
                       color="primary",
                       block=True),
            # dbc.CardLink("External link", href="https://google.com"),
        ]),
    ],
    # style={"width": "18rem"},
)

card_5 = dbc.Card(
    [
        dbc.CardImg(src="assets/antonio_logo_SVG_3.svg", top=True),
        dbc.CardBody([
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text"),
            dbc.Button("Go to App",
                       href="https://google.com",
                       color="primary",
                       block=True),
            # dbc.CardLink("External link", href="https://google.com"),
        ]),
    ],
    # style={"width": "18rem"},
)

card_6 = dbc.Card(
    [
        dbc.CardImg(src="assets/antonio_logo_SVG_3.svg", top=True),
        dbc.CardBody([
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text"),
            dbc.Button("Go to App",
                       href="https://google.com",
                       color="primary",
                       block=True),
            # dbc.CardLink("External link", href="https://google.com"),
        ]),
    ],
    # style={"width": "18rem"},
)

image_cards_row_1 = dbc.Row([
    dbc.Col(card_1, width={
        'size': 3,
        'offset': 1
    }),
    dbc.Col(card_2, width={
        'size': 3,
        'offset': 1
    }),
    dbc.Col(card_3, width={
        'size': 3,
        'offset': 1
    }),
])

image_cards_row_2 = dbc.Row([
    dbc.Col(card_4, width={
        'size': 3,
        'offset': 1
    }),
    dbc.Col(card_5, width={
        'size': 3,
        'offset': 1
    }),
    dbc.Col(card_6, width={
        'size': 3,
        'offset': 1
    }),
])

app.layout = dbc.Container([
    html.Br(),
    html.Br(),
    dbc.Row(
        dbc.Col(
            [
                html.Img(src=app.get_asset_url('antonio_logo_website_250.png')),

                # width={
                #     "size": 6,
                #     "offset": 3
                # },
            ],
            style=dict(textAlign='center'),
        )),
    html.Br(),
    html.Br(),
    image_cards_row_1,
    image_cards_row_2,
])


if __name__ == "__main__":
    app.run_server(debug=True)