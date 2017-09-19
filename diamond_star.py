spaceL = 9
spaceR = 9
x=1
while x<15:
    print(' '*spaceL, '*'* x, ' '*spaceR)
    x = x + 2
    spaceL = spaceL - 1
    spaceR = spaceR - 1

spaceBL = 4
spaceBR = 1
y=11
while y > 0:
    print(' '*spaceBL, '*'* y, ' '*spaceBR)
    y = y - 2
    spaceBL = spaceBL + 1
    spaceBR = spaceBR + 1
