class Calculator(object):
    def evaluate(self, string):
        string_list = string.split(' ')
        count_par = string_list.count('(')
        for n in range(count_par):
            for i, elem in enumerate(string_list):
                if elem == '(':
                    ix_open = i
                if elem == ')':
                    ix_close = i
                    break

            sub_calcul = string_list[ix_open+1: ix_close]
            print(sub_calcul)
            res = self.internal_calcul(sub_calcul)
            del string_list[ix_open: ix_close+1]
            print(string_list)
            string_list.insert(ix_open, str(res))

        res = self.internal_calcul(string_list)

        return res

    def internal_calcul(self, string_list):
        string_list = [float(elem) if elem.replace('.', '').isdigit() else elem for elem in string_list]
        for char in ['/', '*']:
            count = string_list.count(char)
            for n in range(count):
                ix = string_list.index(char)
                if char == '/':
                    res = string_list[ix-1] / string_list[ix+1]
                elif char == '*':
                    res = string_list[ix-1] * string_list[ix+1]       

                del string_list[ix-1: ix+2]
                string_list.insert(ix-1, res)

        print(string_list)
        count = string_list.count('+') + string_list.count('-')
        for n in range(count):
            if '+' in string_list and '-' in string_list:
                ix = min(string_list.index('+'), string_list.index('-'))
            else:
                if '+' in string_list:
                    ix = string_list.index('+')
                else:
                    ix = string_list.index('-')

            char = string_list[ix]
            if char == '+':
                res = string_list[ix-1] + string_list[ix+1]
            elif char == '-':
                res = string_list[ix-1] - string_list[ix+1]          

            del string_list[ix-1: ix+2]
            string_list.insert(ix-1, res)
            print(string_list)

        res = string_list[0]

        return res
