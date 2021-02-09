from bottle import Bottle, run

app = Bottle()

@app.route('/')
def bonjour():
    return "Bonjour !"
    
    
from bottle import template

@app.route('/hello/<name>') #le chemin est ici, ensuite on tape dans le navigateur l'url plus ça pour accéder à la question
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

 
from bottle import request
 
@app.get("/formulaire")
def afficher_formulaire():
    return """
        <form action="/formulaire" method="post">
            Texte1 <input name="parametre1" type="text" />
            <input value="Ajouter" type="submit" />
        </form>
    """
    
@app.post("/formulaire")
def traiter_formulaire():
    valeur = request.forms.get("parametre1")
    return valeur
    

@app.get("/formulaire2")
def afficher_formulaire():
    return """
        <form action="/formulaire2" method="post">
            Chiffre <input name="parametre2" type="text" />
            <br>
            <input value="Ajouter" type="submit" />
        </form>
    """
    
@app.post("/formulaire2")
def traiter_formulaire():
    valeur = request.forms.get("parametre2")
    print(valeur.split(";"))
    valeur2 = valeur.split(";")
    valeur3 = [float(i.replace(",",".")) for i in valeur2]
    return str(valeur3)
  

@app.get("/fonction")
def afficher_formulaire():
    return """
        <form action="/fonction" method="post">
            Chiffre <input name="parametre2" type="text" />
            <br>
            NomFonction <input name="fname" type="text" />
            <br>
            <input value="Ajouter" type="submit" />
        </form>
    """
    
@app.post("/fonction")
def traiter_formulaire():
    valeur = request.forms.get("parametre2")
    print(valeur.split(";"))
    valeur2 = valeur.split(";")
    valeur3 = [float(i.replace(",",".")) for i in valeur2]   


    fname = request.forms.get("fname")
    dic = {'Somme' : sum}
    print(dic)
    return str(dic[fname](valeur3))