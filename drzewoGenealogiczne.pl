osoba('Skipper').
osoba('Julian').
osoba('Morissa').
osoba('Rico').
osoba('Marlenka').
osoba('Mort').
osoba('Gloria').
osoba('Alex').
osoba('Marty').
osoba('Kowalski').
osoba('Szeregowy').
osoba('BabciaWiewiorka').

mezczyzna('Skipper').
mezczyzna('Julian').
mezczyzna('Rico').
mezczyzna('Mort').
mezczyzna('Alex').
mezczyzna('Marty').
mezczyzna('Kowalski').
mezczyzna('Szeregowy').

rodzic('Rico', 'Gloria').
rodzic('Rico', 'Alex').
rodzic('Rico', 'Marty').
rodzic('Marlenka', 'Gloria').
rodzic('Marlenka', 'Alex').
rodzic('Marlenka','Marty').
rodzic('Marlenka', 'Kowalski').
rodzic('Mort', 'Szeregowy').
rodzic('Skipper', 'Rico').
rodzic('Julian', 'Marlenka').
rodzic('Julian', 'Mort').
rodzic('Morissa', 'Marlenka').
rodzic('Morissa', 'Mort').
rodzic('BabciaWiewiorka', 'Julian').

kobieta(X):-
    osoba(X),
    \+mezczyzna(X).

ojciec(X, Y):-
	rodzic(X,Y),
    mezczyzna(X).

matka(X, Y):-
	rodzic(X, Y),
    kobieta(X).

corka(Y, X):-
    rodzic(X, Y),
    kobieta(Y).

brat_rodzony(X, Y):-
    (mezczyzna(X)),
    (matka(A, X), matka(A, Y)),
    (ojciec(B, X), ojciec(B, Y)),
    (X\=Y).

brat_przyrodni(X, Y):-
    (mezczyzna(X), mezczyzna(Y)),
    ((matka(A, X), matka(A, Y)); (ojciec(B, X), ojciec(B, Y))),
    \+brat_rodzony(X, Y),
    (X\=Y).

kuzyn(X, Y):-
    (rodzic(Z, X), rodzic(W, Y)),
    brat_rodzony(Z, W).

dziadek_od_strony_ojca(X, Y):-
    (ojciec(Z, Y), ojciec(X, Z)).

dziadek_od_strony_matki(X, Y):-
    (matka(Z, Y), ojciec(X, Z)).

dziadek(X, Y):-
    dziadek_od_strony_ojca(X, Y);
    dziadek_od_strony_matki(X, Y).

babcia(X, Y):-
    (matka(Z, Y), matka(X, Z));
    (ojciec(Z, Y), matka(X, Z)).

wnuczka(X, Y):-
    babcia(Y, X),
    kobieta(X).

przodek_do_2_pokolenia_wstecz(X, Y):-
    dziadek(Y, X);
    babcia(Y, X).

przodek_do_3_pokolenia_wstecz(X, Y):-
    przodek_do_2_pokolenia_wstecz(Z, Y),
    (ojciec(Z, X); matka(Z, X)).
