import numpy as np



A=np.matrix([[2,1,1],[1,2,1],[1,1,2]])
print("A:")
print(A)
print("\n")

B=np.matrix([[1],[-1],[2]])
print("B:")
print(B)
print("\n")








A=np.matrix([[1,1,0,0],[1,2,0,1],[0,0,3,3],[0,1,3,2]])
print("A:")
print(A)
print("\n")

B=np.matrix([[1],[1],[0],[1]])
print("B:")
print(B)
print("\n")


def inverse_power(A,XX):
    X=XX
    NX=np.linalg.norm(X,np.inf)
    print("X~(0):")  
    X=(1/NX)*X
    print(X)
    print("\n")  
    for i in range(10):
        print(f'k={i}')
        X = np.linalg.solve(A, X)
        print(f'X({i+1}):')
        print(X)
        print("\n")
        NX=np.linalg.norm(X,np.inf)
        print(f'NX~({i+1}):')
        print(NX)
        print("\n")        
        print(f'X~({i+1}):')
        X=(1/NX)*X
        print(X)
        print("\n")     

    return X








def powermethode(A,XX):
    X=XX
    NX=np.linalg.norm(X,np.inf)
    print("X~(0):")  
    X=(1/NX)*X
    print(X)
    print("\n")  
    for i in range(4):
        print(f'k={i}')
        X = A*X
        print(f'X({i+1}):')
        print(X)
        print("\n")
        NX=np.linalg.norm(X,np.inf)
        print(f'NX~({i+1}):')
        print(NX)
        print("\n")        
        print(f'X~({i+1}):')
        X=(1/NX)*X
        print(X)
        print("\n")     

    return X

























inverse_power(A,B)













