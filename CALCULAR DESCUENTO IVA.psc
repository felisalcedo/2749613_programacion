Algoritmo CalcularCostoDescuento
    Definir Precio, Descuento, Costo Como Real;
	Precio=0;
	Descuento=0;
	Costo=0;
	
    Escribir "Ingrese el precio del artículo:";
    Leer Precio;
	
    Si Precio >= 200 Entonces
		    Descuento = Precio * 0.15;
	Sino
	    Si Precio > 100 Y Precio < 200 Entonces
			Descuento = Precio * 0.12;
		Sino
			Si Precio < 100 Entonces
			 Descuento = Precio * 0.10;
		    Fin Si
		Fin Si
	Fin Si	
		Costo = Precio - Descuento;
		
		Escribir "Descuento aplicado:", Descuento;
		Escribir "Costo final: ", Costo;
		
FinAlgoritmo