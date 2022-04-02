import requests
dls = "https://drive.google.com/uc?export=download&id=1f4Z89sdriZhEdVSVtC2zQz5qS-J3R2Py"
response = requests.get(dls)

with open('foreign-holdings-in-brazil-chart.csv', 'wb') as output:
    output.write(response.content)
