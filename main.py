from flask import Flask, escape, request, make_response, render_template
from os import listdir
import SearchFunction as sf
import DocView as dv


app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home_template.html')

@app.route('/search')  
def searchPage():
    return render_template('search_template.html')

@app.route('/search-results')
def resultsPage():
    query = request.args.get('term', 'oletus')
    return sf.searchFunc(query)

@app.route('/file.view')
def docView():
    query = request.args.get('document', 'oletus')
    return dv.docView(query)

@app.route('/sr-style.css')
def srStyle():
    output = ''
    with open(r'sr-style.css','r') as data:
        output = data.read()
    return output

@app.route('/file.select')
def fileSelect():
    output = '<head><link rel="stylesheet" type="text/css" href="sr-style.css"> <title>TextMind Stored Entries</title> </head><body>'
    output = output + '<h3> Currently stored entires: </h3>'
    files = listdir(r"Processed//")
    for file in files:
        if file[-5:] == ".html":
            file = file[:-5]
            url = file.replace(' ', '%20')
            output = output + '<a href=/file.view?document={}>{}</a>'.format(url,file) + '<br>'
    output = output + '</body'
    return output


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
