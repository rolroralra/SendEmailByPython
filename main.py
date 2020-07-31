from smtpClient import SmtpClient
from openpyxl import load_workbook

import configparser
import os

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    emailSendListFilePath = os.path.join(
        config['EMAIL-SEND-LIST']['FILE_DIR'],
        config['EMAIL-SEND-LIST']['FILE_NAME']
    )

    smtpClient = SmtpClient(config['SMTP-SERVER'])

    wb = load_workbook(emailSendListFilePath)
    ws = wb.active
    for row in ws.iter_rows():
        addr = row[0].value
        subj_layout = row[1].value
        cont_layout = row[2].value
        attachment = row[3].value

        print('RECEIVER:', addr)
        print('SUBJECT:', subj_layout)
        print('CONTENT:', cont_layout)
        print('ATTCHMENT:', attachment)
        smtpClient.send_mail(addr, subj_layout, cont_layout, attachment)
        print()
