from pprint import pprint
import string
import sys
import copy

if sys.version_info[0] < 3:
    import Tkinter as tk #if python3, import tkinter
else:
    import tkinter as tk
    
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
        return each_step
    total_attac_m = put_attack(attack,x,y,matrix_size)
    
    
    put = put_or_not(chess_m, x,y)
    if put:
        queen_count = queen_count + 1
        queen_pos[x][y]='1'
        chess_m[x][y]=True
        chess_m = set_it_in(chess_m, total_attac_m)
        return eight_queen(x,(y+1)%matrix_size,matrix_size,attack,chess_m,queen_pos,queen_count, check_x_line, check_y_line+1)
    return eight_queen(x,(y+1)%matrix_size,matrix_size,attack,chess_m,queen_pos,queen_count,check_x_line, check_y_line+1)


def put_attack(attack_range, x,y, matrix_size):
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
        up.append(d2_up)

        #right
        d2_ri={}
        d2_ri['x']=(x+j)
        d2_ri['y']=y
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

    total_attac_m.append(up)
    total_attac_m.append(right)
    total_attac_m.append(down)
    total_attac_m.append(left)
    total_attac_m.append(ri_up)
    total_attac_m.append(le_do)
    total_attac_m.append(ri_do)
    total_attac_m.append(le_up)

    for i in range(len(total_attac_m)):
        total_attac_m_temp=[]
        for j in range(len(total_attac_m[i])):
            temp_x = total_attac_m[i][j]['x']
            temp_y = total_attac_m[i][j]['y']
            if temp_x < matrix_size and temp_x >= 0 and temp_y < matrix_size and temp_y >=0:
                total_attac_m_temp.append(total_attac_m[i][j])
        total_attac_m_2.append(total_attac_m_temp)

    return total_attac_m_2

      
def print_it_GUI(total_step, scale):
    temp_count = 0
    
    for i in range(len(total_step)):
        if int(total_step[i]['queen_count']) > temp_count:
            temp_count = total_step[i]['queen_count']
            temp = total_step[i]
            
    temp_z = temp['final']
    temp_m = temp['map']
 
    label.configure(text="best count of queen:"+ str(temp['queen_count']))
    for i in range(len(temp_z)):
        line_count = int(len(temp_z)-i-1)
        for j in range(len(temp_z)):
            if((temp_z[line_count][j]) == '1'):
                cvs.create_rectangle(j*scale, i*scale, j*scale +scale, i*scale +scale, fill = "black")
            elif((temp_z[line_count][j]) == '2'):
                cvs.create_rectangle(j*scale, i*scale, j*scale +scale, i*scale +scale, fill = "red")
            else:
                cvs.create_rectangle(j*scale, i*scale, j*scale +scale, i*scale +scale, fill = "white")
        
 
def put_or_not(matric_list,x,y):
    put = True

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

def check_legal_or_not(input_queen_list, matric_list,attack_range,queen_pos):
    first_input={}
    for i in range(len(input_queen_list)):
        temp_x = input_queen_list[i]['x']
        temp_y = input_queen_list[i]['y']
        put = put_or_not(matric_list, temp_x,temp_y)
        if put == False:
            win2=tk.Tk()
            win2.title("AI_midTerm")
            win2.resizable(0,0)
            
            label = tk.Label(win2, text="You enter illegal point! Please restart!")
            label.grid(column=1,row=2, padx=10, pady=10)

            win2.mainloop()
            return False
            
        else:
            attack_m = put_attack(attack_range,temp_x,temp_y, 8)
            queen_pos[temp_x][temp_y]='1'
            matric_list[temp_x][temp_y]=True
            matric_list = set_it_in(matric_list,attack_m)
    first_input['matrix'] = matric_list
    first_input['queen_pos'] = queen_pos
    return first_input
 
 
def clickProj1():
    global current_mode
    current_mode = 1
    main_win.destroy()
            
def clickProj2():
    global current_mode
    current_mode = 2
    main_win.destroy()
    
def clickProj3():
    global current_mode
    current_mode = 3
    main_win.destroy()
    
def quit():
    sys.exit()
    
def clickOk():
    global queen_count_input
    queen_count_input = int(e1.get())
    win2.destroy()
    
def clickOk2():
    global global_x
    global global_y

    global_x = int(e3.get())
    global_y = int(e4.get())
    win3.destroy()
    

if __name__ == '__main__':

    scale = 50
    
    while(1):
        main_win=tk.Tk()
        main_win.title("AI_midTerm")        
        
        current_mode = 0
        
        tk.Button(main_win, text="proj1", command=clickProj1).grid(column=1,row=1, padx=10, pady=10)        
        tk.Button(main_win, text="proj2", command=clickProj2).grid(column=2,row=1, padx=10, pady=10)        
        tk.Button(main_win, text="proj3", command=clickProj3).grid(column=3,row=1, padx=10, pady=10)        
        tk.Button(main_win, text="Quit", command=quit).grid(column=4,row=1, padx=10, pady=10)
        
        main_win.mainloop()
        
        input_correct = False
        if (current_mode == 1):
            matrix_size = 8
            attack = 4

            chess_m = [[False for x in range(matrix_size)] for y in range(matrix_size)]
            queen_pos = [['0' for x in range(matrix_size)] for y in range(matrix_size)]
            total_step = []
            queen_count=0
            for y in range(matrix_size):
                for x in range(matrix_size):
                    a= {}
                    a = eight_queen(x,y,matrix_size,attack,chess_m,queen_pos,queen_count,0, 0)
                    total_step.append(a)
                    chess_m = [[False for x in range(matrix_size)] for y in range(matrix_size)]
                    queen_pos = [['0' for x in range(matrix_size)] for y in range(matrix_size)]

        elif (current_mode == 2):
            #-------input Queen numbers----------------------
            queen_count_input = 0
            win2=tk.Tk()
            win2.title("Q2 input")
            win2.resizable(0,0)
            
            label = tk.Label(win2, text="How many queen you want to put?:")
            label.grid(column=1,row=1, padx=10, pady=5)
            
            e1 = tk.Entry(win2)
            e1.grid(column=1,row=2, padx=10, pady=5)
            
            tk.Button(win2, text="ok!", command=clickOk).grid(column=1,row=3, padx=10, pady=5)

            win2.mainloop()
            
            #------------------------------------------------
            #queen_count_input = int(input("How many queen you want to put?:"))           
            matrix_size = 8
            attack = 4
            temp_dic = {}

            chess_m = [[False for x in range(matrix_size)] for y in range(matrix_size)]
            
            chess_m_2 = [[False for x in range(matrix_size)] for y in range(matrix_size)]
            queen_pos = [['0' for x in range(matrix_size)] for y in range(matrix_size)]
            total_step = []
            #queen_input_list = user_input_queen(queen_count_input,matrix_size)
            
            #----------- GUI input ---------------------------
            queen_input_list = []
            i=0
            global_x = 0
            global_y = 0
            
            error_str = ''
            while i < queen_count_input:
                win3=tk.Tk()
                win3.title("Q2 input queen position")
                win3.resizable(0,0)
                
                label = tk.Label(win3, text='queen x '+str(i)+' is:')
                label.grid(column=1,row=1, padx=10, pady=5)
                
                label2 = tk.Label(win3, text='queen y '+str(i)+' is:')
                label2.grid(column=1,row=2, padx=10, pady=5)
                
                label3 = tk.Label(win3, text=error_str)
                label3.grid(column=1,row=4, padx=10, pady=5)
                
                e3 = tk.Entry(win3)
                e3.grid(column=2,row=1, padx=5, pady=5)
                
                e4 = tk.Entry(win3)
                e4.grid(column=2,row=2, padx=5, pady=5)
                
                tk.Button(win3, text="ok!", command=clickOk2).grid(column=1,row=3, padx=10, pady=5)

                win3.mainloop()
                
                queen_position = {}
                queen_position['y']=global_x-1
                queen_position['x']=global_y-1
                
                
                if queen_position['x']>matrix_size-1 or queen_position['y']> matrix_size-1 or queen_position['x'] <0 or queen_position['y']<0:
                    error_str = 'The queen position is put of matrix, please re-input the point!!'
                else:
                    i+=1
                    error_str = ''
                    queen_input_list.append(queen_position)
            #-----------------------------------------------            
            first_input = check_legal_or_not(queen_input_list, chess_m,attack,queen_pos)
            if(first_input != False):
                chess_m = first_input['matrix']
                queen_pos = first_input['queen_pos']

                chess_m_2 = copy.deepcopy(chess_m)
                queen_pos_2 = copy.deepcopy(queen_pos)

                queen_count=copy.deepcopy(queen_count_input)

                for y in range(matrix_size-1):
                    for x in range(matrix_size-1):
                        a= {}
                        a = eight_queen(x,y,matrix_size,attack,chess_m_2,queen_pos_2,queen_count,0,0)

                        total_step.append(a)
                        chess_m_2 = copy.deepcopy(chess_m)
                        queen_pos_2 = copy.deepcopy(queen_pos)
                        queen_count = copy.deepcopy(queen_count_input)
                
                for i in range(len(total_step)):
                    for j in range(queen_count_input):
                        temp_x = queen_input_list[j]['x']
                        temp_y = queen_input_list[j]['y']
                        total_step[i]['final'][temp_x][temp_y] = '2'
                        
                input_correct = True
        else:
            #------------ GUI input ---------------------------
            global_x = 0
            global_y = 0
            
            win3=tk.Tk()
            win3.title("Q3 input ")
            win3.resizable(0,0)
            
            label = tk.Label(win3, text='What is your matrix size?:')
            label.grid(column=1,row=1, padx=10, pady=5)
            
            label2 = tk.Label(win3, text='What is your attack size?:')
            label2.grid(column=1,row=2, padx=10, pady=5)
            
            e3 = tk.Entry(win3)
            e3.grid(column=2,row=1, padx=5, pady=5)
            
            e4 = tk.Entry(win3)
            e4.grid(column=2,row=2, padx=5, pady=5)
            
            tk.Button(win3, text="ok!", command=clickOk2).grid(column=1,row=3, padx=10, pady=5)

            win3.mainloop()

            matrix_size=global_x
            attack=global_y
            #----------------------------------------------- 

            chess_m = [[False for x in range(matrix_size)] for y in range(matrix_size)]
            queen_pos = [['0' for x in range(matrix_size)] for y in range(matrix_size)]
            total_step = []
            queen_count=0
            for y in range(matrix_size-1):
                for x in range(matrix_size-1):
                    a= {}
                    a = eight_queen(x,y,matrix_size,attack,chess_m,queen_pos,queen_count,0, 0)

                    total_step.append(a)
                    chess_m = [[False for x in range(matrix_size)] for y in range(matrix_size)]
                    queen_pos = [['0' for x in range(matrix_size)] for y in range(matrix_size)]
                    queen_count = 0

        
        if((current_mode == 1) or ((current_mode == 2) and (input_correct == True)) or (current_mode == 3)):
            win2=tk.Tk()
            win2.title("AI_midTerm")
            win2.resizable(0,0)
            
            cvs = tk.Canvas(win2, width = matrix_size*scale, height = matrix_size*scale)
            cvs.grid(column=1,row=1)
            
            label = tk.Label(win2, text="Hello World!")
            label.grid(column=1,row=2, padx=10, pady=10)
                    
            print_it_GUI(total_step, scale)

            win2.mainloop()
        
