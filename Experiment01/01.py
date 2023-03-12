# -*- coding: utf-8 -*-
temp_str = input('请输入带有符号的温度值：')
if temp_str[-1] in ['f', 'F']:
    temp_c = (eval(temp_str[:-1]) - 32) / 1.8
    print('转换后的温度是{:.2f}C'.format(temp_c))
elif temp_str[-1] in ['c', 'C']:
    temp_f = 1.8 * eval(temp_str[:-1]) + 32
    print('转换后的温度是{:.2f}F'.format(temp_f))
else:
    print('输入格式错误')
