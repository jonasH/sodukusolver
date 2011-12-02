#!/usr/bin/python

class board:
    

    def __init__(self, values):
        self.b = list()
        for a in values:
            if a != 0:
                self.b.append(a)
            else:
                self.b.append([1,2,3,4,5,6,7,8,9])
        
        

    def print_board(self):
        j = 0
        for i in self.b:
            
            if i.__class__ == list:
                print(' ', end=' ')
            else:
                print(i, end=' ')
        
            j = j + 1
            if j == 9:
                j = 0
                print('',end='\n')

    def get_row(self, row):
        row = row*9
        result = list()
        for i in range(9):
            result.append(self.b[row+i])

        return result
            

    def get_column(self, column):
        result = list()
        for i in range(9):
            result.append(self.b[column+i*9])


        return result



    def get_quadrant(self, quad):
        result = list()
        for i in range(3):
            for j in range(3):
                result.append(self.b[(3*quad+i*9)+j])
            
        return result

    def find_row(self, pos):
        return int(pos/9)

    def find_column(self, pos):
        return pos%9

    def find_quadrant(self, pos):
        return int(self.find_column(pos)/3) + int(self.find_row(pos)/3)*3



# Reduces the possible numbers
    def clear_false(self, pos):
        row = self.find_row(pos)
        column = self.find_column(pos)
        quad = self.find_quadrant(pos)
        value = self.b[pos]
        result = False

        # Row
        for i in range(9):
            index = row*9+i
            if self.b[index].__class__ == list and self.b[index].__contains__(value):

                self.b[index].remove(value)
                result = True
                if len(self.b[index]) == 1:
                   
               
                   self.b[index] = self.b[index][0]
        #Column
        for i in range(9):
            index = column+i*9
            if self.b[index].__class__ == list and self.b[index].__contains__(value):
                self.b[index].remove(value)
                result = True
                if len(self.b[index]) == 1:
                    

                    self.b[index] = self.b[index][0]


        # Quadrant
        #temporary variables for holding start pos of quadrant
        startpos = 27*int(quad/3) + 3*int(quad%3)
        for i in range(3):
            for j in range(3):
                index = startpos + i*9 + j
                
                if self.b[index].__class__ == list and self.b[index].__contains__(value):
                    self.b[index].remove(value)
                    result = True
                    if len(self.b[index]) == 1:
                        
                        self.b[index] = self.b[index][0]

        return result

# Checks if a number is alone in it's row, column or quad
    def clear_false_2(self, pos):
        row = self.find_row(pos)
        column = self.find_column(pos)
        quad = self.find_quadrant(pos)


        

        # Row
        # Solution is gathering all the lists
        # and if a number is alone it has it's place.
        temp_list = list()
        use_templist = False
        for i in range(9):
            index = row*9+i
            if self.b[index].__class__ == list:
                if (len(temp_list) > 0):
                    use_templist = True
                temp_list.extend(self.b[index])
        if use_templist:
                for i in range(9):
                    i = i + 1
                    if temp_list.count(i) == 1:
                        for j in range(9):
                            index = row*9+j
                            if self.b[index].__class__ == list and self.b[index].__contains__(i):
                                # print()
                                # print("DEBUG")
                                # print()
                                # self.print_board()
                                # print()
                                # for var in range(9):
                                #     print(self.get_row(var))
                                # print("TEMP_LIST= ", temp_list)
                                # print("INDEX= ", index)
                                # print("I= ", i)
                                # print()
                
                                self.b[index] = i
                                return True

                    
                

        ##END Row calc


        #Column
        temp_list = list()
        use_templist = False
        for i in range(9):
            index = column+i*9
            if self.b[index].__class__ == list:
                if (len(temp_list) > 0):
                    use_templist = True
                temp_list.extend(self.b[index])

        if use_templist:
                for i in range(9):
                    i = i+1
                    if temp_list.count(i) == 1:
                        for j in range(9):
                            index = column+j*9
                            if self.b[index].__class__ == list and self.b[index].__contains__(i):
                                self.b[index] = i
                                return True
                                
        # Quadrant
        #temporary variables for holding start pos of quadrant

        temp_list = list()
        use_templist = False
        startpos = 27*int(quad/3) + 3*int(quad%3)
        for i in range(3):
            for j in range(3):
                index = startpos + i*9 + j
                if self.b[index].__class__ == list:
                    if (len(temp_list) > 0):
                        use_templist = True
                    temp_list.extend(self.b[index])
        
                            

        if use_templist:
                for i in range(9):
                    i = i + 1
                    if temp_list.count(i) == 1:
                        for j in range(3):
                            for k in range(3):
                                index = startpos + j*9 + k
                                if self.b[index].__class__ == list and self.b[index].__contains__(i):
                                    
                                    
                                    self.b[index] = i
                                    return True
                            

        return False


    def done(self):
        for var in self.b:
            if var.__class__ == list:
                return False

        return True
#not self.done() and
    def solve(self):
        iterations = 0;
        keep_going = True
        
        while keep_going:
            #print('ha')
            keep_going = False
            for r in range(81):
                if self.b[r].__class__ != list: 
                    keep_going = keep_going or self.clear_false(r)

            if not keep_going:
                for r in range(81):
                    if self.b[r].__class__ != list: 
                        keep_going = keep_going or self.clear_false_2(r)

            print()
            print()
            for var in range(9):
                print(self.get_row(var))

            iterations = iterations + 1
            if self.done():
                break

        if keep_going == False:
            print('Could not solve')
            
            for var in range(9):
                print(self.get_row(var))

        print('Number of iterations needed: ', iterations)
    
                

       


#c = board((4,0,0,0,0,3,0,0,0,3,2,9,0,0,7,0,4,5,0,1,0,0,2,9,0,0,3,0,0,0,7,0,0,3,9,6,1,0,7,0,0,0,5,0,4,9,5,3,0,0,6,0,0,0,8,0,0,2,6,0,0,7,0,6,9,0,5,0,0,8,3,2,0,0,0,3,0,0,0,0,1))
print('Hellew and whalecum to sodukosolver, input! 0 is empty!')
temptwo = ''
print('first row: ', end='')
tempone = input()
temptwo = temptwo+tempone
print('second row: ', end='')
tempone = input()
temptwo = temptwo+tempone
print('third row: ', end='')
tempone = input()
temptwo = temptwo+tempone
print('fourth row: ', end='')
tempone = input()
temptwo = temptwo+tempone
print('fifth row: ', end='')
tempone = input()
temptwo = temptwo+tempone
print('sixth row: ', end='')
tempone = input()
temptwo = temptwo+tempone
print('seventh row: ', end='')
tempone = input()
temptwo = temptwo+tempone
print('eigth row: ', end='')
tempone = input()
temptwo = temptwo+tempone
print('ninth row: ', end='')
tempone = input()
temptwo = temptwo+tempone


input_list = list()

for i in temptwo:
    if i != ' ':
        input_list.append(int(i))

print(input_list)

board = board(input_list)
board.print_board()


board.solve()

board.print_board()

