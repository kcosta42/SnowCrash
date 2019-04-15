with open('/usr/sbin/john', 'r') as f:
  passwd = f.read()[:-1]
  for i in range(26):
    cipher = []
    for c in passwd:
      c = ((ord(c) - 97 + i) % 26) + 97
      cipher.append(chr(c))
    print('+%d: %s'% (i, ''.join(cipher)))
