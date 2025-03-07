from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def row_echelon(A):
    rows, cols = A.shape
    steps = []

    for i in range(min(rows, cols)):
       # check if the dignl elmt is 0
        if A[i, i] == 0:
            for j in range(i + 1, rows):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]  #this is for swapping rows
                    steps.append(f"Swapped Row {i+1} with Row {j+1}")
                    break

       
        if A[i, i] != 0:
            factor = A[i, i]
            A[i] = A[i] / factor
            steps.append(f"Row {i+1} divided by {factor}")

      
        for j in range(i + 1, rows):
            if A[j, i] != 0:
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
                steps.append(f"Row {j+1} → Row {j+1} - ({factor}) * Row {i+1}")

    return A, steps

@app.route('/echelon', methods=['POST'])
def echelon():
    try:
        matrix = request.json['matrix']
        A = np.array(matrix, dtype=float)

        echelon_matrix, steps = row_echelon(A)
        echelon_list = echelon_matrix.tolist()

        return jsonify({'result': echelon_list, 'steps': steps})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
