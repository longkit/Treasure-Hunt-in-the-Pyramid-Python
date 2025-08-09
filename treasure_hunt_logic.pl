% تعریف موقعیت بازیکن، گنج و تله‌ها
:- dynamic player/2.
:- dynamic treasure/2.
:- dynamic trap/2.

% جهت‌های حرکت (بالا، پایین، چپ، راست)
direction(-1, 0).
direction(1, 0).
direction(0, -1).
direction(0, 1).

% بررسی موقعیت معتبر (داخل محدوده و بدون تله)
is_valid(X, Y) :-
    X >= 0, X < 12,
    Y >= 0, Y < 16,
    \+ trap(X, Y).

% جستجوی عرضی برای یافتن مسیر به گنج
bfs([[X, Y] | _], _, [[X, Y]]) :-
    treasure(X, Y), !.

bfs([[X, Y] | Rest], Visited, [[X, Y] | Path]) :-
    findall([NX, NY], (direction(DX, DY), NX is X + DX, NY is Y + DY, is_valid(NX, NY), \+ member([NX, NY], Visited)), Neighbors),
    append(Rest, Neighbors, NewQueue),
    append(Visited, Neighbors, NewVisited),
    bfs(NewQueue, NewVisited, Path).

% اجرای الگوریتم برای یافتن مسیر
find_path(Path) :-
    player(PX, PY),
    bfs([[PX, PY]], [[PX, PY]], Path).

% بروزرسانی موقعیت بازیکن
move_player :-
    find_path([NextX, NextY | _]),
    retract(player(_, _)),
    assertz(player(NextX, NextY)).
