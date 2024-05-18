class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(rooms, node, visited):

            if node not in visited:
                visited.append(node)

                for neighbor in rooms[node]:
                    dfs(rooms, neighbor, visited)
            


        visited = []
        dfs(rooms, 0, visited)

        return len(visited) == len(rooms)
        
