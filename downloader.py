import requests
from settings import download_links, csv_folder


def download_csv_files():
    headers = {'User-Agent': 'Mozilla/5.0'}
    for link in download_links:
        filename = csv_folder + '/' + link.split('/')[-1]

        try:
            response = requests.get(link, verify=False, headers=headers)
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'{filename} downloaded successfully')
        except requests.exceptions.RequestException as e:
            print(f'Error downloading {filename}: {e}')
