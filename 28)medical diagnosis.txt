symptom(john, fever).
symptom(john, cough).
symptom(mary, headache).
symptom(mary, fever).

diagnosis(Person, flu) :-
    symptom(Person, fever),
    symptom(Person, cough).

diagnosis(Person, cold) :-
    symptom(Person, cough),
    \+ symptom(Person, fever).

diagnosis(Person, migraine) :-
    symptom(Person, headache),
    \+ symptom(Person, fever).
