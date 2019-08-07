import unittest
from validator import validation_err_format


class ValidationErrFormat(unittest.TestCase):
    def test1_pattern1_name(self):
        """名前のパリデーション
        """
        dummy_data = {'name': '', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '氏名を記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern2_name(self):
        dummy_data = {'name': '太宰治'*100, 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '名前を32文字以下で記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern1_gender(self):
        """性別のバリデーション
        """
        dummy_data = {'name': '太宰治', 'gender': '', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '性別を記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern2_gender(self):
        dummy_data = {'name': '太宰治', 'gender': '不明', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '性別を規定通りに記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern1_tel(self):
        """電話のバリデーション
        """
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '電話番号を記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern2_tel(self):
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '0000000', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '電話番号を規定通りに記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern1_post(self):
        """郵便番号のバリデーション
        """
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '郵便番号を記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern2_post(self):
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '111', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '郵便番号を規定通りに記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern1_address(self):
        """住所のバリデーション
        """
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '',
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '住所を記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern2_address(self):
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1'*100,
                      'item_num': 'A01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '住所を64文字以下で入力して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern1_item(self):
        """商品番号のバリデーション
        """
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': '', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '商品番号を記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern2_item(self):
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'S01', 'reception_date': '2018/10/19 15:30'}
        actual = validation_err_format(dummy_data)
        expected = '商品番号を規定通りに記載して下さい。'
        self.assertEqual(actual, expected)

    def test1_pattern1_date(self):
        """受付日時のバリデーション
        """
        dummy_data = {'name': '太宰治', 'gender': '男', 'birthday': '1909/6/19', 'email': '',
                      'tel': '03-0000-0004', 'post_code': '1000004', 'address': '東京港区麻布十番1-1-1',
                      'item_num': 'A01', 'reception_date': ''}
        actual = validation_err_format(dummy_data)
        expected = '受付日時を記載して下さい。'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
