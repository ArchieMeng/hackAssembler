class SymbolTable:
    def __init__(self):
        self.cmpTab = {
            "@": "0",
            "INS": "111",
            "0": "0101010",
            '1': '0111111',
            '-1': '0111010',
            'D': '0001100',
            '!D': '0001101',
            'A': '0110000',
            'M': '1110000',
            '!A': '0110001',
            '!M': '1110001',
            '-D': '0001111',
            '-A': '0110011',
            '-M': '1110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'M+1': '1110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'M-1': '1110010',
            'D+A': '0000010',
            'D+M': '1000010',
            'D-A': '0010011',
            'D-M': '1010011',
            'A-D': '0000111',
            'M-D': '1000111',
            'D&A': '0000000',
            'D&M': '1000000',
            'D|A': '0010101',
            'D|M': '1010101'
        }
        self.dstTab = {
            'null': '000',
            'M': '001',
            'D': '010',
            'A': '100',
            'MD': '011',
            'AD': '110',
            'AM': '101',
            'AMD': '111'
        }
        self.jmpTab = {
            'null': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }
        self.constTab = {
            'SP': '{0:015b}'.format(0x0),
            'LCL': '{0:015b}'.format(0x1),
            'ARG': '{0:015b}'.format(0x2),
            'THIS': '{0:015b}'.format(0x3),
            'THAT': '{0:015b}'.format(0x4),
            'SCREEN': '{0:015b}'.format(0x4000),
            'KBD': '{0:015b}'.format(0x6000)
        }
        # set R const value
        for i in range(0,16):
            self.constTab['R'+str(i)] = '{0:015b}'.format(i)

        self.freeLoc = 16

    def get_comp(self):
        return self.cmpTab

    def get_jmp(self):
        return self.jmpTab

    def get_const(self):
        return self.constTab

    def get_dst(self):
        return self.dstTab

    def alloc(self, var_name):
        self.constTab[var_name] = '{0:015b}'.format(self.freeLoc)
        self.freeLoc += 1

    def loc_label(self, label, line_num):
        self.constTab[label] = '{0:015b}'.format(line_num)
