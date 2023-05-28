class nQueen:
    def SolutionN(self, n):
        col = set()
        urd = set() # r+c
        drd = set() # r-c

        board = [[" - " for i in range(n)] for j in range(n)]
        res=[]
        
        def backTrack(r):
            if r==n:
                CopyList=["".join(rows) for rows in board]
                res.append(CopyList)
                return
            
            for c in range(n):
                if c in col or (r+c) in urd or (r-c) in drd:
                    continue

                col.add(c)
                urd.add(r+c)
                drd.add(r-c)
                board[r][c] = " Q "

                backTrack(r+1)

                col.remove(c)
                urd.remove(r+c)
                drd.remove(r-c)
                board[r][c] = " - "
        
        backTrack(0)
        return res



new = nQueen()
# new.SolutionN(4)
results= new.SolutionN(4)

for i in results:
    for j in i:
        print(j)
    print()

