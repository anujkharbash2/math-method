from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        a = float(request.json['a'])
        b = float(request.json['b'])

        steps = []
        steps.append(f"Given Equation: {a}x + {b} = 0")

        if a == 0:
            result = "No solution (a should not be zero)"
        else:
            steps.append(f"Step 1: Rearrange the equation → {a}x = {-b}")
            x = -b / a
            steps.append(f"Step 2: Solve for x → x = {-b}/{a}")
            steps.append(f"Final Answer: x = {x}")
            result = f"x = {x}"

        return jsonify({'result': result, 'steps': steps})

    except:
        return jsonify({'result': 'Invalid input', 'steps': []})

if __name__ == '__main__':
    app.run(debug=True)
