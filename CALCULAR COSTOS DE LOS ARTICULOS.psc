Algoritmo CalcularCostoArticulos
    Definir N, i, Precio, CostoArticulo, CostoTotal, Descuento, DescuentoTotal Como Real;
	i<-0;
    Escribir "Ingrese la cantidad de art�culos:";
    Leer N;
	
    CostoTotal = 0;
    DescuentoTotal = 0;
	
    Para i <-1 hasta N Hacer
        Escribir "Ingrese el precio del art�culo ", i, ": ";
	FinPara
	
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
			CostoArticulo = Precio - Descuento;
			CostoTotal = CostoTotal + CostoArticulo;
			DescuentoTotal = DescuentoTotal + Descuento;
			
			Escribir "Art�culos ", N, ": Costo = $", CostoArticulo, ", Descuento = $", Descuento;
		
		Escribir "Costo total por todos los art�culos: $", CostoTotal;
		Escribir "Descuento total aplicado: $", DescuentoTotal;
		
FinAlgoritmo