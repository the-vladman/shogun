[![Stories in Ready](https://badge.waffle.io/mxabierto/shogun.png?label=ready&title=Ready)](https://waffle.io/mxabierto/shogun)
[![Build Status](https://travis-ci.org/mxabierto/shogun.svg)](https://travis-ci.org/mxabierto/shogun)
[![Coverage Status](https://coveralls.io/repos/mxabierto/shogun/badge.svg?branch=master&service=github)](https://coveralls.io/github/mxabierto/shogun?branch=master)
# shogun

[![Join the chat at https://gitter.im/mxabierto/shogun](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/mxabierto/shogun?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
The real commander-in-chief of the Data Squad.

_[mxabierto/ckanops as a service](https://github.com/mxabierto/ckanops)_

![shogun](https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Minamoto_no_Yoritomo.jpg/377px-Minamoto_no_Yoritomo.jpg)

## More info

For more information on installation, configuration, and usage, visit [the Wiki](https://github.com/mxabierto/shogun/wiki).


# NOTA IMPORTANTE

Para poder registrar correctamente el nivel de gobierno se debe utilizar la variable de ambiente *VOCABULARY_GOV_TYPE_ID* en la definicion del deploy de *shogun*.

Para obtener el ID del vocabulario *gov_types* se debe consultar el API en las siguiente rutas dependiendo del ambiente: 

- QA: *http://10.20.55.7/busca/api/3/action/vocabulary_list*
- QA: *https://datos.gob.mx/busca/api/3/action/vocabulary_list*

De la respuesta se debe extraer el *hash* del key *id* antes del nombre *gov_types*.

Ejemplo de la respuesta:
```
  "help": "https://datos.gob.mx/busca/api/3/action/help_show?name=vocabulary_list",
  "success": true,
  "result": [
    {
      "tags": [
        ...
      ],
      "id": "64fc6523-df3659-434342sd-a9d8-f272c9bd898d34sfd",
      "name": "gov_types"
    }
  ]
}
```