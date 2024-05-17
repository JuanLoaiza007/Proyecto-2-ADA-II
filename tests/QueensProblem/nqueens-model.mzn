int: n_i; % The number of queens.

array [1..n_i] of var 1..n_i: q;

include "alldifferent.mzn";

constraint alldifferent(q);
constraint alldifferent(i in 1..n_i)(q[i] + i);
constraint alldifferent(i in 1..n_i)(q[i] - i);