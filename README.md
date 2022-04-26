# Item Recommendataion

Untuk menjalankan program ini pastikan menambahkan/mengkonfigurasi file `.env` yang berisi:
- USER=<username>
- PASSWORD=<pasword>
- DATABASE=<database>
- SECRET_KEY=<secret key>
- WTF_CSRF_SECRET_KEY=<csrf secret key>

Program ini menggunakan database `mongodb` dan .env file di atas digunakan untuk menjalankan database tersebut.

Selanjutya script rekomendasi ada di app -> libraries -> recommender.py .