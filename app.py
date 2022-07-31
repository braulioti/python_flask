from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

frutas = []
registros = []

@app.route('/', methods=["GET", "POST"])
def principal():
    # frutas = ["Morango", "Uva", "Laranja", "Mamão", "Maçã", "Pêra", "Melão", "Abacaxi"]
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    # notas = {"Fulano": 5.0, "Beltrano": 6.0, "Aluno": 7.0, "Sicrano": 8.5, "Rodrigo": 9.5}
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
    return render_template("sobre.html", registros=registros)

@app.route('/filmes/<propriedade>', methods=["GET", "POST"])
def filmes(propriedade):
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=d6cde4f149e0a054f1718c410c9ea56e"
    elif propriedade == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=d6cde4f149e0a054f1718c410c9ea56e"
    elif propriedade == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=d6cde4f149e0a054f1718c410c9ea56e"
    elif propriedade == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&primary_release_year=2014&api_key=d6cde4f149e0a054f1718c410c9ea56e"
    elif propriedade == 'tom_cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=d6cde4f149e0a054f1718c410c9ea56e"


    resposta = urllib.request.urlopen(url)
    dados = resposta.read()

    jsondata = json.loads(dados)

    return render_template("filmes.html", filmes=jsondata['results'])
