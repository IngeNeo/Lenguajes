package Lenguajes.Java.Aerolinea;

public abstract class Asiento {

	// Inserte acá los atributos
	private char tipo;
	private String ID;
	private boolean pantallaEncendida = false;
	private double inclinacionSilla = 90.0;
	private boolean luzLecturaEncendida = false;
	private boolean luzAsistenciaEncendida = false;
	private boolean aireAcondicionadoEncendido = false;

	// Inserte acá el método constructor
	public Asiento(String ID, char tipo) {
		this.ID = ID;
		this.tipo = tipo;
	}

	// Inserte acá los SETTERS Y GETTERS
	public void setTipo(char tipo) {
		this.tipo = tipo;
	}

	public char getTipo() {
		return this.tipo;
	}

	public void setID(String id) {
		this.ID = id;
	}

	public String getID() {
		return this.ID;
	}

	public void setPantallaEncendida(boolean pantallaEncendida) {
		this.pantallaEncendida = pantallaEncendida;
	}

	public boolean isPantallaEncendida() {
		return this.pantallaEncendida;
	}

	public void setInclinacionSilla(double inclinacionSilla) {
		this.inclinacionSilla = inclinacionSilla;
	}

	public double getInclinacionSilla() {
		return this.inclinacionSilla;
	}

	public void setLuzLecturaEncendida(boolean luzLecturaEncendida) {
		this.luzLecturaEncendida = luzLecturaEncendida;
	}

	public boolean isLuzLecturaEncendida() {
		return this.luzLecturaEncendida;
	}

	public void setLuzAsistenciaEncendida(boolean luzAsistenciaEncendida) {
		this.luzAsistenciaEncendida = luzAsistenciaEncendida;
	}

	public boolean isLuzAsistenciaEncendida() {
		return this.luzAsistenciaEncendida;
	}

	public void setAireAcondicionadoEncendido(boolean aireAcondicionadoEncendido) {
		this.aireAcondicionadoEncendido = aireAcondicionadoEncendido;
	}

	public boolean isAireAcondicionadoEncendido() {
		return aireAcondicionadoEncendido;
	}

	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)

	public void gestionarAireAcondicionado() {
		this.aireAcondicionadoEncendido = !this.aireAcondicionadoEncendido;
	}

	public void gestionarPantalla() {
		this.pantallaEncendida = !this.pantallaEncendida;
	}

	public void gestionarLuzLectura() {
		this.luzLecturaEncendida = !this.luzLecturaEncendida;
	}

	public void gestionarLuzAsistencia() {
		this.luzAsistenciaEncendida = !this.luzAsistenciaEncendida;
	}

	public void aumentarInclinacion(double d) {
		if ((this.inclinacionSilla + d) <= 135) {
			this.inclinacionSilla += d;
		} else {
			this.inclinacionSilla = 135;
		}
	}

	public void disminuirInclinacion(double d) {
		if ((this.inclinacionSilla - d) >= 0) {
			this.inclinacionSilla -= d;
		} else {
			this.inclinacionSilla = 0;
		}
	}

	public abstract String imprimirMenuPantalla();
}
