import zlib

# data = open('lorem.txt', 'r').read()

data = "06bc902e-7f36-11e4-aa78-e71d68be9c69"

cksum = zlib.adler32(data)
print 'Adler32: %12d' % cksum
print '       : %12d' % zlib.adler32(data, cksum)

cksum = zlib.crc32(data)
print 'CRC-32 : %12d' % cksum
print '       : %12d' % zlib.crc32(data, cksum)