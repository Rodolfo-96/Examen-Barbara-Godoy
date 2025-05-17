from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/descuento.html", methods=["GET", "POST"])
def descuento():
    resultado = None
    if request.method == "POST":
        try:
            nombre= (request.form["nombre"])
            edad = int(request.form["edad"])
            compra = int(request.form["compra"])

            if edad>18 and edad<30:
                desc = 0.15
            elif edad>30 :
                desc = 0.30

            else:
                desc=0
            total_sin=9000*compra
            dcto=total_sin*desc
            total_final=total_sin-dcto
            resultado = {
                "Total_sin_dto": total_sin,
                "Dcto":dcto,
                "Total_con_dto":total_final,
                "Nombre":nombre,
            }
        except ValueError:
            resultado = {"error": "Por favor, ingrese valores numéricos válidos."}

    return render_template("descuento.html", resultado=resultado)

@app.route("/inicio_sesion.html", methods=["GET", "POST"])
def inicio():
    resultado = None
    if request.method == "POST":
        nombre= request.form["nombre"]
        contras= request.form["contrasena"]
        if (nombre=='juan') and (contras=='admin'):
            mensaje="Bienvenido administrador juan"
        elif (nombre=='pepe') and (contras=='user'):
            mensaje="Bienvenido usuario pepe"
        else:
            mensaje="Usuario o contraseña incorrectos"
        resultado={
            "Mensaje": mensaje,
        "Usuario":nombre,
        "Contras":contras,}
    return render_template("inicio_sesion.html", resultado=resultado)

if __name__ == "__main__":
    app.run()