// Creamos array con los meses del año//
const meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
// Creamos array con los días de la semana //
const dias_semana = ['Domingo', 'Lunes', 'martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
// Creamos el objeto fecha instanciándolo con la clase Date//
const fecha = new Date();
Swal.fire({
    title: 'Fecha y hora actuales',
    text: "Hoy es" + " " + dias_semana[fecha.getDay()] + ', ' + fecha.getDate() + ' de ' + meses[fecha.getMonth()] + ' de ' + fecha.getFullYear() + " y son las " + fecha.getHours() + ":" + fecha.getMinutes() + ":" + fecha.getSeconds(),
    imageUrl: 'https://cdn.datosmundial.com/pics/uhr.jpg',
    imageWidth: 400,
    imageHeight: 200,
    imageAlt: 'Custom image',
})