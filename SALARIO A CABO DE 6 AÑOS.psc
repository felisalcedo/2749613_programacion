Algoritmo CalcularSalario
    Definir SalarioInicial, Anio, SalarioActual Como Real;
	
    SalarioInicial = 1500;
    SalarioActual = SalarioInicial;
    Anio = 1;
	
    Mientras Anio <= 6 Hacer
        SalarioActual = SalarioActual + (SalarioActual * 0.10);   // Incremento del 10%
        Escribir "A�o ", Anio, ": Salario = $", SalarioActual;
        Anio = Anio + 1;
    Fin Mientras
	
    Escribir "Salario al cabo de 6 a�os: $", SalarioActual;
	
FinAlgoritmo