#Python Challange

#1
x = 2**38
print '1 is ' + str(x)


#2
import string

original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc " \
    "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq " \
    "rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu " \
    "ynnjw ml rfc spj."

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

print original.translate(table)



#3
theory = """}#)$[]_+(^_@^][]_)*^*+_!{&$##]((](}}{[!$#_{&{){
*_{^}$#!+]{[^&++*#!]*)]%$!{#^&%(%^*}@^+__])_$@_^#[{{})}$*]#%]{}{][@^!@)_[}{())%)
())&#@*[#}+#^}#%!![#&*}^{^(({+#*[!{!}){(!*@!+@[_(*^+*]$]+@+*_##)&)^(@$^]e@][#&)(
%%{})+^$))[{))}&$(^+{&(#%*@&*(^&{}+!}_!^($}!(}_@@++$)(%}{!{_]%}$!){%^%%@^%&#([+[
_+%){{}(#_}&{&++!@_)(_+}%_#+]&^)+]_[@]+$!+{@}$^!&)#%#^&+$@[+&+{^{*[@]#!{_*[)(#[[
]*!*}}*_(+&%{&#$&+*_]#+#]!&*@}$%)!})@&)*}#(@}!^(]^@}]#&%)![^!$*)&_]^%{{}(!)_&{_{
+[_*+}]$_[#@_^]*^*#@{&%})*{&**}}}!_!+{&^)__)@_#$#%{+)^!{}^@[$+^}&(%%)&!+^_^#}^({
*%]&@{]++}@$$)}#]{)!+@[^)!#[%@^!!"""

#theory = open("temp.txt")

key = "#@!$%+{}[]_-&*()*^@/"
new2 =""

print()
for letter in theory:
    if letter not in key:
        new2 += letter

print(new2)