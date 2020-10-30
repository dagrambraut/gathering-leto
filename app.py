import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import data
import plotly.graph_objects as go
import pandas as pd


external_style = ["https://eds-static.equinor.com/font/equinor-font.css"]


app = dash.Dash(__name__, external_stylesheets=external_style)


data_issues = data.get_issues("equinor/gathering-leto")


def get_node_value(node, key):
    if key == "user":
        return node.user.login
    return getattr(node, key)


def get_data_dict_keys(data_json_list, keys):
    results = []
    for node in data_json_list:
        d = {str(k): get_node_value(node, k) for k in keys}
        results.append(d)
    return results


def _create_logo():
    return html.Img(
        src="https://eds-static.equinor.com/logo/equinor-logo-primary.svg#red",
        id="logo",
        width=100,
        alt="Equinor",
    )


def _create_table_view_div(data_dict):
    return html.Div(
        [
            dash_table.DataTable(
                id="table",
                columns=[{"name": key, "id": key} for key in data_dict[0].keys()],
                data=data_dict,
            )
        ]
    )


def _create_navbar():
    return html.Div(
        children=[
            html.Nav(
                className="nav nav-pills",
                children=[
                    html.A(
                        "Leto issues",
                        className="nav-item nav-link active btn",
                        href="/",
                    )
                ],
            )
        ]
    )


def _create_bottombar():
    return html.Div(
        children=[
            html.Nav(
                className="bottombar",
                children=[
                    html.P(
                        "Team Leto - copyright 2020",
                    )
                ],
            )
        ]
    )


def _create_activity_plot(issue_data):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            name="Closed",
            x=issue_data["date"],
            y=issue_data["closed"],
            stackgroup="the-one",
        )
    )
    fig.add_trace(
        go.Scatter(
            name="Open",
            x=issue_data["date"],
            y=issue_data["open"],
            stackgroup="the-one",
        )
    )

    return html.Div(
        [
            dcc.Graph(figure=fig),
        ]
    )


keys = [
    "assignee",
    "body",
    "closed_at",
    "closed_by",
    "comments",
    "created_at",
    "id",
    "labels",
    "milestone",
    "pull_request",
    "repository",
    "title",
    "user",
]


def _create_checkboxes_div(key_list):
    return html.Div(
        dcc.Checklist(
            id="input-items",
            options=[{"label": key, "value": key} for key in key_list],
            value=["title", "user"],
        )
    )


app.layout = html.Div(
    [
        _create_logo(),
        _create_navbar(),
        _create_checkboxes_div(keys),
        _create_table_view_div(get_data_dict_keys(data_issues, ["title", "user"])),
        _create_activity_plot(
            data.fetch_issue_activity("equinor/gathering-leto"),
        ),
        _create_bottombar(),
    ]
)


@app.callback(
    dash.dependencies.Output("table", "columns"),
    [dash.dependencies.Input("input-items", "value")],
)
def update_output(value):
    data_dict = get_data_dict_keys(data_issues, value)
    columns = [{"name": key, "id": key} for key in data_dict[0].keys()]
    return columns


@app.callback(
    dash.dependencies.Output("table", "data"),
    [dash.dependencies.Input("input-items", "value")],
)
def update_output(value):
    data_dict = get_data_dict_keys(data_issues, value)
    return data_dict


if __name__ == "__main__":
    app.run_server(debug=True, port=8000, host="0.0.0.0")
