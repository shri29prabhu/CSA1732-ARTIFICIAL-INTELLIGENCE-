% Move definitions with print statements
move(state(at_door, on_floor, at_window, has_not), walk(at_door, at_window), state(at_window, on_floor, at_window, has_not)) :-
    writeln('Monkey walks from door to window').
move(state(at_window, on_floor, at_window, has_not), climb, state(at_window, on_box, at_window, has_not)) :-
    writeln('Monkey climbs on box').
move(state(at_window, on_box, at_window, has_not), grasp, state(at_window, on_box, at_window, has)) :-
    writeln('Monkey grasps banana').

% Recursive rule to determine if the monkey can get the banana
canget(state(_, _, _, has)) :-
    writeln('Monkey has the banana!').
canget(State1) :-
    move(State1, Action, State2),
    writeln(Action),
    canget(State2).
