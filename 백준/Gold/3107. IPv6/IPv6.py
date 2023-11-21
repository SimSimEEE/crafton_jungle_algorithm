ipv6 = input()
cnt = ipv6.count(':')
ipv6 = ipv6.replace('::', ':' * (8 - cnt + 1))
ipv6 = ipv6.split(':')
for i in range(len(ipv6)):
    if ipv6[i] == '':
        ipv6[i] = '0000'
    else:
        ipv6[i] = '0' * (4 - len(ipv6[i])) + ipv6[i]
print(':'.join(ipv6))