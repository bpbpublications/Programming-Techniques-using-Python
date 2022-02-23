s1 = '  python  '
print(s1.lstrip()) # -- ls1
s2 = "@@@@@,,,,....phew.....super"
print(s2.lstrip('.,@whep')) # -- ls2
s3 = 'https://www.abc.com'
print(s3.lstrip('spth:/w.')) # -- ls3
print(s3.lstrip('spth:/')) # -- ls4
