
import csv

OUTPUT_DIRECTORY_PATH = 'output'
ERROR_FILE_DIRECTORY_PATH = 'failure'


def write_output_csv(correct_list, output_path):
    """不備がなかった行を success.csv に出力
    """

    with open(output_path, 'w') as fw:
        writer = csv.writer(fw)
        writer.writerows(correct_list)


def write_failure_csv(err_msg_dict, failure_path):
    """不備がある行を failureディレクトリ直下に出力
    """
    with open(failure_path, 'w')as fw:
        for index, err_mag in err_msg_dict.items():
            fw.write(err_mag + '\t' + '({}行目)\n'.format(index))
