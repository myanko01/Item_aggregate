#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

import zenhan
from dateutil import parser

from validator import validation_err_format
from writer import write_output_csv, write_failure_csv

SUCCESS_DATA_HEADER = ['氏名', '性別', '生年月日', 'メールアドレス', '電話番号', '郵便番号',
                       '住所', '希望サンプル商品番号', '受付日時']
GENDER_MODIFIED_MAP = {'男性': '男', '男': '男', '女性': '女', '女': '女'}
SAMPLE_PRODUCT_MAP = {'A01': '化粧水', 'Ａ０１': '化粧水',
                      'B01': 'ハンドクリーム', 'Ｂ０１': 'ハンドクリーム',
                      'C01': 'リップクリーム', 'Ｃ０１': 'リップクリーム'}
EMAIL_PTN = re.compile(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*')
OUTPUT_DIRECTORY_PATH = 'output'
ERROR_FILE_DIRECTORY_PATH = 'failure'


def conversion_data_format(input_data_dict):
    """変換処理を行いリストに格納し、それを返す処理。
    """

    name = input_data_dict['name'].strip()

    gender = GENDER_MODIFIED_MAP[input_data_dict['gender']]

    birthday = input_data_dict['birthday']

    email = input_data_dict['email']

    tel = zenhan.z2h(input_data_dict['tel']).replace('ー', '-')

    zip_code = input_data_dict['post_code'].replace('ー', '')

    address = input_data_dict['address']

    item_sample = SAMPLE_PRODUCT_MAP[input_data_dict['item_num']]

    reception_datetime = parser.parse(input_data_dict['reception_date'])
    str_reception_datetime = reception_datetime.strftime('%Y/%m/%d %H:%M:%S')
    conversion_format = [name, gender, birthday, email, tel, zip_code, address, item_sample, str_reception_datetime]
    return conversion_format


def sorting_aggregate(input_csv_dict):
    """　記載情報を格納する辞書を受け取り、エラーが出てなければ、変換処理を加え正しいファイル(データはリストに持たせる)に、
        エラーの場合、エラー出力とともに謝りファイルにデータを保存する(dictとして持たせる)という不備の振り分け処理。
    """
    err_msg_dict = {}
    correct_list = []
    for file_name, input_data_list in input_csv_dict.items():

        index = 1
        for input_data_dict in input_data_list:
            index += 1
            err_msgs = validation_err_format(input_data_dict)

            if not err_msgs:
                correct_list.append(conversion_data_format(input_data_dict))
            else:
                err_msg_dict.setdefault(file_name, {})
                err_msg_dict[file_name][index] = err_msgs
    return correct_list, err_msg_dict


def parse_input_csv_dict(file, file_list, input_csv_dict):
    """　csvファイル毎に記載情報を格納する辞書を返す関数。
        {ファイル1:[{記載情報名1:データ, 記載情報名:データ},{記載情報名2:データ, 記載情報名:データ},..],
        ファイル2:[...]}
        file = input_file
        file_list = 全てのcsvファイル(2つ)
    """

    for index, row in enumerate(file):
        if index == 0:
            continue

        input_data = row.rstrip().split(',')
        input_csv_dict.setdefault(file_list, [])

        input_csv_dict[file_list].append({'name': input_data[0], 'gender': input_data[1], 'birthday': input_data[2],
                                          'email': input_data[3], 'tel': input_data[4], 'post_code': input_data[5],
                                          'address': input_data[6], 'item_num': input_data[7],
                                          'reception_date': input_data[8]})

    return input_csv_dict


def main():

    input_csv_dict = {}
    for file_name in os.listdir('input'):
        file_path = os.path.join('input', file_name)
        with open(file_path)as input_file:
            parse_input_csv_dict(input_file, file_name, input_csv_dict)

    correct_list, err_msg_dict = sorting_aggregate(input_csv_dict)

    os.makedirs(OUTPUT_DIRECTORY_PATH, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIRECTORY_PATH, 'success.csv')

    write_output_csv(correct_list, output_path)

    os.makedirs(ERROR_FILE_DIRECTORY_PATH, exist_ok=True)
    for file_name, err_msgs in err_msg_dict.items():
        failure_path = os.path.join(ERROR_FILE_DIRECTORY_PATH, file_name)

        write_failure_csv(err_msgs, failure_path)


if __name__ == '__main__':
    main()
