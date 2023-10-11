Algoritmo CalcularCostoEstacionamiento
    Definir HorasEstacionamiento, MinutosAdicionales, CostoTotal Como Entero;
	
    Escribir "Ingrese la cantidad de horas de estacionamiento: ";
    Leer HorasEstacionamiento;
	
    Escribir "Ingrese la cantidad de minutos adicionales (después de las primeras 10 horas): ";
    Leer MinutosAdicionales;
	
    Si HorasEstacionamiento <= 2 Entonces
        CostoTotal = HorasEstacionamiento * 1500;
    Sino 
		Si HorasEstacionamiento > 2 Y HorasEstacionamiento <= 5 Entonces
			CostoTotal = 2 * 1500 + (HorasEstacionamiento - 2) * 3000;
		Sino 
			Si HorasEstacionamiento > 5 Y HorasEstacionamiento <= 10 Entonces
				CostoTotal = 2 * 1500 + 3 * 3000 + (HorasEstacionamiento - 5) * 60;
			Sino
				Si HorasEstacionamiento >=10 Entonces
					CostoTotal = 2 * 1500 + 3 * 3000 + 5 * 60 + MinutosAdicionales * 92;
				Fin Si	
			Fin Si
		Finsi	
	Fin si		
			Escribir "El costo de estacionamiento es: ", CostoTotal;
			
FinAlgoritmo