import os
from niftystocks import ns
from flask import Flask, render_template, request
from src.pipeline.pipeline import Pipeline
import shutil

app = Flask(__name__)

nifty_200 = ns.get_nifty500_with_ns()

def copy_files(file_list, destination_dir):
    for source_file in file_list:
        try:
            shutil.copy(source_file, destination_dir)
            print(f"File '{source_file}' copied successfully.")
        except Exception as e:
            print(f"Error copying file '{source_file}': {e}")


def start_pipeline(selected_stock):
    pipeline = Pipeline()
    graph_1, graph_2, graph_3 = pipeline.run_pipeline(stock_symbol=selected_stock)
    return graph_1, graph_2, graph_3

@app.route('/')
def index():
    return render_template('index.html', stocks=nifty_200)

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        selected_stock = request.form['stocks']
        graph_1, graph_2, graph_3 = start_pipeline(selected_stock=selected_stock)
        file_list = [graph_1, graph_2, graph_3]
        destination_directory = 'static/'
        copy_files(file_list, destination_directory)
        print("Selected stock:", selected_stock)
        # Pass the paths of the graphs to the template
        return render_template('result.html', stocks=nifty_200, graph_1=str(graph_1), graph_2=str(graph_2), graph_3=str(graph_3))

if __name__ == '__main__':
    app.run(debug=True)



