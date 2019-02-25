### 1.python

#### 1.1 正则匹配
- functions
 * re.match
 * re.search
 * re.split
 * re.findall(re.finditer)
 * re.sub 替换字符
 * re.subn (new_str, count) 返回替换次数
    * re.sub(pattern, repl, string, count=0, flags=0) repl: str or func
 * re.escape 自动加转义字符
 ```python
 >>> def dashrepl(matchobj):
        # 进入3次 group(0)分别是 -- -- -
...     if matchobj.group(0) == '-': return ' '
...     else: return '-'
>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
'pro--gram files'
>>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
'Baked Beans & Spam'
```

- re.match and re.search compare
- 限定符(* + ? {n,m})
- 定位符(^ $ /b单词边界 /B非单词边界)
- []
 * [(+*)] 匹配 [ ( + * )
 * \S \w 有效
 * [^3]除了３以外的都匹配
- 常用
 * \b beginning or end of word \B (opposite)
 * \s [\t\n\r\f\v] \S [^\t\n\t\f\v]
 * \w [a-zA-Z0-9_] \W [^a-zA-Z0-9_]
 * \d [0-9] \D [^0-9]
#### 1.2 正则切分
- re.split(':? ', 2) ': space'切分2次
- 只有在正则匹配失败返回[str]
- example
```python
# search match
In [529]: re.search(r'\d', 'afad1fa').group()
Out[529]: '1'
In [531]: re.match(r'\d', 'ab11') is None
Out[531]: True
# 定位符
In [502]: re.match(r'.*\b', 'abc abc').group()
Out[502]: 'abc abc'
In [503]: re.match(r'.*\B', 'abc abc').group()
Out[503]: 'abc ab'
In [504]: re.match(r'.*\B', 'abc abc ').group()
Out[504]: 'abc abc '
>>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']
In [612]: re.split('[\s,]', 'dsfaf ,afads, fasa ')
Out[612]: ['dsfaf', '', 'afads', '', 'fasa', '']
# 切分加上分组的话，返回内容包含切分元素,如果不想包含匹配分组的话，确保分组为非捕获分组
In [613]: re.split('([\s,])', 'dsfaf ,afads, fasa ')
Out[613]: ['dsfaf', ' ', '', ',', 'afads', ',', '', ' ', 'fasa', ' ', '']
```

#### 1.3 分组
- group()匹配的字符串 == group(0)  group(1)第一个分组的内容 如何匹配多次，则取最后一个
- groups() 所有的分组
- \number \g<number> 代表第number个分组,

```python
In [768]: re.match(r'(.+) \1', 'ab ab')
Out[768]: <_sre.SRE_Match at 0x7f5e24ddb828>

In [764]: re.sub(r'(foo)', r'\g<1>123', 'foobar')
Out[764]: 'foo123bar'
```

#### 1.4 贪婪匹配

- example(限定符 + * ? {}默认采用贪婪匹配，+? *? ?? {}?非贪婪)
  * \d+ 采用贪婪匹配
  * \d+? 非贪婪匹配

```python
#  分组
In [719]: m = re.match(r'(..)+', 'a1b2c3')

In [720]: m.group()
Out[720]: 'a1b2c3'

In [721]: m.group(0)
Out[721]: 'a1b2c3'

In [722]: m.group(1)
Out[722]: 'c3'
# 没有匹配到的分组显示 None， 附默认值 m.groups('default')
In [723]: m.groups()
Out[723]: ('c3',)
# greedy
In [378]: re.match(r'^(\d+)(0*)$', '12300').groups()
Out[378]: ('12300', '')

In [379]: re.match(r'^(\d+?)(0*)$', '12300').groups()
Out[379]: ('123', '00')
```

- 分组自定义名字
```python
In [384]: re.match(r'^(\d+?)(?P<a>0*)$', '12300').group('a')
Out[384]: '00'
# (?:exp)
In [386]: re.match(r'^(\d+?)(?:0*)$', '12300').groups()
Out[386]: ('123',)
# (?!exp)
In [418]: re.match(r'1230(?!a|b)', '1230e').group()
Out[418]: '1230'
In [419]: re.match(r'1230(?!a|b)', '1230a') # None
# (?=exp)
In [420]: re.match(r'1230(?=a|b)', '1230a')
Out[420]: <_sre.SRE_Match at 0x7f5e256c67e8>
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
# 非捕获元的占用大小
In [666]: b = re.match('(a)', 'a')
In [667]: b1 = re.match('(?:a)', 'a')
In [668]: b.__sizeof__()
Out[668]: 120
In [669]: b1.__sizeof__()
Out[669]: 104
In [670]: bb = re.match('a', 'a')
In [671]: bb.__sizeof__()
Out[671]: 104
```

- 非捕获元（非获取匹配）
  * (?:exp): 匹配exp，不捕获获匹配文本，也不分配组号（只进行匹配，不缓存匹配内容）
  * (?=exp)正向预查
  * (?!exp)负向预查
  * (?<=exp)
  * (?<!exp)
