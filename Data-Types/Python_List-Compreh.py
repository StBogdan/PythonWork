if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    myList = [ [xx,yy,zz] for xx in range(0,x+1) for yy in range(0,y+1) for zz in range(0,z+1) if (xx+yy+zz!=n)]
    print(myList)

