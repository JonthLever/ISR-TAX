from flask import Flask, render_template, request
from datetime import datetime

def get_current_date():
    current_date = datetime.today().date()
    formatted_date = current_date.strftime("%Y-%m-%d")
    return formatted_date

# Example usage
current_date = get_current_date()

app = Flask(__name__,template_folder="templates")

@app.route('/')
def page():
    return home_page()

@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/enter_bills')
def enter_bills():
    return render_template('enter_bills.html')

@app.route('/submit_bill', methods=['POST'])
def submit_bill():
    if request.method == 'POST':
        vendor = request.form['vendor']
        amount = request.form['amount']
        description = request.form['description']
        
        print(f"Customer: {vendor}, Amount: {amount}, Description: {description}")

        return "Bill submitted successfully! Thank you."
    
    
@app.route('/submit_invoice', methods=['POST'])
def submit_invoice():
    if request.method == 'POST':
        costumer = request.form['costumer']
        #amount = request.form['amount']
        #description = request.form['description']
        
        #print(f"Customer: {costumer}, Amount: {amount}, Description: {description}")

        return "Invoice submitted successfully! Thank you."
    
@app.route('/enter_invoice')
def enter_invoice():
    return render_template('enter_invoice.html', datetoday=current_date)    

@app.route('/receive_data', methods=['POST'])
def receive_data():
    table_data = []
    for value in request.form.items():
        table_data.append(value)
    print(table_data)  

    return "Data received successfully"
if __name__ == '__main__':
    app.run(debug=True)

