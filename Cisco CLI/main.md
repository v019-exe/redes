| **Comando**                        | **Descripción**                                                      |
|------------------------------------|----------------------------------------------------------------------|
| `enable`                           | Acceder al modo EXEC privilegiado.                                  |
| `configure terminal`               | Entrar en el modo de configuración global.                          |
| `show running-config`              | Mostrar la configuración en ejecución.                              |
| `show startup-config`              | Mostrar la configuración de inicio almacenada en NVRAM.             |
| `interface [tipo] [número]`       | Entrar en la configuración de una interfaz específica (e.g., `interface GigabitEthernet0/1`). |
| `ip address [dirección] [máscara]`| Asignar una dirección IP y máscara a una interfaz.                  |
| `no shutdown`                      | Habilitar una interfaz que está apagada.                            |
| `shutdown`                         | Apagar una interfaz.                                               |
| `exit`                             | Salir del modo actual (puede ser modo de configuración o interfaz). |
| `show ip interface brief`          | Mostrar un resumen de las interfaces y sus direcciones IP.         |
| `ping [dirección]`                 | Probar la conectividad a una dirección IP.                          |
| `traceroute [dirección]`           | Rastrear la ruta a una dirección IP.                                |
| `copy running-config startup-config`| Guardar la configuración en ejecución como la configuración de inicio. |
| `reload`                           | Reiniciar el dispositivo.                                           |
| `show version`                    | Mostrar la versión del sistema operativo y detalles del hardware.   |
| `enable secret [contraseña]`       | Configurar una contraseña secreta para acceder al modo privilegiado.|
| `line console 0`                  | Configurar la línea de consola.                                     |
| `password [contraseña]`            | Configurar una contraseña en una línea.                             |
| `login`                            | Habilitar la autenticación de inicio de sesión en la línea.        |
| `show mac address-table`           | Mostrar la tabla de direcciones MAC en un switch.                  |
| `vlan [número]`                   | Crear o acceder a una VLAN específica.                             |
| `switchport mode access`           | Configurar el modo de un puerto como acceso.                       |
| `switchport access vlan [número]`  | Asignar un puerto a una VLAN específica.                           |
| `show vlan brief`                  | Mostrar un resumen de las VLANs configuradas.                      |
| `show ip route`                   | Mostrar la tabla de enrutamiento IP.                               |
| `ip default-gateway [dirección]`  | Configurar una puerta de enlace predeterminada para switches.      |
