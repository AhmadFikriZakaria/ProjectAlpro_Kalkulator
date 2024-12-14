from flask import Flask, render_template, request, flash
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Diperlukan untuk flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kalkulator_matematika', methods=['GET', 'POST'])
def kalkulator_matematika():
    hasil = None
    if request.method == 'POST':
            angka1 = float(request.form['angka1'])
            angka2 = float(request.form['angka2'])
            operasi = request.form['operasi']
            
            if operasi == 'tambah':
                hasil = angka1 + angka2
            elif operasi == 'kurang':
                hasil = angka1 - angka2
            elif operasi == 'kali':
                hasil = angka1 * angka2
            elif operasi == 'bagi':
                if angka2 == 0:
                    flash('Error: Pembagian dengan nol tidak diperbolehkan!')
                    return render_template('kalkulator_matematika.html', hasil=None)
                hasil = angka1 / angka2
            
    return render_template('kalkulator_matematika.html', hasil=hasil)

@app.route('/kalkulator_bmi', methods=['GET', 'POST'])
def kalkulator_bmi():
    bmi = None
    kategori = None
    if request.method == 'POST':
            berat = float(request.form['berat'])
            tinggi = float(request.form['tinggi'])

            if berat <= 0 or tinggi <= 0:
                flash('Error: Berat dan tinggi harus lebih besar dari 0!')
                return render_template('kalkulator_bmi.html', bmi=None, kategori=None)

            tinggi = tinggi / 100    
            bmi = berat / (tinggi ** 2)
            
            if bmi < 18.5:
                kategori = "Kurus Kerempeng"
            elif 18.5 <= bmi < 24.9:
                kategori = "Normal"
            elif 25 <= bmi < 29.9:
                kategori = "Gendut"
            else:
                kategori = "Obesitas"
                            
    return render_template('kalkulator_bmi.html', bmi=bmi, kategori=kategori)

@app.route('/kalkulator_umur', methods=['GET', 'POST'])
def kalkulator_umur():
    hasil = None
    if request.method == 'POST':
            tanggal_lahir = datetime.strptime(request.form['tanggal_lahir'], '%Y-%m-%d')
            hari_ini = datetime.now()
            
            if tanggal_lahir > hari_ini:
                flash('Error: Tanggal lahir tidak boleh di masa depan!')
                return render_template('kalkulator_umur.html', hasil=None)
            
            tahun = hari_ini.year - tanggal_lahir.year
            bulan = hari_ini.month - tanggal_lahir.month
            hari = hari_ini.day - tanggal_lahir.day
            
            if hari < 0:
                bulan -= 1
                akhir_bulan = hari_ini.replace(day=1) - timedelta(days=1)
                hari += akhir_bulan.day
                
            if bulan < 0:
                tahun -= 1
                bulan += 12
                
            hasil = {
                'years': tahun,
                'months': bulan,
                'days': hari
            }
            
    return render_template('kalkulator_umur.html', hasil=hasil)