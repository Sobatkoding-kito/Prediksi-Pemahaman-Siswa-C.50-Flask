from flask import Flask, redirect, url_for, render_template, request, jsonify 
import pandas as pd
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

BASE_URL = "http://127.0.0.1:5000/"

# dataSiswa = pd.read_csv("tbl_data_latih.csv", sep = ';', encoding = 'UTF-8')
appName = ''

@app.route('/')
def index():
    dr = {'BASE_URL' : BASE_URL}
    return render_template('home.html', dRes=dr)

@app.route('/data-siswa')
def data_siswa():
    dSiswa = []
    dataSiswa = pd.read_csv("tbl_data_latih.csv", sep = ';', encoding = 'UTF-8')
    dtnp = dataSiswa.to_numpy()
    # print(dtnp)
    ord = 1
    for x in dtnp:
        dSatuan = {}
        dSatuan['nama'] = x[2]
        dSatuan['ord'] = ord
        ord += 1
        dSiswa.append(dSatuan)
        # print(x[2])
    dtnp = []
    dr = {'dataSiswa' : dSiswa}
    # print(dSiswa)
    return render_template('data-siswa.html', dataSiswa=dSiswa)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)