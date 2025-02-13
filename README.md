# delete-property

Este proyecto es una utilidad para eliminar propiedades de objetos en JavaScript de manera segura y eficiente, incluso cuando las propiedades están profundamente anidadas.

## 🚀 Características

- Elimina propiedades de objetos anidados utilizando una cadena de ruta.
- Devuelve `true` si la propiedad se eliminó con éxito.
- Devuelve `false` si la propiedad no existe o si el argumento proporcionado no es un objeto.

## 📦 Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/HenryJulian3/delete-property.git
   cd delete-property
   ```

2. Instala las dependencias:

   ```sh
   npm install
   ```

## 🛠 Uso

1. Importa la función en tu proyecto:

   ```javascript
   const deleteProperty = require('delete-property');
   ```

2. Utiliza la función para eliminar una propiedad anidada:

   ```javascript
   const obj = {
     n: {
       p: {
         m: true
       }
     }
   };

   const result = deleteProperty('n.p.m', obj);
   console.log(result); // true
   console.log(obj.n.p.hasOwnProperty('m')); // false
   ```

## 📋 Notas

- Si intentas eliminar una propiedad que no existe, la función devolverá `false`.
- Si el argumento proporcionado no es un objeto, la función también devolverá `false`.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT.
