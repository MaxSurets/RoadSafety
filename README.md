# RoadSafety

After cloning this repository, navigate to the root of the project. Make sure you have Node and NPM installed.

Type:
`cd frontend`  
`npm install`  

When that finishes, type:
`npm start`


In order to have access to the ZIP code feature, you would need to start the server locally. We have our database set up on Google Cloud, so you can access it as well to test.   
We have data for only zip codes 9001-9003 and 07410 due to MapBox free tier constraints.  

Make sure you have pip installed for the next steps.

Open a new terminal window and type the following to create a virtual environment called '`env`':  
`python3 -m venv env`

Activate the environment:   
On macOS and Linux:  
`source env/bin/activate`

On Windows:  
`.\env\Scripts\activate`

To install the required packages, type:  
`pip install -r requirements.txt`  


To start the server, type the following:
`cd road_safety`  
`python manage.py runserver`

Now you should be able to use the zip code search!
