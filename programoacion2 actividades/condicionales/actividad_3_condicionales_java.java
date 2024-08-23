package clase4;

import java.util.Scanner;

public class actividad_3_condicionales_java {
    public static void main(String[] args) {
Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese su nombre:");
        String Nombre = entrada.next();
        System.out.print("Ingrese su apellido:");
        String Apellido = entrada.next();
        System.out.print("Ingrese su edad:");
        int edad = entrada.nextInt();
        System.out.print("Ingrese su sexo 1(Masculino) o 2(Femenino):");
        int sexo = entrada.nextInt();
        if(edad>=18){
            System.out.println("Usted es mayor de edad");
        }else{
            System.out.println("Usted es menor de edad");
        }
        if(sexo==1){
            System.out.println("Usted es Hombre");
        }else{
            System.out.println("Usted es Mujer");
        }
        entrada.close();
    } 

}
    

