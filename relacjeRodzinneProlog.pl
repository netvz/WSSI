rodzic('TataHryndariusz', 'Marek').
rodzic('TataHryndariusz', 'Tadeusz').
rodzic('MamaLudomila', 'Marek').
rodzic('MamaLudomila', 'Tadeusz').
rodzic('DziadekMariusz', 'MamaLudomila').
rodzic('DziadekMariusz', 'SiostraMamy').
rodzic('BabciaWirgilia', 'MamaLudomila').
rodzic('BabciaWirgilia', 'SiostraMamy').
rodzic('SiostraMamy', 'Kuzyn').
rodzic('MazSiostryMamy', 'Kuzyn').
rodzic('MazSiostryMamy', 'PasierbSiostryMamy').
rodzic('MamaTaty', 'TataHryndariusz').
rodzic('TataTaty', 'TataHryndariusz').
rodzic('SiostraMamy', 'DzieckoPasierba').
rodzic('PasierbSiostryMamy', 'DzieckoPasierba').


%A
brat(X, Y):-
    (rodzic(Z, Y), rodzic(W, Y)),
    (rodzic(Z, X), rodzic(W, X)),
    (Z\=W),
    (X\=Y).

%B
kuzyn(X, Y):-
    rodzic(Z, X),
    rodzic(W, Y),
    brat(Z, W),
    X\=Y.

%C
wspoltesciowie(X, Y):-
    (rodzic(M, Z), rodzic(K, Z)),
    (rodzic(X, M), rodzic(Y, K)),
    \+rodzic(X, K),
    \+rodzic(Y, M),
    X\=Y.

%D
przybrana_rodzina(X, Y):-
    (rodzic(X, Z), rodzic(A, Z)),
    rodzic(A, Y),
    \+rodzic(X, Y).

%E
brat_przyrodni(X, Y):-
    (rodzic(Z, Y), rodzic(Z, X)),
    rodzic(W, Y),
     \+rodzic(W, X).


%F
szwagrostwo(X, Y):-
    (rodzic(X, M), rodzic(Z, M)),
    (rodzic(D, Z), rodzic(D, Y)),
    brat(Z,Y),
    \+brat(Y, X),
    X\=Y.

%G
to_skomplikowane(X, Y):-
    (rodzic(Z, X), rodzic(Z, Y)),
    (rodzic(M, X), rodzic(M, P)),
    rodzic(P, Y).














