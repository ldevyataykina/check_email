import pandas as pd
import dns.resolver
import socket
import smtplib

class emails:
    def generate_email(self, sur, name, patr, dom):  # generate all email combinations

        all_emails = [
                str(name) + '@' + str(dom),
                str(name) + str(sur) + '@' + str(dom),
                str(name) + '.' + str(sur) + '@' + str(dom),
                str(sur) + '@' + str(dom),
                str(name)[0] + str(sur) + '@' + str(dom),
                str(name)[0] + '.' + str(sur) + '@' + str(dom),
                str(name) + str(sur)[0] + '@' + str(dom),
                str(name) + '.' + str(sur)[0] + '@' + str(dom),
                str(name)[0] + str(sur)[0] + '@' + str(dom),
                str(name)[0] + '@' + str(dom),
                str(name)[0] + str(patr)[0] + str(sur) + '@' + str(dom),
                str(name)[0] + str(patr)[0] + str(sur)[0] + '@' + str(dom),
                str(name)[0] + str(patr)[0] + '.' + str(sur) + '@' + str(dom),
                str(name)[0] + '.' + str(sur) + '@' + str(dom),
                str(sur) + str(name) + '@' + str(dom),
                str(sur) + str(name)[0] + '@' + str(dom),
                str(sur) + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(sur) + '.' + str(name) + '@' + str(dom),
                str(sur) + '.' + str(name)[0] + '@' + str(dom),
                str(sur) + '.' + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(sur)[0] + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(sur)[0] + str(name) + '@' + str(dom),
                str(sur)[0] + '.' + str(name) + '@' + str(dom),
                str(name) + str(sur)[0] + '@' + str(dom),
                str(name) + '.' + str(sur)[0] + '@' + str(dom),
                str(sur)[:4] + '_' + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(sur)[:3] + '_' + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(name)[0] + str(patr)[0] + '_' + str(sur)[:3] + '@' + str(dom),
                str(sur)[:3] + '-' + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(name)[0] + str(patr)[0] + '-' + str(sur)[:3] + '@' + str(dom),
                str(name) + '_' + str(sur)[0] + '@' + str(dom),
                str(sur)[0] + '_' + str(name) + '@' + str(dom),
                str(name) + '_' + str(sur) + '@' + str(dom),
                str(name)[0] + '_' + str(sur) + '@' + str(dom),
                str(name) + '-' + str(sur)[0] + '@' + str(dom),
                str(name)[0] + '-' + str(sur) + '@' + str(dom),
                str(sur) + '-' + str(name) + '@' + str(dom),
                str(sur) + '-' + str(name)[0] + '@' + str(dom),
                str(sur) + '-' + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(name) + '-' + str(sur)[0] + '@' + str(dom),
                str(sur)[0] + '-' + str(name) + '@' + str(dom),
                str(name) + '-' + str(sur) + '@' + str(dom),
                str(name)[0] + '-' + str(sur) + '@' + str(dom),
                str(name) + '-' + str(sur)[0] + '@' + str(dom),
                str(name)[0] + '-' + str(sur) + '@' + str(dom),
                str(sur) + '-' + str(name) + '@' + str(dom),
                str(sur) + '-' + str(name)[0] + '@' + str(dom),
                str(sur) + '-' + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(sur)[:3] + '.' + str(name)[0] + str(patr)[0] + '@' + str(dom),
                str(name)[0] + str(patr)[0] + '.' + str(sur)[:3] + '@' + str(dom),
                'dir' + '@' + str(dom),
                'head' + '@' + str(dom),
                'director' + '@' + str(dom),
                'boss' + '@' + str(dom),
                'main' + '@' + str(dom),
                'lead' + '@' + str(dom),
                'leader' + '@' + str(dom),
                'chief' + '@' + str(dom),
                'ceo' + '@' + str(dom),
                str(dom).split('.')[0] + '@' + str(dom)]

        return all_emails

    def get_mx(self, domain): # get all mx records
        mx_records = []
        for x in dns.resolver.query(domain, 'MX'):
            mx_records.append(x.to_text())
        mx_numbers = [int(mx.split(' ')[0]) for mx in mx_records]
        mx_high_priority = mx_numbers.index(min(mx_numbers))
        return mx_records[mx_high_priority]

    def check_email(self, email, mx): # check email with smtp
        host = socket.gethostname()
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        addressToVerify = email
        server.connect(mx)
        server.helo(host)
        server.mail('me@domain.com')
        code, message = server.rcpt(str(addressToVerify))
        server.quit()
        return code


