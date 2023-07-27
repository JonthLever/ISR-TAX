from flask import Flask, render_template, request, session, redirect, url_for
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.HEX_SEC_KEY

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
#--------------------------------------------------------------------------------------
def calc_less_30(monto_bruto):
    monto_neto=monto_bruto/1.12
    retencion=round(monto_neto*0.05,2)
    return retencion

def calc_greater_30(monto_bruto):    
    monto_neto=monto_bruto/1.12
    retencion=round(((monto_neto-30000)*0.07)+1500,2)
    return retencion

def decider(nm):
    n=round(float(nm),2)
    if n/1.12>2499.99 and n/1.12<30000.00:
        
        return calc_less_30(n)
    elif n/1.12>=30000:
        
        return alc_greater_30(n)
    else:
        return 0.0
#--------------------------------------------------------------------------------------

@app.route('/obtener', methods=['POST'])
def obtener():
    
    monto = request.form['mont']
    reten=decider(monto)
    session["resultado"]=reten
    return render_template('index.html', message="hola")

if __name__ == '__main__':
    app.run(debug=True)
