import io
import os
import unittest

import main


class TestWriteOutputCsv(unittest.TestCase):
    def test1(self):
        dummy_data = [['田中 美智子', '女', '1989/3/11', '', '03-0000-0004', '1000004', '東京千代田区大手町1-1-1', '化粧水', '2018/10/19 15:30:00']]

        file_path = os.path.join("testoutput", 'success.csv')
        main.write_output_csv(dummy_data, file_path)

        with open(file_path, encoding="utf-8") as file:

            expected = io.StringIO()
            expected.write('田中 美智子,女,1989/3/11,,03-0000-0004,1000004,東京千代田区大手町1-1-1,化粧水,2018/10/19 15:30:00\n')
            self.assertEqual(file.read(), expected.getvalue())


class TestWriteFailureCsv(unittest.TestCase):
    def test1(self):
        dummy_data = {3: '商品番号を規定通りに記載して下さい。', 5: '商品番号を規定通りに記載して下さい。'}

        file_path = os.path.join('testfailure', 'sawaki.csv')
        main.write_failure_csv(dummy_data, file_path)

        with open(file_path)as file:

            expected = io.StringIO()
            expected.write('商品番号を規定通りに記載して下さい。\t(3行目)\n商品番号を規定通りに記載して下さい。\t(5行目)\n')
            self.assertEqual(file.read(), expected.getvalue())


if __name__ == '__main__':
    unittest.main()
