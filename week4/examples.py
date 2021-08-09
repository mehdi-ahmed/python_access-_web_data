# ord() tells us the numeric value of a simple ASCII character

# 8 bits of memory = 1 byte. This sdd is 100 Giga Bytes

print(ord('H'))  # 72
print(ord('Z'))  # 90
print(ord('\n'))  # 10
print(ord('*'))  # 42
print(ord('i'))  # 42

# lower cases are higher than uppercase 'Hi' < 'hi'
# UTF-16 = Fixed Length - Two Bytes
# UTF-32 = Fixed Length - Four Bytes
# UTF-8 = Recommended. Overlaps with ASCII

x = 'حوار الكاتبة ألفة يوسف في هنا شمس'
print(type(x))  # <class 'str'>

y = b'ABC'
print(type(y))  # <class 'bytes'>
# For Python 3 , all strings internally are UNICODE

# When we talk to a DB or network resources using sockets, we have to encode and decode data(usually to UTF-8)
# But reading data from files just works natively
