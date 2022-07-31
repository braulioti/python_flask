import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=d6cde4f149e0a054f1718c410c9ea56e"

resposta = urllib.request.urlopen(url)
dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])
