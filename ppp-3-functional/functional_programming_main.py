def flatten_dict(diction):
    
    def decompile_obj(obj, values):
        result = dict()
        for i in values: result[f"{obj}.{i}"] = values[i]
        return result

    result = dict()

    for i in diction:
        if isinstance(diction[i], dict): result.update(decompile_obj(i, diction[i]))
        else: result[i] = diction[i]
    return result

def unflatten_dict(diction):
    # create a list of objects i need
    result = dict()

    # iterate over diction
    for i in diction:
        # Test if nested
        if '.' in i:
            outer_name = i[0:1]
            inner_name = i[2::]
            # check if outer exists
            if outer_name in result:
                result[outer_name].update({inner_name: diction[i]})
            else:
                result.update({outer_name: {inner_name: diction[i]}})
        else: result[i] = diction[i]
    return result



def treemap(func, in_list):  
    new_list = in_list
    for i in range(0, len(in_list)):
        new_list[i] = func(new_list[i]) if not isinstance(new_list[i], list) else treemap(func, new_list[i])
    return new_list

print(treemap(lambda x: x*x, [1, 2, [4, [5]]]))





print(flatten_dict({'a':'1','b':{'i': '3', 'j': '7'},"c":'P'}))

print(unflatten_dict({'a.g': '4', 'b.i': '7', 'n': '1', 'p': '0', 'b.j': '1', 'a.a': '99'}))