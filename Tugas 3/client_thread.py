import sys
import socket
import logging
import threading
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


def create_thread():
    t = threading.Thread(target=kirim_data)
    t.start()
    t.join()


if __name__ == '__main__':
    thread_count = 0  # Tambahkan counter
    start_time = time.time()  # Simpan waktu mulai
    while time.time() - start_time < 10:  # Hanya jalankan loop selama 10 detik
        create_thread()
        thread_count += 1  # Update counter di sini
    # Cetak jumlah thread yang telah dibuat
    logging.warning(f"Total threads created: {thread_count}")
