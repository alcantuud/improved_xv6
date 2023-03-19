# Aso_xv6

Trabajamos sobre un esqueleto básico de xv6, y sobre el realizamos ciertas modificaciones para mejorarlo. Implementamos las siguientes funcionalidades:


1. Modificaciones en las llamadas al sistema

1.1. Nueva llamada al sistema a xv6: int date (structrtcdate*d)
1.2. Llamada al sistema dup2() y modificar el shell para usarla
1.3. Modificar las llamadas exit() y wait() para que sigan la signatura de las funciones de POSIX, es decir: int wait ( int * status ); void exit ( int status )


2. El sistema de memoria de xv6. Reserva de páginas bajo demanda

2.1. Implementar la reserva diferida en xv6
2.2. Modificar el código de la función exec() para que asigne a cada proceso un número de páginas de pila igual al número de páginas de código+datos de ese proceso.
2.3. Añadimos una llamada al sistema freemem() con la siguiente signatura: 1 int freemem (int type)

3. Ficheros grandes en xv6

3.1. Modificamos bmap() para que implemente un bloque doblemente indirecto. Sin cambiar el tamaño del nodo-i en disco, por lo que sacrificaremos un bloque directo para implementar el doblemente indirecto
3.2. Modificamos xv6 para manejar el borrado de ficheros con bloques doblemente indirectos

# Como usarlo

Ejecutamos el comando make, dentro podemos seleccionar entre varias opciones. Como por ejemplo make quemu-gdb.

Se puede escribir tanto desde la terminal como desde la interfaz que te ofrece, y para comprobar las implementaciones basta con ejecutar los siguientes comandos

$./dup2test

$./exitwait

$./freem

$./big

$./tsbrk1

$./tsbrk2

$./tsbrk3

$./tsbrk4

$./tsbrk5
