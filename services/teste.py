import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, Dash


app = Dash()

progress = html.Div(
    [
        dcc.Interval(id="progress-interval", n_intervals=0, interval=0 * 1000),
        dbc.Progress(id="progress"),
    ]
)

app.layout = progress

@app.callback(
    [Output("progress", "value"), Output("progress", "label")],
    [Input("progress-interval", "n_intervals")],
)
def update_progress(n):
    print(n)
    # check progress of some background process, in this example we'll just
    # use n_intervals constrained to be in 0-100
    progress = min(n % 110, 100)
    # only add text after 5% progress to ensure text isn't squashed too much
    return progress, f"{progress} %" if progress >= 5 else ""



if __name__ == '__main__':
    app.run_server(debug=True)
