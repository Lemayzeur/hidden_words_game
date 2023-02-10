import random
import string

# Direksyon ki disponib yo
dir_list = [
  ('HRZ', (0,1)),  # orizontal
  ('-HRZ', (0,-1)), # orizontal alanvè
  ('VTC', (1,0)), # vètikal
  ('-VTC', (-1,0)), #vètikal alanvè
  
  # TODO: Ajoute afichaj dyagonal
  #('DGNL', (1,1)),
  #('-DGNL', (-1,-1)),
  #('DGNR', (1,-1)), 
  #('-DGNR', (-1,1)),
]

# Lis mo yo
words = ['LUB', 'LORRY']
mx = my = 10 # pwen maksimal yo

# Jenere matris lèt aleyatwa yo
matrix = [[f'{random.choices(string.ascii_uppercase)}' for y in range(mx)] for x in range(mx)]

# Memorize lèt ak pozisyon ki jenere deja yo, pou jere entèseksyon lèt yo
taken_pos = [] # TODO: Sa pa ko fèt

for w in words:
    # chwa aleyatwa pozisyon demaraj yon mo ki pral afiche
    sp = (random.randint(0, mx-1), random.randint(0, my-1)) # sarting_point
    
    while True: # tanke pozisyon ak direksyon an depase matris la, kontinye rechwazi.
        # chwa aleyatwa direksyon mo ki pral afiche a.
        direction = random.choice(dir_list)
        
        # Kantite deplasman X,Y ki pral gen pou fèt. Ek. "Hello" => 5lèt * 1 = 5 deplasman
        move1 = len(w) * direction[1][0]
        move2 = len(w) * direction[1][1]
        
        if move1 + sp[0] >= 0 and move2 + sp[1] >= 0 and move1 + sp[0] < mx and move2 + sp[1] < my:
            break

    # Mete mo yo, an majiskil
    w = w.upper()
    
    stepx = 1 if move1 >= 0 else -1 # Step +1 oubyen -1 (annavan, alanvè)
    stepy = 1 if move2 >= 0 else -1
    
    endx = sp[0] + 1 if move1 == 0 else sp[0] + move1 # Pwen final X, entèval yo
    endy = sp[1] + 1 if move2 == 0 else sp[1] + move2 # Pwen final Y, entèval yo
    count = 0 # kontè chak lèt mo a
    
    # Afichaj chak lèt nan matris ki te jenere a
    for i in range(sp[0], endx, stepx):
        for j in range(sp[1], endy, stepy):
            matrix[i][j] = f'[{w[count]}]'
            taken_pos.append([(i,j), w[count]]) # Anrejistre mo ak pozisyon ki chwazi a
            count += 1

# Afichaj jeneral matris la nan fòma yon matris kare.
for x in range(mx):
    for y in range(mx):
        print(matrix[x][y], end='\t')
    print('\n')
