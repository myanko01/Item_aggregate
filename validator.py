import re


TEL_PTN = re.compile(r'\d{2,4}[ー-]?\d{3,4}[ー-]?\d{4}')
POST_CODE_PTN = re.compile(r'\d{3}-?(?:\d{4}|\d{7})')


def validation_err_format(input_data_dict):
    """エラーメッセージの出力
    """

    err_msg = ''

    if not input_data_dict['name']:
        err_msg += '氏名を記載して下さい。'
    else:
        if len(input_data_dict['name']) > 32:
            err_msg += '名前を32文字以下で記載して下さい。'
    if not input_data_dict['gender']:
        err_msg += '性別を記載して下さい。'
    else:
        if input_data_dict['gender'] not in ['男性', '男', '女性', '女']:
            err_msg += '性別を規定通りに記載して下さい。'
    if not input_data_dict['tel']:
        err_msg += '電話番号を記載して下さい。'
    else:
        if not re.match(TEL_PTN, input_data_dict['tel']):
            err_msg += '電話番号を規定通りに記載して下さい。'
    if not input_data_dict['post_code']:
        err_msg += '郵便番号を記載して下さい。'
    else:
        if not re.match(POST_CODE_PTN, input_data_dict['post_code']):
            err_msg += '郵便番号を規定通りに記載して下さい。'
    if not input_data_dict['address']:
        err_msg += '住所を記載して下さい。'
    else:
        if len(input_data_dict['address']) > 64:
            err_msg += '住所を64文字以下で入力して下さい。'
    if not input_data_dict['item_num']:
        err_msg += '商品番号を記載して下さい。'
    else:
        if input_data_dict['item_num'] not in ['A01', 'B01', 'C01', 'Ａ０１', 'Ｂ０１', 'Ｃ０１']:
            err_msg += '商品番号を規定通りに記載して下さい。'
    if not input_data_dict['reception_date']:
        err_msg += '受付日時を記載して下さい。'
    else:
        if not input_data_dict['reception_date']:
            err_msg += '受付日時を規定通りに記載して下さい。'
    return err_msg

