# Item Recommendataion

<<<<<<< HEAD
 Pada item-based, prediksi rekomendasi didasarkan oleh kesamaan antar item. Membangun model kesamaan item dengan mengumpulkan semua item yang dinilai oleh user aktif dari matriks user-item, dimana menentukan seberapa mirip item yang diambil dengan item target, kemudian memilih n item yang paling mirip. Prediksi yang dibuat dengan menghitung rata-rata yang terbobot dari rating pengguna aktif pada item-item serupa n. 
=======
Pada item-based, prediksi rekomendasi didasarkan oleh kesamaan antar item. Membangun model kesamaan item dengan mengumpulkan semua item yang dinilai oleh user aktif dari matriks user-item, dimana menentukan seberapa mirip item yang diambil dengan item target, kemudian memilih n item yang paling mirip. Prediksi yang dibuat dengan menghitung rata-rata yang terbobot dari rating pengguna aktif pada item-item serupa n. 
>>>>>>> cd65d6d2e003b314e9070aecb23cd64142cbff4d
Berikut Algoritma untuk item-based collaborative filtering:
1.	Pembentukan matrik user-item rating dari dataset
2.	Menghitung nilai similarity antara item i dengan item lainnya menggunakan rumus  cosine similarity
3.	Menemukan top n item (item neighbor) yang memiliki similarity tinggi dengan item i
4.  Memberikan rekomendasi sebanyak n dengan urutan similarity dari yang paling tinggi (mendekati 1)
5.	Menghitung nilai prediksi terhadap top n item (item neighbor) oleh user u dengan rumus weighted sum
