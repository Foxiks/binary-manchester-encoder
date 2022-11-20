import binascii
from manchester_code import encode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input binary CADU file")
parser.add_argument("-o", "--output", help="Output binary CADU file with manchester code")
args = parser.parse_args()

inputfile = args.input
outfile = args.output
print("Reading input")
f = open(inputfile, 'rb')
x = f.read()
print("Encoding")
manchester_code = encode(x)
nman = (''.join(f'{m:08b}' for m in manchester_code))
data = '%08X' % int(nman, 2)
print("Writing output")
with open(outfile, 'wb') as f:
    binstr = binascii.unhexlify(data)
    f.write(binstr)
    f.close()
print("Done!")