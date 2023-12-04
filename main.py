from flask import Flask, render_template, request

app = Flask(__name__,template_folder="templates")

@app.route('/')
def enter_bills():
    return render_template('enter_bills.html')

@app.route('/submit_bill', methods=['POST'])
def submit_bill():
    if request.method == 'POST':
        customer = request.form['customer']
        amount = request.form['amount']
        description = request.form['description']
        
        print(f"Customer: {customer}, Amount: {amount}, Description: {description}")

        return "Bill submitted successfully! Thank you."

if __name__ == '__main__':
    app.run(debug=True)

