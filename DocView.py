
def docView(fileName):

    output = ''
    fileName = fileName.replace('%20', ' ')
    with open(r"Processed/{}.html".format(fileName), "r") as data:
        output = data.read()
        return output