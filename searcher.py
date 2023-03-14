import os
import pandas as pd
from settings import csv_folder


def _find_info_in_csv(filename: str, number: str):
    op_code = int(number[:3])
    seven_digits = number[3:]

    if len(seven_digits) != 7:
        return _make_error_dict('Неверный формат номера')
    seven_digits = int(seven_digits)

    df = pd.read_csv(os.path.join(csv_folder, filename), sep=';')
    info = df.loc[
        (df['АВС/ DEF'] == op_code) &
        (df['От'] <= seven_digits) &
        (df['До'] >= seven_digits),
        ['Оператор', 'Регион']
    ]
    if len(info):
        info = info.to_dict(orient='records')[0]
        info['Номер'] = int(number)
        return info
    return _make_error_dict('Номер не найден')


def _make_error_dict(err):
    return {'error': err}


def search_number_info(number):
    number = number.lstrip(' +')
    if number.startswith('7'):
        number = number[1:]

    for filename in os.listdir(csv_folder):
        if f'{number[0]}xx' in filename:
            return _find_info_in_csv(filename, number)
    return _make_error_dict('Неверный код оператора')
