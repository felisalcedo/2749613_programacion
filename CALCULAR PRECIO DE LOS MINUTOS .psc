Algoritmo CalcularCostoLlamada
    Definir DuracionLlamada, CostoPorMinuto, CostoTotal Como Real;
	
    Escribir "Ingrese la duraci�n de la llamada (en minutos): ";
    Leer DuracionLlamada;
	
    Escribir "Ingrese el costo por minuto: ";
    Leer CostoPorMinuto;
	
    CostoTotal = DuracionLlamada * CostoPorMinuto;
	
    Escribir "El costo total de la llamada es: ", CostoTotal;
	
FinAlgoritmo