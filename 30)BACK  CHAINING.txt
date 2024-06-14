% Facts
action(smile).
action(laugh).

feeling(happy).
feeling(sad).

% Rules
happy(Person) :-
    action(Action),
    causes_happiness(Action),
    person(Person).

causes_happiness(smile).
causes_happiness(laugh).

person(john).  % John is our test person
