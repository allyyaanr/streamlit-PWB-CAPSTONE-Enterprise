import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data():
    data = pd.read_csv("Enterprise1_.csv")
    return data

def load_data1():
    data = pd.read_csv("Data Cleaning.csv")
    return data

def distribusi_histogram(df):
    debit_data = df['Debit'].value_counts()
    kredit_data = df['Kredit'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist([debit_data, kredit_data], bins=10, color=['skyblue', 'orange'], edgecolor='black', label=['Debit', 'Kredit'])
    ax.set_title('Metode Pembayaran Pada Perumahan Bukit Alam Lestari')
    ax.set_xlabel('Jumlah Pembayaran Debit atau Kredit')
    ax.set_ylabel('Frekuensi')
    ax.legend()
    ax.grid(True)

def perbandingan_piechart(df):
    kredit_counts = df['Kredit'].sum()
    debit_counts = df['Debit'].sum()
    labels = ['Kredit', 'Debit']
    sizes = [kredit_counts, debit_counts]
    plt.figure(figsize=(6, 6))
    plt.title('Perbandingan antara metode pembayaran kredit dan pembayaran debit')
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'])
    
def distribusi_boxplots(df):
    plt.figure(figsize=(15, 12))
    plt.subplot(2, 2, 1)
    sns.boxplot(data=df, x='Debit')
    plt.title("Boxplot Kolom Debit")
    plt.subplot(2, 2, 2)
    sns.boxplot(data=df, x='Kredit')
    plt.title("Boxplot Kolom Kredit")
    plt.subplot(2, 2, 3)
    sns.boxplot(data=df, x='Saldo')
    plt.title("Boxplot Kolom Saldo")
    plt.tight_layout()
    return plt

def hubungan_heatmap(df):
    df2 = df.drop(['Uraian'],axis=1)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df2.corr(), annot=True, cmap='coolwarm', ax=ax)
    plt.title('Heatmap korelasi antar kolom numerik')
    st.pyplot(fig)
    
def komposisi (df):
    df.drop(['Uraian'],axis=1, inplace=True)
    # Hitung rata-rata fitur untuk setiap kelas
    class_komposisi = df.groupby('Project').mean()
    # Plot komposisi kelas
    plt.figure(figsize=(10, 6))
    sns.heatmap(class_komposisi.T, annot=True, cmap='YlGnBu', fmt='.2f')
    plt.title('Komposisi berdasarkan wilayah pembangunan')
    plt.xlabel('Class')
    plt.ylabel('Feature')
    st.pyplot(plt)

def kolase(images):
    num_images = len(images)
    for i in range(0, num_images, 2):
        col1, col2 = st.columns(2)
        with col1:
            st.image(images[i], use_column_width=True)
        with col2:
            if i + 1 < num_images:
                st.image(images[i + 1], use_column_width=True)
                
def logo12():
        st.markdown(
            """
            <style>
            .center {
                display: flex;
                justify-content: center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        uploaded_logo = st.file_uploader("logo.jpg", type=["png", "jpg", "jpeg"])

        if uploaded_logo is not None:
            st.markdown('<div class="center"><img src="logo.jpg,{}" style="max-width: 200px;"></div>'.format(uploaded_logo.read().encode("base64").decode()), unsafe_allow_html=True)

        if __name__ == "__main__":
            main()
         
def encode_labels(value, options):
    return options.index(value)
   
def clustering(df):
    tampil_cluster(df)
    project_options = ['Km 9', 'Siaga', 'Km 4', 'Kariangau', 'Puncak Permai', 'Km 8']
    Project = st.selectbox('Project', options=project_options)
    jenis_pembayaran_options = ['Debit', 'Kredit']
    Jenis_Pembayaran = st.selectbox('Jenis Pembayaran', options=jenis_pembayaran_options)
    Debit = st.number_input('Debit')
    Kredit = st.number_input('Kredit')
    Saldo = st.number_input('Saldo')
    
    Project_encoded = encode_labels(Project, project_options)
    jenis_pembayaran_encoded = encode_labels(Jenis_Pembayaran, jenis_pembayaran_options)
    data = pd.DataFrame({
        'Project': [Project_encoded],
        'Debit': [Debit],
        'Kredit': [Kredit],
        'Saldo': [Saldo],
        'jenis_pembayaran': [jenis_pembayaran_encoded]
    })

    st.write(data)
    button = st.button('Clust!')
    
    if button:
        with open('kmeans.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        predicted = loaded_model.predict(data)
        answer = st.success(predicted)
        if answer == 0:
            st.success('Wilayah Pembangunan Km 9') 
        elif answer == 1:
            st.success('Wilayah Pembangunan Siaga')
        elif answer == 2:
            st.success('Wilayah Pembangunan Km 4') 
        elif answer == 3:
            st.success('Wilayah Pembangunan Kariangau') 
        elif answer == 4:
            st.success('Wilayah Pembangunan Puncak Permai')  
        elif answer == 5:
            st.success('Wilayah Pembangunan Km 8')

        
def tampil_cluster(data):
    df_clean = data.dropna(subset=['Project', 'Debit', 'Kredit', 'Saldo', 'jenis_pembayaran'])
    kolom = ['Project', 'Debit', 'Kredit', 'Saldo', 'jenis_pembayaran']
    X = df_clean[kolom]
    pipeline_kmeans = Pipeline([
        ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=3, random_state=42))
    ])
    pipeline_kmeans.fit(X)
    df_clean['kmeansCluster'] = pipeline_kmeans.named_steps['kmeans'].labels_
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_clean, x='Project', y='Saldo',hue='kmeansCluster', palette='viridis', s=100, alpha=0.6)
    plt.title('K-Means Clustering Result')
    plt.xlabel('Wilayah Pembangunan Project')
    plt.ylabel('Harga Bayar')
    st.pyplot(plt)
    st.write('**Keterangan Tampilan Cluster:**')
    st.write('0 = Wilayah Pembangunan Km 9')
    st.write('1 = Wilayah Pembangunan Siaga')
    st.write('2 = Wilayah Pembangunan Km 4')
    st.write('3 = Wilayah Pembangunan Kariangau')
    st.write('4 = Wilayah Pembangunan Puncak Permai')
    st.write('5 = Wilayah Pembangunan Km 8')
    
    st.write('**Keterangan Jenis Pembayaran:**')
    st.write('0 = Debit')
    st.write('1 = Kredit')
