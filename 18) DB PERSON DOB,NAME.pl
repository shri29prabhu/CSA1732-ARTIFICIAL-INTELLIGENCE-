person(goutham, 2004, 12, 16).

dob(Name, Year, Month, Day) :-
    person(Name, Year, Month, Day).

name(Year, Month, Day, Name) :-
    person(Name, Year, Month, Day).
