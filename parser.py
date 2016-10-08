from symbol import SymbolTable


class HackAsmParser:
    def __init__(self):
        self.Tab = SymbolTable()
        self.var_list = []

    def parse(self, line, line_num):
        if line[0] == '(':
            label = line[1:-1]
            self.Tab.loc_label(label, line_num)
            label_type = 'location label'
            if label in self.var_list:
                self.var_list.remove(label)
                label_type = 'var -> location label'
        elif line[0] == '@':
            label = line[1:]
            if not label.isdigit():
                if label not in self.Tab.constTab:
                    if label not in self.var_list:
                        self.var_list.append(label)
                label_type = 'var'
            else:
                label_type = 'const'
        else:
            label = ''
            label_type = 'null'

        return label + '  ' + label_type

    def alloc_all_var(self):
        print self.var_list
        for name in self.var_list:
            self.Tab.alloc(name)
        return self.get_tab()

    def get_tab(self):
        return self.Tab
