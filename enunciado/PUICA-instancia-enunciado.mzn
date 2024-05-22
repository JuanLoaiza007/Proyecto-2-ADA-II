% Número de clientes y sitios
int: n = 7; 
int: m = 6; 

% Costos fijos, capacidad de producción, demanda de los clientes
array[1..m] of float: f = [10,10,10,10,10,10];
array[1..m] of int: c = [6,6,6,6,6,6];
array[1..n] of float: d = [1.5,2.0,3.0,4.0,2.5,1.0,2.0];

% Beneficio por unidad vendida al cliente c desde la instalación i
array[1..n, 1..m] of float: b = array2d(1..n, 1..m, [4.0,4.0,3.5,1.3,0.5,-1.0,4.5,4.5,5.0,3.0,1.0,0.0,2.5,2.5,4.0,5.0,1.5,1.5,0.5,4.2,3.5,3.3,5.0,3.3,1.0,3.5,4.5,5.5,4.0,4.0,0.5,1.5,1.5,1.8,5.5,4.5,-3.5,-0.5,0.0,1.3,3.0,2.0]);

% Variables de decisión
array[1..m] of var 0..1: a; % Si se abre la instalación i
array[1..n, 1..m] of var 0..max(i in 1..m) (c[i]): x; % Cantidad enviada al cliente c desde la instalación i

% Función objetivo
var float: utilidad_total = sum(c_s in 1..n, i_s in 1..m) (b[c_s,i_s]*x[c_s,i_s]) - sum(i_s in 1..m) (f[i_s]*a[i_s]);
solve maximize utilidad_total;

% Restricciones
constraint forall(c_s in 1..n) (sum(i_s in 1..m) (x[c_s,i_s]) - d[c_s] = 0);
constraint forall(i_s in 1..m) (sum(c_s in 1..n) (x[c_s,i_s]) <= c[i_s]*a[i_s]);
constraint sum(i_s in 1..m) (a[i_s]) <= m;
constraint forall(c_s in 1..n, i_s in 1..m) (x[c_s,i_s] >= 0.0 );
