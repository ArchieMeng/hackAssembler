import re
from coder import HackAsmCoder
from parser import HackAsmParser
import sys


if len(sys.argv) == 1:
    file_name = ['Add.asm']
else:
    file_name = list(sys.argv[1:])

for name in file_name:

    print '-----------' + name + '----------\n'
    asmFile = open(name, 'r')
    parser = HackAsmParser()
    i = 0

    src_codes = []

    for line in asmFile:
        if line[0:2] != '//':
            line = re.sub('[ \r\t\n]', '', line)
            line = re.sub('//.*', '', line)
            if line is not '':
                print line
                src_codes.append(line)
                print 'parser output:\t' + parser.parse(line, i)
                if '(' in line:
                    i -= 1
                i += 1

    asmFile.close()

    print src_codes

    write_file = open(name.replace('asm','hack'),'w')
    coder = HackAsmCoder(parser.alloc_all_var())
    print '\n'
    for line in src_codes:
        line = re.sub('[ \t\n]', '', line)
        print line
        code = coder.code(line)
        if code is not None:
            print 'coder output:\t' + code
            write_file.write(code+'\r')
    write_file.close()
    print '------------' + name + '-------------\n'