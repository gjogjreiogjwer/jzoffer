
def find(target,array):
    row=len(array)
    line=len(array[0])
    if row>0 and line>0:
        x=0
        y=line-1
        while x<row and y>=0:
            if array[x][y]==target:
                return True
            if array[x][y]<target:
                x+=1
            else:
                y-=1;
    return False
