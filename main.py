
t_map = ["---#--###--#-",
         "-#---#----##-",
         "####-#-#-#-##",
         "---#---#-#---",
         "-#-####---##-",
         "-#------#----",
         "-############",
         "------------@"]

finalPath = [['x' for x in range(len(t_map[0]))] for y in range(len(t_map))]
#t_map is immutable so...
#making a list-of-list of map
for x in range(0, len(t_map)):
    for y in range(0, len(t_map[x])):
        finalPath[x][y] = ''+t_map[x][y]

flag1 = False
steps = "" #will store the steps to reach to treasure
count = 0
isVisited = [[0 for x in range(len(t_map[0]))] for y in range(len(t_map))] # will keep record of each character if its visited or not

class Main:

    def checkCharacter(self, i, j, steps):
        global flag1
        global count
        global finalPath
        global isVisited

        #if i and j is out of bound just return false
        if(i >= len(finalPath) or j >= len(finalPath[i])):
            return False

        #if flag1 is true means treasure is already found
        if(flag1 == True):
            return True;

        currentChar = finalPath[i][j]

        #check if the character is + and visited
        if(currentChar == '+' and isVisited[i][j] == 1):
            return True

        #if current character is already visited and not '+' then return false
        if(isVisited[i][j] == 1):
            return False
        else:
            #if not visited then mark it visited in isVisited array
            isVisited[i][j] = 1

        #check if its treasure
        if(currentChar == '@'):
            flag1 = True
            finalPath[i][j]='T'
            #print moves needed to reach to treasure
            print("Steps are : ", steps)
            return True

        elif(currentChar == '#'):
            if (i == 0 and j == 0):
                print("Theres no way to enter the cave!")
                return False
            else:
                return False



        elif currentChar == '-' or currentChar == '+':
            #print("Replaced - to + row no ", "[",i,",", j,"]")
            finalPath[i][j] = '+'
            if (i == 0 and j == 0):
                # top left
                # right bellow
                count += 1
                tp1 = self.checkCharacter(i, j + 1, steps + " right")
                tp2 = self.checkCharacter(i + 1, j, steps + " down")
                if(tp1 == False and tp2 == False):
                    finalPath[i][j] = '!'
                    return False
                return tp1 or tp2


            elif (i == (len(finalPath) - 1) and j == 0):
                # bottom left
                # check above and right
                count += 1
                r1 = self.checkCharacter(i - 1, j, steps + " up")
                r2 = self.checkCharacter(i, j + 1, steps + " right")
                if(r1 == False or r2 == False):
                    finalPath[i][j] = '!'
                    return False
                return r1 or r2
            elif (i == 0 and j == (len(finalPath[i]) - 1)):
                # top right
                # check below and left
                count += 1
                tp3 = self.checkCharacter(i + 1, j, steps + " down")
                tp4 = self.checkCharacter(i, j - 1, steps + " left")
                if(tp3 == False or tp4 == False):
                    finalPath[i][j] = '!'
                    return False
                return tp3 or tp4

            elif (i == (len(finalPath) - 1) and j == (len(finalPath[i]) - 1)):
                # bottom right
                # check above and left
                count += 1
                tp5 = self.checkCharacter(i - 1, j, steps + " up")
                tp6 = self.checkCharacter(i, j - 1, steps + " left")
                if(tp5 == False or tp6 == False):
                    finalPath[i][j]= '!'
                    return False
                return tp5 or tp6

            elif (i == 0):
                # top most row
                # check below left and right
                count += 1
                tp7 = self.checkCharacter(i + 1, j, steps + " down")
                tp8 = self.checkCharacter(i, j - 1, steps + " left")
                tp9 = self.checkCharacter(i, j + 1, steps + " right")
                if((tp7 == False and tp8 == False) or (tp7 == False and tp9 == False) or (tp8 == False and tp9 == False)):
                    finalPath[i][j] = '!'
                    return False
                return tp7 or tp8 or tp9
            elif (j == 0):
                # left most column
                # check right top and bottom
                count += 1
                tp10 = self.checkCharacter(i, j + 1, steps + " right")
                tp11 = self.checkCharacter(i-1, j, steps+" up")
                tp12 = self.checkCharacter( i + 1, j, steps + " down")
                if ((tp10 == False and tp11 == False) or (tp10 == False and tp12 == False) or (tp11 == False and tp12 == False)):
                    finalPath[i][j] = '!'
                    return False
                return tp10 or tp11 or tp12

            elif (i == len(finalPath) - 1):
                # bottom most column
                # check top left and right
                count += 1
                tp13 = self.checkCharacter(i - 1, j, steps + " up")
                tp14 = self.checkCharacter(i, j - 1,steps + " left")
                tp15 = self.checkCharacter(i, j + 1, steps + " right")
                if((tp13 == False and tp14 == False) or (tp13 == False and tp15 == False) or (tp14 == False and tp15 == False)):
                    finalPath[i][j] = '!'
                    return False
                return tp13 or tp14 or tp15
            elif (j == len(finalPath[i]) - 1):
                # right most column
                # check left top and bellow
                count += 1
                tp16 = self.checkCharacter(i - 1, j, steps + " up")
                tp17 = self.checkCharacter(i, j - 1, steps + " left")
                tp18 = self.checkCharacter(i + 1, j, steps + " Down")
                if((tp16 == False and tp17 == False) or (tp16 == False and tp18 == False) or (tp17 == False and tp18 == False)):
                    finalPath[i][j] == '!'
                    return False
                return tp16 or tp17 or tp18


            else:
                # check bellow right top and left
                # somewhere in middle
                count += 1
                tp19 = self.checkCharacter(i + 1, j, steps + " Down")
                tp20 = self.checkCharacter(i, j + 1, steps + " right")
                tp21 = self.checkCharacter(i - 1, j, steps + " up")
                tp22 = self.checkCharacter(i, j - 1, steps + " left")
                if((tp19 == False and tp20 == False and tp21 == False) or (tp20== False and tp21== False and tp22== False) or (tp21== False and tp22== False and tp19== False) or (tp19== False and tp20== False and tp22== False) ):
                    finalPath[i][j] = '!'
                    return False
                return tp19 or tp20 or tp21 or tp22

        else:
            print("Somethig is wrong in the map")
            return False;



#calling function
m1 = Main()
m1.checkCharacter(0,0,"")
for i in finalPath:
    print(i)
print("count is ", count)
if flag1==True:
    print("Got Treasure")
else:
    print("can't find treasure, Better Luck next time")