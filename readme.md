# Analisis Sentimen Artikel Berita Padel di Indonesia Menggunakan Fine-Tuning Model IndoBERT

Proyek ini berfokus pada analisis opini publik mengenai perkembangan olahraga Padel di Indonesia melalui media daring. Menggunakan model transformer **IndoBERT**, kami mengklasifikasikan sentimen dari artikel berita nasional untuk memahami dinamika tren olahraga ini.

## Deskripsi Proyek
Padel adalah olahraga yang sedang berkembang pesat di Indonesia. Proyek ini mengumpulkan data dari berbagai portal berita (Detik, Kompas, Tempo, CNN Indonesia, dll.) untuk melihat bagaimana media dan masyarakat merespons fenomena ini. Kami menggunakan pendekatan **Natural Language Processing (NLP)** untuk mengekstrak wawasan dari teks berita yang bersifat formal dan kompleks.

## Alur Pengerjaan
- **Web Scraping:** Pengumpulan data otomatis dari Google News RSS, Bing News, dan portal berita langsung.
- **Preprocessing:** Normalisasi teks, tokenisasi, penghapusan stopwords (NLTK + Custom), dan lemmatization (Sastrawi).
- **Klasifikasi Sentimen:** Menggunakan model `IndoBERT-base-p2` yang di-*fine-tune* untuk domain bahasa Indonesia.
- **Ekstraksi Fitur:**
  - **TF-IDF Analysis:** Identifikasi kata kunci signifikan per portal berita dan per bulan.
  - **POS Tagging & NER:** Identifikasi jenis kata dan entitas penting (Orang, Lokasi, Organisasi) menggunakan library Stanza.
  - **N-gram Analysis:** Analisis hubungan antar kata (Bigram).

## Teknologi yang Digunakan
- **Bahasa:** Python
- **Model NLP:** IndoBERT (Hugging Face Transformers)
- **Library Utama:** `torch`, `transformers`, `pandas`, `nltk`, `Sastrawi`, `stanza`, `scikit-learn`.

## Hasil Analisis
- **Akurasi Model:** ~87%
- **Distribusi Sentimen:** Didominasi oleh sentimen **Netral (95,7%)**, menunjukkan bahwa pemberitaan Padel saat ini masih bersifat informatif dan faktual.
- **Wawasan Utama:** Sentimen negatif biasanya muncul dari isu konflik sosial terkait pembangunan fasilitas lapangan di kawasan perumahan.

## Tim Penyusun
Proyek ini disusun oleh mahasiswa Departemen Sistem Informasi - ITS (Kelompok A):
1. Daniel Bara Seftino
2. Oryza Reynaleta Wibowo
3. Metta Anjali Putri
4. Muhammad Naufal Erwin Effendi
5. Muhammad Abyansyah Putra Dewanto
