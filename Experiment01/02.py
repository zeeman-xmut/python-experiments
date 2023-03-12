# -*- coding: utf-8 -*-
money_str = input('请输入带符号（人民币 ￥，美元 $）的货币值：')
if money_str[0] == '￥':
    print('{}人民币转换为美元为${:.2f}'.format(money_str, eval(money_str[1:]) / 6))
elif money_str[0] == '$':
    print('{}美元转换为人民币为￥{:.2f}'.format(money_str, eval(money_str[1:]) * 6))
else:
    print('输入格式错误')
