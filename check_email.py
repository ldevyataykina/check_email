#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import sys
import smtplib
import csv
import dns.resolver
from multiprocessing import Pool
import time
from generate_emails import emails
import socket

reload(sys)
sys.setdefaultencoding('utf-8')

df = pd.read_excel('15000_contacts/all_new.xlsx')

emails = emails()

def write_csv(data): # write to csv
    with open('15000_contacts/test.csv', 'a') as f:
        csv.writer(f).writerow((data['num'],
                                data['email']))

def checking_emails(elements): # checking all emails
    sur, name, patr, dom, num = elements
    global emails
    test_email = 'qweasdzxc123' + '@' + str(dom)
    email_status = 'none'
    trying = 0
    resolver = dns.resolver.Resolver()
    resolver.timeout = 60
    resolver.lifetime = 60
    while email_status is 'none':
        try:
            print(dom)
            mx_record = str(emails.get_mx(dom).split(' ')[1])
            if emails.check_email(test_email, mx_record) == 250:
                email_status = 'server_is_lying'
                break
            else:
                for email in emails.generate_email(sur, name, patr, dom):
                    if emails.check_email(email, mx_record) == 250:
                        email_status = email
                        data = {'num': num,
                                'email': email_status}
                        return data
                    else:
                        continue
                email_status = 'not_found'

        except (dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.name.LabelTooLong):
            email_status = 'no_dns'


        except (smtplib.SMTPServerDisconnected, socket.error, dns.resolver.NoAnswer, dns.exception.Timeout):
            trying += 1
            if trying < 3:
                time.sleep(5)
                pass
            else:
                email_status = 'error'
                break

    data = {'num': num,
            'email': email_status}
    return data

def make_all(inputs):
    data = checking_emails(inputs)
    write_csv(data)

if __name__ == '__main__':
    pool = Pool(processes=40)
    inputs = zip(df.sur_eng.values.tolist(), df.name_eng.values.tolist(), df.patr_eng.values.tolist(), df.domain.values.tolist(), df.number.values.tolist())
    print pool.map(make_all, inputs)
    pool.terminate()






