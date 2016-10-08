from symbol import SymbolTable


class HackAsmCoder:
    def __init__(self, table=SymbolTable):
        self.Tab = table

    def code(self, line):

        def combine_ins(comp, dst, jmp='null'):
            return self.Tab.get_comp()['INS'] + self.Tab.get_comp()[comp] + self.Tab.get_dst()[dst] + self.Tab.get_jmp()[jmp]

        if line[0] == '(':
            pass
        elif line[0] == '@':
            if line[1:] in self.Tab.constTab:
                return self.Tab.cmpTab['@'] + self.Tab.constTab[line[1:]]
            # assign const int
            else:
                return self.Tab.cmpTab['@'] + '{0:015b}'.format(int(line[1:]))
        elif ';' in line:
            param = line.split(';')
            comp = param[0]
            jmp = param[1]

            if '=' in line:
                param = comp.split('=')
                dst = param[0]
                comp = param[1]
            else:
                dst = 'null'
            return combine_ins(comp, dst, jmp)
        else:
            param = line.split('=')
            dst = param[0]
            comp = param[1]
            return combine_ins(comp, dst)