# chapter02-01
# 파이썬 완전 기초과정
# Print 사용법

# 기본 출력
print("Python Start!")
print('Python Start!')
print('''Python Start!''')
print("""Python Start!""")

print()

# seporator 옵션
# sep사이의 띄어쓰기 간격이 자간간격
print('P', 'Y', 'T', 'H', 'O', 'N', sep='    ')
print("P", "Y", "T", "H", "O", "N", sep=' ')
print("010", "6784", "4311", sep='-')
print('kminsuk123', 'gmail.com', sep='@')

print()

# end옵션

print('Welcome to', end='  ')
print('IT News', end='-')
print('Web Site')

# file옵션
import sys

print('Learn Python', file=sys.stdout)

print()
# format 사용(d : 3, s : 'python', f : 3.14159265)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', '2'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:@>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%5s' % ('nice'))
print('%5s' % ('pythonstudy'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f
print('%f' % (3.14159265358979))
print('%1.8f' % (3.14159265))
print('{:f}'.format(3.14159265358979))

print('%06.2f' % (3.14159265358979))
print('{:06.2f}'.format(3.141592653589)) 
