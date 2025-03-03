import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, filedialog, Button, Label, OptionMenu, StringVar, messagebox

def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(title="CSV Dosyasını Seçin", filetypes=[("CSV files", "*.csv")])
    
    if dosya_yolu:
        global df
        df = pd.read_csv(dosya_yolu)
        print(df)

        ortalama = df['Satış'].mean()
        medyan = df['Satış'].median()
        min_deger = df['Satış'].min()
        max_deger = df['Satış'].max()
        std_sapma = df['Satış'].std()

        istatistikler.config(
            text=f"Ortalama: {ortalama:.2f}\nMedyan: {medyan}\nMin: {min_deger}\nMax: {max_deger}\nStandart Sapma: {std_sapma:.2f}"
        )

        grafik_turu = grafik_seçimi.get()

        plt.figure(figsize=(8, 5))
        if grafik_turu == "Çizgi Grafik":
            sns.lineplot(x='Tarih', y='Satış', data=df, marker='o', color='blue')
        elif grafik_turu == "Çubuk Grafik":
            sns.barplot(x='Tarih', y='Satış', data=df, palette='viridis')
        elif grafik_turu == "Dağılım Grafiği":
            sns.scatterplot(x='Tarih', y='Satış', data=df, color='red')
        
        plt.title(f"{grafik_turu} - Satış Trendleri")
        plt.xticks(rotation=45)

        plt.show()

        kaydet_buton.config(state="normal", command=lambda: grafiği_kaydet(grafik_turu))

def grafiği_kaydet(grafik_turu):
    dosya_yolu = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    
    if dosya_yolu:
        plt.figure(figsize=(8, 5))
        if grafik_turu == "Çizgi Grafik":
            sns.lineplot(x='Tarih', y='Satış', data=df, marker='o', color='blue')
        elif grafik_turu == "Çubuk Grafik":
            sns.barplot(x='Tarih', y='Satış', data=df, palette='viridis')
        elif grafik_turu == "Dağılım Grafiği":
            sns.scatterplot(x='Tarih', y='Satış', data=df, color='red')

        plt.title(f"{grafik_turu} - Satış Trendleri")
        plt.xticks(rotation=45)
        
        plt.savefig(dosya_yolu)
        plt.close()
        
        messagebox.showinfo("Başarılı", f"Grafik başarıyla kaydedildi: {dosya_yolu}")

pencere = Tk()
pencere.title("Veri Analizi Aracı")

grafik_seçimi = StringVar(pencere)
grafik_seçimi.set("Çizgi Grafik")
grafik_turu_menu = OptionMenu(pencere, grafik_seçimi, "Çizgi Grafik", "Çubuk Grafik", "Dağılım Grafiği")
grafik_turu_menu.pack(pady=10)

secim_buton = Button(pencere, text="CSV Dosyası Seç", command=dosya_sec)
secim_buton.pack(pady=20)

kaydet_buton = Button(pencere, text="Grafiği Kaydet", state="disabled")
kaydet_buton.pack(pady=10)

istatistikler = Label(pencere, text="İstatistikler burada görünecek", justify="left")
istatistikler.pack(pady=10)

pencere.mainloop()
