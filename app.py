import dash

# import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dotenv
from pathlib import Path

from models import Person

# from models import *

import time
from subprocess import Popen, PIPE
import multiprocessing

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

dotenv.load_dotenv(dotenv_path=Path(Path.home(), "access", ".dotenv-postgres"))


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.H4(id="app-label"),
        html.Button("Process", id="app-button-process"),
    ]
)


def slow_worker():
    print("Starting worker")
    time.sleep(3)
    print("popen")
    process = Popen(
        'sleep 3 && echo "doing some work" && sleep 1',
        stdout=PIPE,
        stderr=PIPE,
        shell=True,
        encoding="utf-8",
    )
    # wait for process to finish
    stdout, stderr = process.communicate()
    # Create a new entry in DB
    Person.create(name="Bob", birthday="2020-01-02", is_relative=True)
    print("db", Person.select().count())
    print(stdout)
    print(stderr)

    print("done open")
    print("Finished worker")


@app.callback(
    Output("app-label", "children"), [Input("app-button-process", "n_clicks")]
)
def process_data(n_clicks):
    if n_clicks is None:
        return ""

    p = multiprocessing.Process(
        target=slow_worker,
    )
    print("BEFORE:", p, p.is_alive())
    p.start()
    print("DURING:", p, p.is_alive())

    return "done"


if __name__ == "__main__":
    app.run_server(debug=True)
