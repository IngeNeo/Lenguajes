package Lenguajes.Java.Sumar;

import org.junit.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Before;

public class SumarTest {

	@Before
	public void setup() {

	}

	@Test
	public void testSumar() {
		int a = 2;
		int b = 3;

		Sumar numeros = new Sumar();

		int resultado = numeros.SumarNumeros(a, b);

		assertEquals(5, resultado);

	}
}
