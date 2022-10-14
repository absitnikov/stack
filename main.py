from stack_data import balance_check


if __name__ == '__main__':

    print(balance_check('(((([{}]))))'))
    print(balance_check('[([])((([[[]]])))]{()}'))
    print(balance_check('{{[()]}}'))
    print(balance_check('}{}'))
    print(balance_check('{{[(])]}}'))
    print(balance_check('[[{())}]'))


