__author__ = 'Administrator'
'''正则表达
--------字符--------
.  --匹配任意字符，除\n,datall模式可以匹配换行符
\  --转译字符
[...] ---字符集

--------预定义字符集可以写在[...]中---------
\d    --数字0-9
\D    --非数字
\s    --空白字符[<空格>\t\r\n\f\v]
\S    --非空白字符[^\s]
\w    --单词字符：[A-Za-z0-9]
\W    --非单词字符[^\w]

--------数量词用在字符域(...)之后--------
*     --匹配前一个字符0或无限次
+     --匹配前一个字符1或无限次
？    --匹配前一个字符0或者1次
{m}   --匹配前一个字符m次
{m,n} --匹配前一个字符m至n次（省略m则为0到n，省略n则为m到无限次）

--------边界匹配（不消耗待匹配字符串中的字符）------
^     --匹配字符串开头，多行匹配每一行开头
$     --匹配字符串结尾，多行匹配每一行结尾
\A    --仅匹配字符串开头。
\Z    --仅匹配字符串结尾。
\b    --匹配\w和\W之间  ？？？？
\B    --[^\b]

--------逻辑，分组--------
|     --代表左右表达式任意匹配一个例子 abc|def,匹配左边或者右边均可
(...) --被括起来的表达式将作为一个分组，每一个分组有编号，从左一次加1，分组作为一个整体后面可以接数量词
(?P<name>...) --分组除了有编号之外还可以有别名
\<number>     --引用编号为number的分组匹配到的字符串 (ww)abc\1 -->wwabcww
(?)P=name     --引用别名为name的分组匹配到字符串    (?P<id>\d)asn(?P=id)  6asn6

--------特殊构造（不作为分组）--------
(?:...)      --(...)的不分组版本，用于使用|或者后接数量词
(?iLmsux)    --iLmsux的每一个字母代表一种匹配模式，只能用在正则表达式的开头，可以选多个
(?#...)      --#后的内容作为注释忽略掉
(?=...)      --之后的内容需要匹配表达式才能匹配成功，不消耗字符串内容  a(?=\d)
(?!...)      --之后的内容需要不匹配表达式才能匹配成功，不消耗字符串内容 a(?!\d)
(?<=...)     --之前的字符串内容需要匹配表达式才能匹配成功，不消耗字符串内容  (?<=\d)a
(?<!...)     --之前的字符串内容需要匹配表达式才能匹配成功，不消耗字符串内容  (?<!\d)a
(?(id/name))  --如果编号为id，别名为name的组匹配到字符，则需要
yes-pattern|    匹配yes-pattern，否则则需要匹配no-pattern   (\d)abc(?(1)/d|abc)
no-pattern)

'''
import re

import re

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(p.sub(r'\2 \1', s))
print(s)
#sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]):
def func(m):
    print(m.group(1))
    print(m.group(1).title() + ' ' + m.group(2).title())
    return m.group(1).title() + ' ' + m.group(2).title()

#print(p.sub(func, s))
kk=p.subn(func, s)
print(kk[1])
'''
pattern = re.compile(r'(world)')
mm=pattern.finditer('hello world!as world world')
for m in pattern.finditer('hello world!as world world'):
    print('group is:'+m.group())
    print(m.span())
'''
'''
if m:
    # 使用Match获得分组信息
    print(m.group)
else:
    print('no group')
'''
'''
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
m = re.match(r'hello world!', 'hello world!')

print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)

#print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
#print("m.start(2):", m.start(2))
#print("m.end(2):", m.end(2))
#print("m.span(2):", m.span(2))
#print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))

### output ###
# m.string: hello world!
# m.re: <_sre.SRE_Pattern object at 0x016E1A38>
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(1,2): ('hello', 'world')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\2 \1\3'): world hello!
'''


