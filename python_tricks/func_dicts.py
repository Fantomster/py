func_dict = {
    'cond_a': handle_a,
    'cond_b': handle_b,
}

cond = 'cond_a'
func_dict[cond]()

func_dict.get(cond, handle_default)()