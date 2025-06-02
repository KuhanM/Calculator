from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400
            
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Please enter valid numbers'}), 400

if __name__ == '__main__':
    app.run(debug=True)