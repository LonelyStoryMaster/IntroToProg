import struct

print('Result of unpacking %s:' % repr('\x00\x05'), end=' ')
print(struct.unpack('>h', b'\x00\x05'))


print('Result of unpacking %s:' % repr('\x01\x00'), end=' ')
print(struct.unpack('>h', b'\x01\x00'))

print('Result of unpacking %s:' % repr('\x00\x05\x01\x00'), end=' ')
print(struct.unpack('>hh', b'\x00\x05\x01\x00'))