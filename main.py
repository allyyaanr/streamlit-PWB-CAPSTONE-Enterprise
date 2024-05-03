import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import *
from st_on_hover_tabs import on_hover_tabs
from function import *

df = pd.read_csv('Enterprise1_.csv')
df2 = pd.read_csv('mapping.csv')

def main():
    st.sidebar.title("Menu")
    menu = ["Beranda", "Distribusi", "Hubungan", "Komposisi", "Perbandingan", "Clustering"]
    choice = st.sidebar.radio("Silahkan pilih untuk menelusuri informasi lebih lanjut!", menu)

    if choice == "Beranda":
        st.image("logo.jpg", width = 700)
        st.markdown(
        """
        <h1 style='text-align: center;'>PT. Tritunggal Borneo Karya - Analisis laporan keuangan dan promosi proyek perumahan Bukit Alam Lestari</h1>
        """,
        unsafe_allow_html=True
        )
        st.write("Mari temukan informasi terbaru tentang laporan keuangan kami dan promosi terbaru untuk proyek perumahan kami di Bukit Alam Lestari.")
        images = [
            "logo3.jpg",
            "logo4.jpg"
        ]
        kolase(images)
        
        st.header("About Us")
        st.write("PT. Tritunggal Borneo Karya mulai berdiri pada tahun 2010, selain bergerak dibidang general contractor dan supplier perusahaan ini juga bergerak dibidang properti yaitu sebagai pengembang (developer). Kami, sebagai pengembang properti, melihat bahwa sekarang adalah waktu yang tepat untuk berinvestasi dalam pembangunan kota. Dukungan dari sektor perbankan, terutama dalam penyaluran kredit kepemilikan rumah (KPR), memberikan peluang besar bagi kami untuk mengembangkan proyek perumahan skala menengah ke bawah di wilayah Kalimantan Timur. Dengan melihat perkembangan positif dan prospek yang cerah dalam industri properti, kami berkomitmen untuk memberikan kontribusi positif bagi masyarakat dengan membangun rumah-rumah yang terjangkau dan berkualitas. ")
        
        st.header("Visi dan Misi")
        st.write("Visi PT. Tritunggal Borneo Karya untuk menjadi perusahaan developer, general kontraktor, dan general suppliers terdepan di Indonesia khususnya di Kalimantan Timur yang senantiasa mendapatkan prioritas di hati costumer dan mitra.")
        st.write("<br>", unsafe_allow_html=True)
        st.write("Misi PT. Tritunggal Borneo Karya untuk meberikan kepuasan pelanggan, menumbuhkan kepercayaan, meningkatkan kualitas pekerjaan, menjaga ketetapan pekerjaan, dan memelihara harga agar kompetitif.")
        
        st.header("Background Proyek")
        st.image("logo1.jpg", use_column_width=True)
        st.image("logo2.jpg", use_column_width=True)
        st.image("logo5.jpg", use_column_width=True)
        
        
    elif choice == "Distribusi":
        st.markdown(
        """
        <h1 style='text-align: center;'>Halaman Distribusi</h1>
        """,
        unsafe_allow_html=True
        )
        st.write("<br>", unsafe_allow_html=True)
        fig = distribusi_histogram(df)
        st.pyplot(fig)
        st.write("Visualisasi histogram di atas menampilkan distribusi dari dua variabel, yaitu 'Saldo' dan 'Kredit', berdasarkan jenis metode pembayaran pada Perumahan Bukit Alam Lestari.")
        st.write("Hasil menunjukan bahwa:")
        st.write("1. Distribusi 'Saldo' cenderung lebih merata dibandingkan dengan distribusi 'Kredit' untuk setiap jenis metode pembayaran.")
        st.write("2. Untuk sebagian besar jenis metode pembayaran, jumlah observasi atau frekuensi untuk 'Saldo' lebih tinggi daripada 'Kredit', yang berati saldo cenderung menjadi fokus utama dalam dataset ini.")
        st.write("3. Terdapat variasi yang signifikan dalam jumlah observasi antara jenis metode pembayaran yang berbeda, yang dapat mengindikasikan preferensi atau kecenderungan tertentu dalam metode pembayaran di Perumahan Bukit Alam Lestari.")
        st.write("<br>", unsafe_allow_html=True)
        boxplot_figure = distribusi_boxplots(df)
        st.pyplot(boxplot_figure)
        st.write("Hasil dari ketiga visualisasi boxplot menunjukkan distribusi data untuk kolom 'Debit', 'Kredit', dan 'Saldo' pada dataset yang diamati.")
        st.write("1. Untuk kolom 'Debit', distribusi data terkonsentrasi pada nilai yang lebih rendah, dengan sebagian besar data berada di atas nilai median. Namun, terdapat beberapa outliers yang melebihi batas nilai maksimum.")
        st.write("2. Pada kolom 'Kredit', terdapat sedikit kemiringan distribusi ke arah nilai yang lebih tinggi, dengan sebagian besar data berada di atas nilai median. Begitu juga, terdapat beberapa outliers yang melebihi batas nilai maksimum")
        st.write("3. Sementara pada kolom 'Saldo', distribusi data cenderung lebih merata dengan sebagian besar data terkonsentrasi di sekitar nilai median. Namun, terdapat beberapa outliers yang melebihi batas nilai maksimum.")
        
    elif choice == "Hubungan":
        st.markdown(
        """
        <h1 style='text-align: center;'>Halaman Hubungan</h1>
        """,
        unsafe_allow_html=True
        )
        st.write("<br>", unsafe_allow_html=True)
        hubungan_heatmap(df2)
        st.write('Heatmap diatas menunjukkan korelasi antara kolom-kolom numerik dalam dataframe. Setiap sel dalam heatmap menunjukkan seberapa kuat korelasi antara dua kolom yang berbeda. Korelasi berkisar dari -1 hingga 1, di mana nilai 1 menunjukkan korelasi positif sempurna, nilai -1 menunjukkan korelasi negatif sempurna, dan nilai 0 menunjukkan tidak adanya korelasi. Hasilnya adalah sebuah heatmap yang menunjukkan korelasi antara kolom-kolom numerik dalam dataframe. Dalam heatmap tersebut, korelasi antara "Debit", "Kredit", "Saldo", "Project", dan "jenis_pembayaran" adalah 1, yang ditampilkan dengan warna merah. Hal ini menunjukkan bahwa kelima kolom memiliki korelasi positif sempurna satu sama lain.')
        
    elif choice == "Komposisi":
        st.markdown(
        """
        <h1 style='text-align: center;'>Halaman Komposisi</h1>
        """,
        unsafe_allow_html=True
        )
        st.write("<br>", unsafe_allow_html=True)
        komposisi(df2)
        st.write('Pada heatmap diatas menunjukkan komposisi  kelas yang diambil dari rata-rata setiap fitur yang ada (kolom) yang berhubungan dengan label prediksinya yaitu wilayah pembangunan.')
        st.write('Contoh :')
        st.write('''Untuk wilayah pembangunan Km9 (0) pada kolom jenis_pembayarannya sebesar 0.95 mendekati 1 artinya banyak costumer menggunakan jenis_pembayaran 1 yaitu kredit, 
                 lalu pada kolom Saldo nilai rata-rata costumer di Km9 (0) sebesar 77811300.14, pada kolom Kredit nilai rata-rata costumer di Km9 (0) sebesar 2233928.99, dan
                 pada kolom Debit nilai rata-rata costumer di Km9 (0) sebesar 927595.34''')
        
    elif choice == "Perbandingan":
        st.markdown(
        """
        <h1 style='text-align: center;'>Halaman Perbandingan</h1>
        """,
        unsafe_allow_html=True
        )
        st.write("<br>", unsafe_allow_html=True)
        pie_chart = perbandingan_piechart(df)
        st.pyplot(pie_chart)
        st.write("Hasil dari visualisasi di atas menunjukkan perbandingan antara kredit dan debit. Dari diagram lingkaran tersebut, terlihat bahwa banyak customer melakukan transaksi dengan metode pembayaran kredit memiliki persentase sebesar 51%, sedangkan customer yang melakukan transaksi dengan metode pembayaran debit memiliki persentase 49%. Dengan demikian, dapat disimpulkan bahwa pembagian antara kredit dan debit dalam dataset hampir seimbang.")
        
    elif choice == "Clustering":
        st.title("Clustering!")
        clustering(df2)
        
if __name__ == "__main__":
    main()

