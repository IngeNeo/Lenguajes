using System;

namespace Calculator
{
	class Program
	{
		static void Main(string[] args)
		{
			// Declare variables and then initialize to zero.
			int num1 = 0; int num2 = 0;	
			// Display title as the C# console calculator app.
			Console.WriteLine("Calculadora de consola en C#\r");
			Console.WriteLine("------------------------\n");	
			// Ask the user to type the first number.
			Console.WriteLine("Ingrese un numero, y presione Enter");
			num1 = Convert.ToInt32(Console.ReadLine());	
			// Ask the user to type the second number.
			Console.WriteLine("Ingrese otro numero, y presione Enter");
			num2 = Convert.ToInt32(Console.ReadLine());	
			// Ask the user to choose an option.
			Console.WriteLine("Elija una opción de la siguiente lista: ");
			Console.WriteLine("\ts - Suma");
			Console.WriteLine("\tr - Resta");
			Console.WriteLine("\tm - Multiplicacion");
			Console.WriteLine("\td - Division");
			Console.Write("Cual es su opcion? ");	
			// Use a switch statement to do the math.
			switch (Console.ReadLine())
			{
				case "s":
					Console.WriteLine($"Tu resultado es: {num1} + {num2} = " + (num1 + num2));
					break;
				case "r":
					Console.WriteLine($"Tu resultado es: {num1} - {num2} = " + (num1 - num2));
					break;
				case "m":
					Console.WriteLine($"Tu resultado es: {num1} * {num2} = " + (num1 * num2));
					break;
				case "d":
					Console.WriteLine($"Tu resultado es: {num1} / {num2} = " + (num1 / num2));
					break;
			}
			// Wait for the user to respond before closing.
			Console.Write("Press any key to close the Calculator console app...");
			Console.ReadKey();
		}
	}
}
