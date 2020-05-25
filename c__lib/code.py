def snake_case(varname: str):
    retval = ''
    for c in varname:
        if c.isupper():
            retval += '_' + c.lower()
        else:
            retval += c
    return retval


def camel_case(varname: str):
    return ''.join(x.capitalize() or '_' for x in varname.split('_'))


if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
