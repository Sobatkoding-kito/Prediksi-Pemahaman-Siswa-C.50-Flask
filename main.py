from flask import Flask, redirect, url_for, render_template, request, jsonify 
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from sklearn import tree
from sklearn.tree import export_text
from sklearn.tree import DecisionTreeClassifier
import graphviz

app = Flask(__name__)

# dataSiswa = pd.read_csv("tbl_data_latih.csv", sep = ';', encoding = 'UTF-8')

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)