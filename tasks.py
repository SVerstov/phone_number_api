import datetime
import os
import threading

from downloader import download_csv_files
from settings import download_period, download_links, csv_folder


def periodic_downloader():
    print("Начало загрузки файлов", datetime.datetime.now())
    download_csv_files()
    print("Файлы загружены", datetime.datetime.now())

    threading.Timer(download_period, periodic_downloader).start()


def start_periodic_task():
    if len(download_links) != len(os.listdir(csv_folder)):
        threading.Thread(target=periodic_downloader).start()
    else:
        threading.Timer(download_period, periodic_downloader).start()
