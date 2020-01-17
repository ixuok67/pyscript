import argparse


#8D679D3711D3E4981000E787EC6DE8A4
def is_bstr_format(s):
    if len(s) == 32 and s.isalnum():
        return True
    return False


#4B43EC55-1FC0-4891-ACD3-F51A5662F1E3
def is_uuid_format(s):
    if len(s) == 36 and s.count('-') == 4 and s.replace('-', '1').isalnum():
        return True
    return False


#{ 0x8d679d37, 0xe498, 0x11d3, { 0x87, 0xe7, 0x00, 0x10, 0xa4, 0xe8, 0x6d, 0xec } }
def is_def_format(s):
    if len(s) == 82 and s.count('0x') == 11:
        if s.replace('0x', '1').replace(' ', '1').replace(',', '1').replace('{', 1).replace('}', 1).isalnum():
            return True
    return False


def convert_uuid_to_bstr(s):
    return s[:8] + s[14:18] + s[9:13]+ s[26:28]+s[24:26]+s[21:23]+s[19:21]+s[34:36]+s[32:34]+s[30:32]+s[28:30]


def convert_bstr_to_uuid(s):
    return s[:8]+'-'+s[12:16]+'-'+s[8:12]+'-'+s[22:24]+s[20:22]+'-'+s[18:20]+s[16:18]+s[30:32]+s[28:30]+s[26:28]+s[24:26]


def convert_bstr_to_def(s):
    return '{ 0x'+s[:8]+', 0x'+s[12:16]+', 0x'+s[8:12]+', { 0x'+s[22:24]+', 0x'+s[20:22]+', 0x'+s[18:20]+', 0x'+s[16:18]+', 0x'+s[30:32]+', 0x'+s[28:30]+', 0x'+s[26:28]+', 0x'+s[24:26]+' } }'


def convert(s):
    if is_bstr_format(s):
        return convert_bstr_to_uuid(s)
    elif is_uuid_format(s):
        return convert_uuid_to_bstr(s)
    return s


def convert_to_fomat(s, format):
    if format == 'b' and is_uuid_format(s):
        return convert_uuid_to_bstr(s)
    elif format == 'r' and is_bstr_format(s):
        return convert_bstr_to_uuid(s)
    elif format == 'd' and is_bstr_format(s):
        return convert_bstr_to_def(s)
    else:
        return s


def convert2mode(s, bstr_mode):
    if (bstr_mode is True and not is_bstr_format(s)) or (bstr_mode is not True and not is_uuid_format(s)):
        return convert(s)
    else:
        return s

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GUID Convertor')
    parser.add_argument('-input', help='If no output form is specified, input BSTR format, it will output registry format, and otherwise')
    parser.add_argument('-output', help='Output format, b for BSTR format, r for registry format, d for definition format')
    arg_result = parser.parse_args()

    output_s = convert_to_fomat(arg_result.input, arg_result.output)
    print('convert result: {}'.format(output_s))