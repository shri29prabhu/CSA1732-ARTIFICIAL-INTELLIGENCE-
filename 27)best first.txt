connected(a, b, 1).
connected(a, c, 3).
connected(b, d, 1).
connected(c, d, 1).

heuristic(d, 0).
heuristic(b, 2).
heuristic(c, 1).
heuristic(a, 3).

best_first_search(Start, Goal, Path, Cost) :-
    bfs([[Start, 0]], Goal, [], Path, Cost).

bfs([[Goal, Cost]|_], Goal, _, [Goal], Cost).
bfs([[Node, NodeCost]|Rest], Goal, Visited, [Node|Path], Cost) :-
    findall([NextNode, NewCost],
            (connected(Node, NextNode, StepCost),
             \+ member(NextNode, Visited),
             heuristic(NextNode, HCost),
             NewCost is NodeCost + StepCost + HCost),
            Neighbors),
    append(Rest, Neighbors, NewFrontier),
    sort(2, @=<, NewFrontier, SortedFrontier),
    bfs(SortedFrontier, Goal, [Node|Visited], Path, Cost).
