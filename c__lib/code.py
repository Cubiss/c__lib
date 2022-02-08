def snake_case(varname: str):
    if len(varname) < 2:
        return varname.lower()

    retval = ''

    while varname.startswith('_'):
        retval += '_'
        varname = varname[1:]

    varname = varname[0].lower() + varname[1:]

    for c in varname:
        if c.isupper():
            retval += '_' + c.lower()
        else:
            retval += c
    return retval


def pascal_case(varname: str):
    retval = ''

    while varname.startswith('_'):
        retval += '_'
        varname = varname[1:]

    return retval + ''.join(x.capitalize() or '_' for x in snake_case(varname).split('_'))


def camel_case(varname: str):
    if len(varname) == 1:
        return varname.lower()

    retval = ''

    while varname.startswith('_'):
        retval += '_'
        varname = varname[1:]

    pascal = pascal_case(varname)
    return retval + pascal[0].lower() + pascal[1:]


if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
