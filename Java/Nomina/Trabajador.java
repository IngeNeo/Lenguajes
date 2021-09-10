package Lenguajes.Java.Nomina;

//EL CALIFICADOR GENERARÁ ERROR SI USTED NO IMPLEMENTA TODOS LOS MÉTODOS ESPECIFICADOS EN EL ENUNCIADO
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Trabajador {

	// Inserte acá los atributos
	private String nombre;
	private String CC;
	private double salarioPorHora;
	private int horasTrabajadas;
	private int diaNacimiento;
	private int mesNacimiento;
	private int yearNacimiento;

	// Inserte acá el método constructor
	public Trabajador(String nombre, String CC, double salarioPorHora, int horasTrabajadas, int diaNacimiento,
			int mesNacimiento, int yearNacimiento) {
		this.nombre = nombre;
		this.CC = CC;
		this.salarioPorHora = salarioPorHora;
		this.horasTrabajadas = horasTrabajadas;
		this.diaNacimiento = diaNacimiento;
		this.mesNacimiento = mesNacimiento;
		this.yearNacimiento = yearNacimiento;
	}

	// Inserte acá los SETTERS Y GETTERS
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getNombre() {
		return this.nombre;
	}

	public void setCC(String CC) {
		this.CC = CC;
	}

	public String getCC() {
		return this.CC;
	}

	public void setSalarioPorHora(double salarioPorHora) {
		this.salarioPorHora = salarioPorHora;
	}

	public double getSalarioPorHora() {
		return this.salarioPorHora;
	}

	public void setHorasTrabajadas(int horasTrabajadas) {
		this.horasTrabajadas = horasTrabajadas;
	}

	public int getHorasTrabajadas() {
		return this.horasTrabajadas;
	}

	public void setDiaNacimiento(int diaNacimiento) {
		this.diaNacimiento = diaNacimiento;
	}

	public int getDiaNacimiento() {
		return this.diaNacimiento;
	}

	public void setMesNacimiento(int mesNacimiento) {
		this.mesNacimiento = mesNacimiento;
	}

	public int getMesNacimiento() {
		return this.mesNacimiento;
	}

	public void setYearNacimiento(int yearNacimiento) {
		this.yearNacimiento = yearNacimiento;
	}

	public int getYearNacimiento() {
		return this.yearNacimiento;
	}

	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)
	public int calcularEdad() {
		LocalDateTime myDateObj = LocalDateTime.now();
		DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd");
		int diaActual = Integer.valueOf(myDateObj.format(myFormatObj));

		DateTimeFormatter myFormatObj2 = DateTimeFormatter.ofPattern("MM");
		int mesActual = Integer.valueOf(myDateObj.format(myFormatObj2));

		DateTimeFormatter myFormatObj3 = DateTimeFormatter.ofPattern("yyyy");
		int yearActual = Integer.valueOf(myDateObj.format(myFormatObj3));

		if (mesActual > mesNacimiento || mesActual == mesNacimiento && diaActual >= diaNacimiento)
			return yearActual - yearNacimiento;

		return yearActual - yearNacimiento - 1;
	}

	public double salarioQuincenal() {
		return this.salarioPorHora * this.horasTrabajadas;
	}
}