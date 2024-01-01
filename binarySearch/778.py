class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        #BFS + Min Heap solution
        q=[[grid[0][0],0,0]]
        t=0
        r=len(grid)
        c=len(grid[0])
        vis=[[0]*c for i in range(r)]
        arr=[[0,1],[1,0],[-1,0],[0,-1]]
        while len(q)>0:
            h,y,x=q[0]
            if h>t:
                t+=1
            else:
                heapq.heappop(q)
                if y==r-1 and x==c-1:
                    return t
                for a,b in arr:
                    yy=y+a
                    xx=x+b
                    if yy>=0 and xx>=0 and yy<r and xx<c and vis[yy][xx]==0:
                        vis[yy][xx]=1
                        heapq.heappush(q,[grid[yy][xx],yy,xx])
        return -1
        

        #Binary search
        l=0
        r=2500
        def bfs(val):
            if grid[0][0]>val:
                return False
            q=[[0,0]]
            
            r=len(grid)
            c=len(grid[0])
            vis=[[0]*c for i in range(r)]
            
            vis[0][0]=1
            arr=[[0,1],[1,0],[-1,0],[0,-1]]
            while len(q)>0:
                    y,x=q.pop(0)
                    if y==r-1 and x==c-1:
                        return True
                    for a,b in arr:
                        yy=y+a
                        xx=x+b
                        if yy>=0 and xx>=0 and yy<r and xx<c and vis[yy][xx]==0 and grid[yy][xx]<=val:
                            vis[yy][xx]=1
                            q.append([yy,xx])
            return False
        while l<=r:
            m=(l+r)//2
            if bfs(m):
                r=m-1
            else:
                l=m+1
        return l
            
          
            