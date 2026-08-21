class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq={i:[] for i in range(numCourses)}

        visitingSet=set()

        #populate hashmap

        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        def dfs(crs):

            if crs in visitingSet:
                return False

            if preReq[crs]==[]:
                return True
            visitingSet.add(crs)

            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
                
            visitingSet.remove(crs)
            preReq[crs]=[]
            return True
        
    
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            