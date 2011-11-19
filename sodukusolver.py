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

    def clear_false(self, pos):
        row = self.find_row(pos)
        column = self.find_column(pos)
        quad = self.find_quadrant(pos)
        value = self.b[pos]
        
        

        for i in range(9):
            index = row*9+i
            if self.b[index].__class__ == list and self.b[index].__contains__(value):

                self.b[index].remove(value)
                
                if len(self.b[index]) == 1:
                   
                    self.b[index] = self.b[index][0]

        for i in range(9):
            index = column+i*9
            if self.b[index].__class__ == list and self.b[index].__contains__(value):
                self.b[index].remove(value)
                
                if len(self.b[index]) == 1:
                    
                     self.b[index] = self.b[index][0]

        #temporary variables for holding start pos of quadrant
        #print('quad: ', quad)
        startpos = 27*int(quad/3) + 3*int(quad%3)
        for i in range(3):
            for j in range(3):
                index = startpos + i*9 + j
                #print('index: ', index)
                if self.b[index].__class__ == list and self.b[index].__contains__(value):
                    self.b[index].remove(value)
                    
                    if len(self.b[index]) == 1:
                    
                        self.b[index] = self.b[index][0]

    def done(self):
        for var in self.b:
            if var.__class__ == list:
                return False

        return True

    def solve(self):
        iterations = 0;
        while not self.done():
            for r in range(81):
                if self.b[r].__class__ != list: 
                    self.clear_false(r)
            iterations = iterations + 1

        print('Number of iterations needed: ', iterations)
        
                

       


c = board((4,0,0,0,0,3,0,0,0,3,2,9,0,0,7,0,4,5,0,1,0,0,2,9,0,0,3,0,0,0,7,0,0,3,9,6,1,0,7,0,0,0,5,0,4,9,5,3,0,0,6,0,0,0,8,0,0,2,6,0,0,7,0,6,9,0,5,0,0,8,3,2,0,0,0,3,0,0,0,0,1))

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

print(temptwo)

# c.print_board()



# c.solve()

# c.print_board()

