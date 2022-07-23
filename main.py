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

appName = 'Pemahaman Siswa C.50'

@app.route('/')
def index():
    dr = {'BASE_URL' : BASE_URL}
    return render_template('home.html', dRes=dr)


@app.route('/data-siswa')
def data_siswa():
    dSiswa = []
    dataSiswa = pd.read_csv("tbl_data_latih.csv", sep = ';', encoding = 'UTF-8')
    dtnp = dataSiswa.to_numpy()
    ord = 1
    for x in dtnp:
        dSatuan = {}
        dSatuan['nama'] = x[2]
        dSatuan['ord'] = ord
        dSatuan['kelas'] = x[3]
        dSatuan['penyampaian_materi'] = x[4]
        dSatuan['media_pembelajaran'] = x[5]
        dSatuan['suasana_belajar'] = x[6]
        dSatuan['tugas'] = x[7]
        dSatuan['kehadiran'] = x[8]
        dSatuan['praktikum'] = x[9]
        dSatuan['uts' ] = x[10]
        dSatuan['uas'] = x[11]
        dSatuan['matematika'] = x[12]
        dSatuan['b_indo'] = x[13]
        dSatuan['b_inggris'] = x[14]
        dSatuan['pemahaman'] = x[15]
        ord += 1
        dSiswa.append(dSatuan)
    dtnp = []
    return render_template('data-siswa.html', dataSiswa=dSiswa)


@app.route('/data-latih')
def data_latih():
    dSiswa = []
    dataSiswa = pd.read_csv("tbl_data_latih.csv", sep = ';', encoding = 'UTF-8')
    dataSiswa.replace({'penyampaian_materi':{'Serius Santai':4, 'Serius':3, 'Santai':2, 'Membosankan':1}},inplace=True)
    dataSiswa.replace({'media_pembelajaran':{'EBOOK':5, 'PPT':4, 'Video':3, 'PPT':2, 'PDF':1}},inplace=True)
    dataSiswa.replace({'suasana_belajar':{'Mendukung':4, 'Tidak Mendukung':1}},inplace=True)
    dataSiswa.replace({'tugas':{'Sangat Baik':4, 'Baik':3, 'Cukup':2, 'Kurang':1}},inplace=True)
    dataSiswa.replace({'kehadiran':{'Sangat Baik':4, 'Baik':3, 'Cukup':2}},inplace=True)
    dataSiswa.replace({'praktikum':{'Sangat Baik':4, 'Baik':3, 'Cukup':2, 'Kurang':1}},inplace=True)
    dataSiswa.replace({'uts':{'Sangat Baik':4, 'Baik':3, 'Cukup':2, 'Kurang':1}},inplace=True)
    dataSiswa.replace({'uas':{'Sangat Baik':4, 'Baik':3, 'Cukup':2, 'Kurang':1}},inplace=True)
    dataSiswa.replace({'matematika':{'Sangat Baik':4, 'Baik':3, 'Cukup':2, 'Kurang':1}},inplace=True)
    dataSiswa.replace({'bindo':{'Sangat Baik':4, 'Baik':3, 'Cukup':2, 'Kurang':1}},inplace=True)
    dataSiswa.replace({'bing':{'Sangat Baik':4, 'Baik':3, 'Cukup':2, 'Kurang':1}},inplace=True)
    dtnp = dataSiswa.to_numpy()
    ord = 1
    for x in dtnp:
        dSatuan = {}
        dSatuan['nama'] = x[2]
        dSatuan['ord'] = ord
        dSatuan['kelas'] = x[3]
        dSatuan['penyampaian_materi'] = x[4]
        dSatuan['media_pembelajaran'] = x[5]
        dSatuan['suasana_belajar'] = x[6]
        dSatuan['tugas'] = x[7]
        dSatuan['kehadiran'] = x[8]
        dSatuan['praktikum'] = x[9]
        dSatuan['uts' ] = x[10]
        dSatuan['uas'] = x[11]
        dSatuan['matematika'] = x[12]
        dSatuan['b_indo'] = x[13]
        dSatuan['b_inggris'] = x[14]
        dSatuan['pemahaman'] = x[15]
        ord += 1
        dSiswa.append(dSatuan)
    dtnp = []
    return render_template('data-latih.html', dataSiswa=dSiswa)

@app.route('/prediksi')
def prediksi():
    return render_template('prediksi.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)