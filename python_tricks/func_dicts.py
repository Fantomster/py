func_dict = {
    'cond_a': handle_a,
    'cond_b': handle_b,
}

cond = 'cond_a'
func_dict[cond]()

func_dict.get(cond, handle_default)()



def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_dict('mul', 2, 8))
print(dispatch_dict('unknown', 2, 8))