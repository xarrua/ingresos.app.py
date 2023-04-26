from app_ingresos_gastos import app
from flask import render_template,request,redirect
import csv
from datetime import date

@app.route("/")
def index():
    datos=[]
    #llamada al archivo
    fichero = open('data/movimientos.csv','r')
    #accediendo a cada registro del archivo y lo formatea
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #recorrer el objeto csvReader y cargar cada registro en la lista datos
    for item in csvReader:
        datos.append(item)

    return render_template("index.html",data=datos,title="Lista")

@app.route("/new",methods=["GET","POST"])
def create():
    if request.method == "POST":
        hoy = str(date.today())
       
        if request.form['fecha'] > hoy:
            return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar")

        if request.form['fecha'] <= hoy:
            #acceder al archivo y configurar para cargar un nuevo registro
            mifichero = open('data/movimientos.csv','a',newline='')
            #llamar al metodo writer de escritura y configuramos el formato
            lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
            #registramos los datos recibidos
            lectura.writerow([request.form['fecha'],request.form['concepto'],request.form['monto']])
        
            return redirect("/")  

    else:
        return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar")

@app.route("/update")
def edit():
    return render_template("update.html",title="Actualizar",tipoAccion="Actualización",tipoBoton="Editar")

@app.route("/delete")
def remove():
    return render_template("delete.html",title="Eliminar")    