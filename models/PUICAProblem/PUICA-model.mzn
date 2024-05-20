% Parámetros generales del modelo
% Ejecutar con COIN-BC

int: n; % Número de clientes
int: m; % Número de instalaciones

% Costos fijos de abrir cada instalación
array[1..m] of float: f; %Ejemplo [10,10,10,10,10,10]

% Capacidad de producción de cada instalación
array[1..m] of int: c; %Ejemplo [6,6,6,6,6,6]

% Demanda de cada cliente
array[1..n] of float: d; %Ejemplo [1.5,2.0,3.0,4.0,2.5,1.0,2.0]

% Beneficio por unidad vendida al cliente c desde la instalación i
array[1..n, 1..m] of float: b;
% Ejemplo array2d(1..n, 1..m, [4.0,4.0,3.5,1.3,0.5,-1.0,4.5,4.5,5.0,3.0,1.0,0.0,2.5,2.5,4.0,5.0,1.5,1.5,0.5,4.2,3.5,3.3,5.0,3.3,1.0,3.5,4.5,5.5,4.0,4.0,0.5,1.5,1.5,1.8,5.5,4.5,-3.5,-0.5,0.0,1.3,3.0,2.0])

% Variables de decisión
array[1..m] of var 0..1: a; % Verifica sii se abre la instalación i
array[1..n, 1..m] of var 0.0..100000: x; % Cantidad enviada al cliente c desde la instalación i

% Función objetivo: maximizar la utilidad total
% Se suma el total de beneficios menos el total de costo de cada instalación abierta
var float: utilidad_total = sum(c_s in 1..n, i_s in 1..m) (b[c_s,i_s]*x[c_s,i_s]) - sum(i_s in 1..m) (f[i_s]*a[i_s]);

solve maximize utilidad_total;

% Restricciones

% La suma de los productos enviados a cada cliente debe satisfacer su demanda
constraint forall(c_s in 1..n) (
    sum(i_s in 1..m) (x[c_s,i_s]) = d[c_s]
);

% La suma de los productos enviados desde cada instalación no debe exceder su capacidad si está abierta
constraint forall(i_s in 1..m) (
    sum(c_s in 1..n) (x[c_s,i_s]) <= c[i_s] * a[i_s]
); 

% No abrir más instalaciones de las necesarias
constraint sum(i_s in 1..m) (a[i_s]) <= m; 

% No se puede enviar una cantidad negativa de productos (restricción de no negatividad)
constraint forall(c_s in 1..n, i_s in 1..m) (
    x[c_s,i_s] >= 0.0
); 


output [
    "Utilidad total: ", show(utilidad_total), "\n",
    "Instalaciones abiertas: ", show(a), "\n",
    "Productos enviados: ", show(x), "\n",
];

