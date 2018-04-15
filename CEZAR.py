print('Number')
z = int(input())
print('Slovo')
n = input().strip()
a =''
main = 'abcdefghijklmnopqrstuvwxyz'
umain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in n:
    a += main[main(i + z) % len(main)]
for i in n:
    a += umain[umain(i + z) % len(umain)]
print ('Result: ' + a )
