import dash
import dash_core_components as dcc
import dash_html_components as html
import geopandas as gpd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# data source
shp = 'shp/planimetrics_2016_centerline_trails.shp'
df = gpd.read_file(shp)
columns = list(df.columns.values)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''


app.layout = html.Div([
    dcc.Markdown(children=markdown_text),
    html.Div(children=columns),
    html.Div(children='hello geopandas')
])

if __name__ == '__main__':
    app.run_server(debug=True)
