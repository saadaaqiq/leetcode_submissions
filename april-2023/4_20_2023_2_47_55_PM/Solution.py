# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = {}
        for rec, ings in zip(recipes, ingredients):
            adj[rec] = set(ings)
        
        supply_set = set(supplies)
        vis = set()

        @cache
        def dfs(x):
            # if x is a supply then it's all good
            if x in supply_set:
                return True
            if x in vis:
                return False
            vis.add(x)
            # if not continue until all its dependencies are
            if x in adj:
                for y in adj[x]:
                    if not dfs(y):
                        return False
                return True
            else:
                return False
        
        res = []
        for x in recipes:
            if dfs(x):
                res.append(x)
            vis.clear()
        return res







        