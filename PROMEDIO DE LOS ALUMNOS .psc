Algoritmo CalcularPromedio
    Definir NotaExamen1, NotaExamen2, NotaExamen3, Ponderacion1, Ponderacion2, Ponderacion3, Promedio Como Real;
	
    Escribir "Ingrese la nota del primer examen: ";
    Leer NotaExamen1;
	
    Escribir "Ingrese la nota del segundo examen: ";
    Leer NotaExamen2;
	
    Escribir "Ingrese la nota del tercer examen: ";
    Leer NotaExamen3;
	
    Ponderacion1 = NotaExamen1 * 0.25;
    Ponderacion2 = NotaExamen2 * 0.25;
    Ponderacion3 = NotaExamen3 * 0.50;
	
    Promedio = Ponderacion1 + Ponderacion2 + Ponderacion3;
	
    Escribir "El promedio del alumno es: ", Promedio;
	
FinAlgoritmo
