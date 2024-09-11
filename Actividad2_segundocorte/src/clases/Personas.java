/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package clases;

import java.util.ArrayList;
import java.util.List;

public class Personas {

    private String nombre;
    private String apellido;
    private String dirrecion;
    private String edad;

    public Personas(String nombre, String apellido, String dirrecion, String edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.dirrecion = dirrecion;
        this.edad = edad;
    }

    /**
     * @return the nombre
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * @param nombre the nombre to set
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    /**
     * @return the apellido
     */
    public String getApellido() {
        return apellido;
    }

    /**
     * @param apellido the apellido to set
     */
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    /**
     * @return the dirrecion
     */
    public String getDirrecion() {
        return dirrecion;
    }

    /**
     * @param dirrecion the dirrecion to set
     */
    public void setDirrecion(String dirrecion) {
        this.dirrecion = dirrecion;
    }

    /**
     * @return the edad
     */
    public String getEdad() {
        return edad;
    }

    /**
     * @param edad the edad to set
     */
    public void setEdad(String edad) {
        this.edad = edad;
    }
    private final List<String> datos = new ArrayList<>();

    public void almacenarDatos() {
        String personasInfo = "Nombre: " + this.nombre + ", Apellido: " + this.apellido + ", Dirrecion: " + this.dirrecion + ", Edad: " + this.edad;
        datos.add(personasInfo);
    }

    public List<String> getDatos() {
        return datos;
    }
}
