import sys
import socket
import logging
from concurrent.futures import ThreadPoolExecutor
import time  # Import time


def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        data = sock.recv(32)
        logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        start_time = time.time()  # Simpan waktu mulai
        request_count = 0  # Tambahkan counter
        futures = set()  # Set untuk menyimpan futures

        while time.time() - start_time < 10:  # Hanya jalankan loop selama 10 detik
            future = executor.submit(kirim_data)
            futures.add(future)

            # Jika ada future yang sudah selesai, hapus dari set dan tambahkan ke request_count
            completed_futures = {f for f in futures if f.done()}
            request_count += len(completed_futures)
            futures -= completed_futures

        # Tunggu semua task selesai sebelum keluar dari program
        for future in futures:
            future.result()

        # Cetak jumlah request yang telah dikirim setelah loop selesai
        logging.warning(f"Total requests sent: {request_count}")
