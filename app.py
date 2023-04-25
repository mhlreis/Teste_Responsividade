from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def faz_calculo():
    print('Tratador de requisição.')
    if request.method == 'POST':
        print('Tratanto um post.')
        valx = request.form['valor_x']
        valy = request.form['valor_y']
        valz = request.form['valor_z']
        total = ((int(valx)*2)+(int(valy)+2)+(int(valz)+2))
        return "O valor é: " + str(total)
    else:
        return render_template("formulario.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)