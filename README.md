# Bandersnatch Project

Read the Documentation for information on how to get started.

[Deployed App](https://bandersnatch.herokuapp.com)


### Tech Stack
- Logic: Python3
- API Framework: Flask
- Templates: Jinja2
- Structure: HTML5
- Styling: CSS3
- Database: MongoDB
- Graphs: Altair
- Machine Learning: Scikit
- Hosting: Heroku

### Provided Code
- HTML Templates
- CSS Styles
- API Framework
- Miscellaneous Helper Files
- Sprint Specific Documentation

### Primary Features by URL
- `/`: Splash Page
- `/data`: Tabular Data
- `/view`: Dynamic Visualizations
- `/model`: Interactive Machine Learning Model

### Primary Goals
For best results, complete each sprint in order, before going on to the next sprint.

1. Sprint 1: Database Operations
	- Develop a database interface class
	- Create random data
	- Populate the database with at least 1000 datapoints
2. Sprint 2: Dynamic Visualizations
	- Notebook exploration
	- Chart function
	- API integration
3. Sprint 3: Machine Learning Model
	- Notebook exploration
	- Machine Learning interface class
	- Model serialization (save and open)
	- API model integration

### Stretch Goals
- Use ElephantSQL instead of MongoDB
- Use Plotly instead of Altair
- Use PyTorch instead of Scikit
- Use FastAPI instead of Flask
- Add the ability for the user to reset & reseed the database
- Add the ability for the user to re-train the machine learning model
- Add the ability for the user to download a working serialized model and dataset
- Add authentication to sensitive pages
- Use a different set of features to train the model
- Use your own dataset entirely


### OS Specific Notes: Gunicorn is not Windows compatible!
- Windows users should not use the `run.sh` shell script, as it depends on gunicorn.
- Windows users should use `py -m app.main` to start the app with Flask acting as the server.
- Mac and Linux users can use `./run.sh` script or type the command directly `python3 -m gunicorn app.main:APP`.
- Feel free to modify the shell scripts to suit your needs, these are intended to run locally.
- In any case you should not modify the Procfile, this is the run script for the remote server.
