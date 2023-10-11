Algoritmo CalcularPrecio
    Definir Precio, Descuento, PrecioConDescuento, Iva, PrecioFinal Como Real;
	
    Escribir "Ingrese el precio del artículo: ";
    Leer Precio;
	
    Descuento = Precio * 0.20;// Aplicar descuento del 20%
	PrecioConDescuento = Precio - Descuento;//
    Iva = PrecioConDescuento * 0.15;   // Agregar 15% de IVA
	PrecioFinal = PrecioConDescuento + Iva;
	
	Escribir "Descuento: ", Descuento;
    Escribir "Precio con descuento: ", PrecioConDescuento;
	Escribir "Iva: ", Iva;
    Escribir "Precio final: ", PrecioFinal;
	
FinAlgoritmo