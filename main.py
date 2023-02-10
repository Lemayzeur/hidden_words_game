import random
import string

# Direksyon ki disponib yo
dir_list = [
  ('HRZ', (0,1)), 
  ('-HRZ', (0,-1)),
  ('VTC', (1,0)), 
  ('-VTC', (-1,0)),
  
  #('DGNL', (1,1)),
  #('-DGNL', (-1,-1)),
  #('DGNR', (1,-1)), 
  #('-DGNR', (-1,1)),
]

# Lis mo yo
words = ['LUB', 'LORRY']
mx = my = 10
matrix = [[(x,y) for y in range(mx)] for x in range(mx)]

taken_pos = []
for w in words:
    sp = (random.randint(0, mx-1), random.randint(0, my-1)) # sarting_point
    direction = random.choice(dir_list) # direksyon afichaj mo a
    
    while True:
        print(taken_pos)
        move1 = len(w) * direction[1][0]
        move2 = len(w) * direction[1][1]
        direction = random.choice(dir_list) # direksyon afichaj mo a
        print(move1+sp[0], move2+sp[1])
        if move1 + sp[0] >= 0 and move2 + sp[1] >= 0 and move1 + sp[0] < mx and move2 + sp[1] < my:
            break

    w = w.upper()
    
    stepx = 1 if move1 >= 0 else -1
    stepy = 1 if move2 >= 0 else -1
    endx = sp[0] + 1 if move1 == 0 else sp[0] + move1
    endy = sp[1] + 1 if move2 == 0 else sp[1] + move2
    count = 0
    for i in range(sp[0], endx, stepx):
        for j in range(sp[1], endy, stepy):
            matrix[i][j] = f'[{w[count]}]'
            taken_pos.append([(i,j), w[count]])
            count += 1

for x in range(mx):
    for y in range(mx):
        print(matrix[x][y], end='\t')
    print('\n')
