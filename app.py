from flask import Flask, render_template, request
import numpy as np
from visualizer import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, visualize_sorting

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualize', methods=['POST'])

#fucntion for the visualization in the website
def visualize():

        algorithm = request.form['algorithm']
        array_size = int(request.form['size'])

        # Generate a random array of the selected size
        arr = np.random.randint(1, 100, array_size)

        #condition of the visualization
        if algorithm == 'bubble':
            visualize_sorting(arr, bubble_sort)
        elif algorithm == 'selection':
            visualize_sorting(arr, selection_sort)
        elif algorithm == 'insertion':
            visualize_sorting(arr, insertion_sort)
        elif algorithm == 'merge':
            visualize_sorting(arr, merge_sort)
        elif algorithm == 'quick':
            visualize_sorting(arr, quick_sort)

        return render_template('index.html', message="Visualization completed successfully!")

if __name__ == '__main__':
    app.run(debug=True)
