# heroku_dash_gdal_test

This repo has a working example of deploying a dash app (by plotly) with geopandas and all related dependencies (gdal, fiona, shapely) to heroku.

Important points for building a geopandas/gdal dependent conda environment  
a. Install geopandas and dependencies with conda  
b. Install pip into conda environment  
d. Install dash and related plotly pakcages with pip (into conda environment)  
e. Install gunicorn and geopandas using both conda and pip  

Steps for successfully deploying geopandas and dependencies to heroku:
1. conda env export > environment.yml (with working conda env activated, test locally first)
2. pip freeze > requirements.txt (while in active conda environment)
3. clean up two package dependency files.  Environment.yml and requirements.txt will have repeated package dependencies.  This is 
 both unnecessary and problematic for deployment to heroku (despite working fine locally).  Repeated packages lead to a bloated slug size which exceeded the 500 mb slug limit on heroku.  Repeated packages also caused a number of failure modes during deployment. With both files open, compare and remove repeated packages from the requirements.txt.  NOTE: leave geopandas and gunicorn in both pip and conda requirements.
 4. Create new heroku app
 5. Add two buildpacks to heroku app: https://github.com/heroku/heroku-buildpack-apt, and default python buildpack.  
 
 MISC: The working app also had a conda buildpack: https://github.com/conda/conda-buildpack.git, however this is likely unnecessary.  If problems arise during future deployment, re-add this buildpack
