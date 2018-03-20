from pprint import pprint
import string
import sys
import copy
from collections import OrderedDict

def eight_queen(x, y, matrix_size,attack,chess_m,queen_pos,queen_count, check_x_line, check_y_line):
    d2 = {'x':x,'y':y}
    if(check_y_line == matrix_size):
        x = (x+1) % matrix_size
        check_x_line +=1
        check_y_line = 0

    if(check_x_line == matrix_size):
        each_step ={}
        each_step['final']=queen_pos
        each_step['queen_count']=queen_count
        each_step['map'] = chess_m
        #print(each_step)
        return each_step
    total_attac_m = put_attack(attack,x,y)
    
    
    put = put_or_not(chess_m, x,y)
    if put:
        queen_count+=1
#        print(queen_count)
#        print('queenOuO')
#        print(queen_count)
        queen_pos[x][y]='1'
#        print(queen_pos)
        chess_m[x][y]=True
        chess_m = set_it_in(chess_m, total_attac_m)
#        print(chess_m)
        return eight_queen(x,(y+1)% matrix_size,matrix_size,attack,chess_m,queen_pos,queen_count, check_x_line, check_y_line+1)
    return eight_queen(x,(y+1)%matrix_size,matrix_size,attack,chess_m,queen_pos,queen_count, check_x_line, check_y_line+1)



def put_attack(attack_range, x,y):
    total_attac_m=[]
    total_attac_m_2 = []
    up = []
    right = []
    down = []
    left = []
    ri_up = []
    ri_do = []
    le_up = []
    le_do = []
    for i in range(attack_range-1):
        j = i+1
        d2_up = {}
        d2_up['x']=x
        d2_up['y']= (y+j)
#        print(d2_nf)
        up.append(d2_up)
#        print(up)
        #right
        d2_ri={}
        d2_ri['x']=(x+j)
        d2_ri['y']=y
#        print(d2_n)
        right.append(d2_ri)
        #down
        d2_do={}
        d2_do['x']= x
        d2_do['y']= (y-j)
        down.append(d2_do)
        #left
        d2_le ={}
        d2_le['x'] = (x-j)
        d2_le['y'] = y
        left.append(d2_le)
        #right_up
        d2_ru = {}
        d2_ru['x'] = (x+j)
        d2_ru['y'] = (y+j)
        ri_up.append(d2_ru)
        #left_down
        d2_ld ={}
        d2_ld['x'] = (x-j)
        d2_ld['y'] = (y-j)
        le_do.append(d2_ld)
        #right_down
        d2_rd = {}
        d2_rd['x'] = (x+j)
        d2_rd['y'] = (y-j)
        ri_do.append(d2_rd)
        #left_up
        d2_lu = {}
        d2_lu['x'] = (x-j)
        d2_lu['y'] = (y+j)
        le_up.append(d2_lu)

#    print(up)
    total_attac_m.append(up)
#    print(total_attac_m)
    total_attac_m.append(right)
    total_attac_m.append(down)
    total_attac_m.append(left)
    total_attac_m.append(ri_up)
    total_attac_m.append(le_do)
    total_attac_m.append(ri_do)
    total_attac_m.append(le_up)

    for i in range(len(total_attac_m)):
#        print(total_attac_m[i])
        total_attac_m_temp = []
        for j in range(len(total_attac_m[i])):
            temp_x = total_attac_m[i][j]['x']
            temp_y = total_attac_m[i][j]['y']
#            print(temp_x)
#            print(temp_y)
            if temp_x < matrix_size and temp_x >= 0 and temp_y < matrix_size and temp_y >=0:
                total_attac_m_temp.append(total_attac_m[i][j])
        total_attac_m_2.append(total_attac_m_temp)

    return total_attac_m_2

def print_it(total_step):
    temp_count = 0
    for i in range(len(total_step)):
        if int(total_step[i]['queen_count']) > temp_count:
            temp_count = total_step[i]['queen_count']
            temp = total_step[i]
    temp_z = temp['final']
    temp_m = temp['map']
 #    print(temp_z)
    print("best count of queen:", temp['queen_count'])
    for i in range(len(temp_z)):
        line_count = int(len(temp_z)-i-1)
#        print(line_count)
        print(temp_z[line_count])
    for i in range(len(temp_m)):
        line_count = int(len(temp_m)-i-1)
#        print(line_count)
        print(temp_m[line_count])
 
def put_or_not(matric_list,x,y):
    put = True
    # if can put put==True
 #    print(list_want_put)
 #    for i in range(len(list_want_put)):
 #        for j in range(len(list_want_put[i])):
 #            temp_x = list_want_put[i][j]['x']
 #            temp_y = list_want_put[i][j]['y']
  #           print(temp_x,temp_y)
  #           print(matric_list)
            # if ==True that some can attack so can't put
    if matric_list[x][y] == True:
            put = False
    return put
 
def set_it_in(matric_list, list_put_in):
    for i in range(len(list_put_in)):
        for j in range(len(list_put_in[i])):
            temp_x = list_put_in[i][j]['x']
            temp_y = list_put_in[i][j]['y']
            matric_list[temp_x][temp_y] = True
    return matric_list
 
def user_input_queen(input_queen_c,matrix_size):
    queen_input_list = []
    i=0
    while i < input_queen_c:
        queen_position = {}
        queen_position['y']=int(input('queen x '+str(i)+' is:'))-1
        queen_position['x']=int(input('queen y '+str(i)+' is:'))-1
        if queen_position['x']>matrix_size-1 or queen_position['y']> matrix_size-1 or queen_position['x'] <0 or queen_position['y']<0:
            print("The queen position is put of matrix, please re-input the point!!")
        else:
            i+=1
            queen_input_list.append(queen_position)
    return queen_input_list



def check_legal_or_not(input_queen_list, matric_list,attack_range,queen_pos):
    first_input={}
    for i in range(len(input_queen_list)):
        temp_x = input_queen_list[i]['x']
        temp_y = input_queen_list[i]['y']
        put = put_or_not(matric_list, temp_x,temp_y)
        if put == False:
            print("You enter legal point! Please restart!")
            sys.exit()
        else:
            attack_m = put_attack(attack_range,temp_x,temp_y)
            queen_pos[temp_x][temp_y]='1'
            matric_list[temp_x][temp_y]=True
            matric_list = set_it_in(matric_list,attack_m)
    first_input['matrix'] = matric_list
    first_input['queen_pos'] = queen_pos
    return first_input



if __name__ == '__main__':

    queen_count_input = int(input("How many queen you want to put?:"))
    matrix_size = 8
    attack = 4
    temp_dic = {}

    chess_m = [[False for x in range(matrix_size)] for y in range(matrix_size)]
    
    chess_m_2 = [[False for x in range(matrix_size)] for y in range(matrix_size)]
    queen_pos = [['0' for x in range(matrix_size)] for y in range(matrix_size)]
    total_step = []
    queen_input_list = user_input_queen(queen_count_input,matrix_size)
    first_input = check_legal_or_not(queen_input_list, chess_m,attack,queen_pos)
    chess_m = first_input['matrix']
    queen_pos = first_input['queen_pos']

#    for i in range(len(queen_pos)):
#        line_count = int(len(queen_pos)-i-1)
#        print(line_count)
#        print(queen_pos[line_count])
#    for i in range(len(chess_m)):
#        line_count = int(len(chess_m)-i-1)
##        print(line_count)
#        print(chess_m[line_count])
    chess_m_2 = copy.deepcopy(chess_m)
    queen_pos_2 = copy.deepcopy(queen_pos)
#    print()
    queen_count=copy.deepcopy(queen_count_input)
#    print(queen_count)
    for x in range(matrix_size-1):
        for y in range(matrix_size-1):
            a= {}
            a = eight_queen(x,y,matrix_size,attack,chess_m_2,queen_pos_2,queen_count,0,0)
#            print(a)
            total_step.append(a)
            chess_m_2 = copy.deepcopy(chess_m)
            queen_pos_2 = copy.deepcopy(queen_pos)
            queen_count = copy.deepcopy(queen_count_input)
#    print_it(total_step)
    print_it(total_step)
