import os

class Film:
    def __init__(self, nama, judul, genre, durasi, jadwal, harga_tiket, jumlah_tiket_tersedia):
        self.nama = nama
        self.judul = judul
        self.genre = genre
        self.durasi = durasi
        self.jadwal = jadwal
        self.harga_tiket = harga_tiket
        self.jumlah_tiket_tersedia = jumlah_tiket_tersedia

    def __str__(self):
        return f"Nama:{self.nama}\nJudul: {self.judul}\nGenre: {self.genre}\nDurasi: {self.durasi}\nJadwal: {self.jadwal}\nHarga tiket: Rp{self.harga_tiket}\nJumlah tiket tersedia: {self.jumlah_tiket_tersedia}"



daftar_film = [
    Film(" ", "The Batman", "Action, Crime, Mystery", "176 menit", "19:00 WIB", 50000, 100),
    Film(" ", "Top Gun: Maverick", "Action, Drama, Romance", "138 menit", "21:00 WIB", 45000, 75),
    Film(" ", "Doctor Strange in the Multiverse of Madness", "Action, Adventure, Fantasy", "126 menit", "23:00 WIB", 40000, 50),
]

def input_nama():
    return input("Masukkan Nama : ")

def menu_utama():
    print("Selamat datang di aplikasi ticketing bioskop!")
    print("Pilih menu yang diinginkan:")
    print("1. Daftar film")
    print("2. Pesan tiket")
    print("3. Keluar")

    pilihan = input("Pilihan Anda: ")
    return pilihan


def tampilkan_daftar_film():
    print("Daftar film hari ini:")
    for nomor, film in enumerate(daftar_film, start=1):
        print(f"{nomor}. {film}")

    input("Tekan Enter untuk kembali ke menu utama...")

def pesan_tiket():
  print("Pilih film yang ingin Anda pesan:")
  for nomor, film in enumerate(daftar_film, start=1):
      print(f"{nomor}. {film.judul}")

  pilihan_film = input("Pilihan Anda: ")

  try:
      pilihan_film = int(pilihan_film)
  except ValueError:
      print("Pilihan Anda tidak valid.")
      return

  if not 1 <= pilihan_film <= len(daftar_film):
      print("Pilihan Anda tidak valid.")
      return

  film = daftar_film[pilihan_film - 1]

  print(f"Anda memilih film {film.judul}.")
  print("Berapa tiket yang ingin Anda pesan?")

  jumlah_tiket = input("Jumlah tiket: ") 
  try:
      jumlah_tiket = int(jumlah_tiket)
  except ValueError:
      print("Jumlah tiket yang Anda masukkan tidak valid.")
      return

  if jumlah_tiket > film.jumlah_tiket_tersedia:
      print("Jumlah tiket yang Anda inginkan melebihi ketersediaan.")
      return

  total_harga = film.harga_tiket * jumlah_tiket
  print(f"Total harga tiket: Rp{total_harga}")

  film.jumlah_tiket_tersedia -= jumlah_tiket
  print("Pemesanan berhasil!")

  # Call the input_nama() function and store its return value in a variable
  nama = input_nama()

  pesan = Film(nama, film.judul, film.genre, film.durasi, film.jadwal, film.harga_tiket, jumlah_tiket)

  pesan_str = str(pesan)

  os.makedirs(os.path.join('User Data_Catatan film', nama), exist_ok=True)

  with open(os.path.join('User Data_Catatan film', nama, f'{nama}.txt'), 'w') as f:
      # Write the string representation of the object to the file
      f.write(pesan_str)
      input("Tekan Enter untuk menyelesaikan pemesanan...")

while True:
    pilihan = menu_utama()

    if pilihan == "1":
        tampilkan_daftar_film()
    elif pilihan == "2":
        pesan_tiket()
    elif pilihan == "3":
        break



