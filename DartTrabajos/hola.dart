//capturar datos de la consola
import 'dart:io';
void main(List<String> args) {
  print('Hola Mundo');
  print('Escriba Su nombre');
  String nombre = stdin.readLineSync().toString();
  print('Buen dia $nombre');
}