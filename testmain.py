#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import unittest

import main


class TestConversionDataFormat(unittest.TestCase):
    def test1(self):
        dummy_data = {'name': '田中 美智子', 'gender': '女', 'birthday': '1989/3/11',
                      'email': '', 'tel': '03-0000-0004', 'post_code': '1000004',
                      'address': '東京千代田区大手町1-1-1', 'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = main.conversion_data_format(dummy_data)
        expected = ['田中 美智子', '女', '1989/3/11', '', '03-0000-0004', '1000004',
                    '東京千代田区大手町1-1-1', '化粧水', '2018/10/19 15:30:00']
        self.assertEqual(actual, expected)


class TestSortingAggregate(unittest.TestCase):

    def test1(self):
        dummy_data = {'sawaki.csv': [{'name': '田中 美智子', 'gender': '女', 'birthday': '1989/3/11', 'email': '',
                                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京千代田区大手町1-1-1',
                                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'},
                                     {'name': '広瀬 栄太', 'gender': '男', 'birthday': '1953/5/13', 'email': '',
                                      'tel': '080-0000-0006', 'post_code': '1000004', 'address': '東京千代田区大手町1-1-1',
                                      'item_num': 'D01', 'reception_date': '2018/10/22 11:30'}]}

        actual = main.sorting_aggregate(dummy_data)
        expected_list = [['田中 美智子', '女', '1989/3/11', '', '03-0000-0004', '1000004', '東京千代田区大手町1-1-1',
                          '化粧水', '2018/10/19 15:30:00']]
        expected_dict = {'sawaki.csv': {3: '商品番号を規定通りに記載して下さい。'}}
        expected_total = (expected_list, expected_dict)
        self.assertEqual(actual, expected_total)


class TestParseInputCsvDict(unittest.TestCase):

    def test1(self):
        dummy_file_csv = """氏名,性別,生年月日,メールアドレス,電話番号,郵便番号,住所,希望サンプル商品番号,受付日時
田中 美智子,女,1989/3/11,,03-0000-0004,1000004,東京千代田区大手町1-1-1,A01,2018/10/19 15:30
広瀬 栄太,男,1953/5/13,,080-0000-0006,1000004,東京千代田区大手町1-1-1,D01,2018/10/22 11:30"""
        dummy_file = io.StringIO(dummy_file_csv)
        dummy_file_list = 'sawaki.csv'
        dummy_input_csv_dict = {}
        actual = main.parse_input_csv_dict(dummy_file, dummy_file_list, dummy_input_csv_dict)
        expected = {'sawaki.csv': [{'name': '田中 美智子', 'gender': '女', 'birthday': '1989/3/11', 'email': '',
                                    'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京千代田区大手町1-1-1',
                                    'item_num': 'A01', 'reception_date': '2018/10/19 15:30'},
                                   {'name': '広瀬 栄太', 'gender': '男', 'birthday': '1953/5/13', 'email': '',
                                    'tel': '080-0000-0006', 'post_code': '1000004', 'address': '東京千代田区大手町1-1-1',
                                    'item_num': 'D01', 'reception_date': '2018/10/22 11:30'}]}

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
