---
title: A* Pathfinding
date: 2017-1-2 00:00:00
tag: 
    - algorithm
---
[A* Pathfinding tutorial in unity](https://www.youtube.com/watch?v=-L-WgKMFuhE&list=PLFt_AvWsXl0cq5Umv3pMC9SPnKjfp9eGW)

G cost: distance from starting node  
H cost(heuristic): distance from end node  
F cost: G cost + H cost  

算最小F cost周围的node的cost，如果已经有值并且新cost小于旧cost，进行覆盖，迭代  