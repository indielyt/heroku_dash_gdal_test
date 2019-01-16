import dash
import dash_core_components as dcc
import dash_html_components as html
import geopandas as gpd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# data sources
shp = 'shp/shptest.shp'
df = gpd.read_file(shp)
columns = list(df.columns.values)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

markdown_text = '''
### baker gdal test

Flood Risk Dashboard V1 referenced static geospatial files 
created as 'prebaked' query results.  

Geopandas is an open source geospatial library built on the c library GDAL.
With geopandas up and running, we should be able to query a .shp file on the 
cloud platform.  This allows a wider range of user defined queries to be visualized.

For example, weighting for flood risk scoring can be defined by the user and results are
computed on the fly.  A second example would be sociovulnerability attributes driving the visualization.
Interactive querying, rather than static files, can allow one .shp file to drive [hundreds] of different 
visualizations of the same dataset.
'''


app.layout = html.Div([
    dcc.Markdown(children=markdown_text),
    html.Div(children=columns),
    html.Div(children='hello geopandas')
])

if __name__ == '__main__':
    app.run_server(debug=True)

