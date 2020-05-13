# vya-flask

*Prequesite*
- Python 3.7.5 with `pipenv` & `pip` installed
- Text Editor (VSCode, Sublime Text or Notepad nobody cares)

# Install & Setup pipenv
1.  Clone this project
2.  In command line/powershell/terminal: ```pip install pipenv```
3.  Type ```pipenv shell```
4.  Type pipenv install.  This command will install every packages needed to run the project properly.
5.  If the above step failed. Please install these packages manually: flask, praw 
    (Using ```pip install package_name```).
    
# Run Flask:
-   Open cmd/Terminal/Powershell and type `python app.py`.
-   There will be a line that says `Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
-   -> Copy the http address and paste it on your browser, or ctrl-click on the link to go to your page.
-   Go to http://127.0.0.1:5000/reddit and you will receive a sample json string which is the comments  from this submission: 3g1jfi
