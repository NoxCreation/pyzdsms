# PYZDSMS: Biblioteca para enviar SMS en Cuba con los servicios de ZonaDigital

pyzdsms es una biblioteca de Python que te permite enviar SMS dentro de Cuba usando la API de ZonaDigital (https://zdsms.cu/). Con pyzdsms puedes crear campañas de marketing, enviar notificaciones, confirmaciones y más, de forma fácil y segura.

# Requisitos previos

Para usar pyzdsms necesitas lo siguiente:
- Python >= 3.5
- pip
- Una cuenta de ZonaDigital

# Instalación

Para instalar pyzdsms, ejecuta el siguiente comando:

    pip install pyzdsms 
 
# Uso

Para enviar un SMS, primero debes importar la biblioteca:

    from pyzdsms import pyzdsms

Luego debes obtener un token de autenticación de ZonaDigital. Puedes usar un token persistente o uno temporal. En este ejemplo usaremos un token persistente que debes guardar en una variable de entorno:

    TOKEN_PERSISTENT = os.environ.get("TOKEN_PERSISTENT") # Obtén tu token de ZonaDigital y guárdalo como una variable de entorno

Después debes crear una instancia de pyzdsms con el token:

    zd = pyzdsms(TOKEN_PERSISTENT)

Finalmente, puedes enviar el SMS con el método send_sms, indicando el número de destino y el texto del mensaje. El método te devuelve una respuesta con el mensaje y el id del SMS: 

    number_send = "535*******" # Número de destino
    response = zd.send_sms(
        number_send,
        "Esto es un sms desde pyzdsms" # Texto del mensaje
    )
    message = response.getMessage() # Mensaje de la respuesta
    id = response.getId() # Id del SMS
    print("message", message, "id", id) # Imprime el mensaje y el id

Con este código puedes enviar un sms a cualquier persona dentro de Cuba. Para obtener el estado de este SMS puede con el id obtener la información correspondiente:

    details = zd.details_sms(id)
    print(details.getStatus())
    print(details.getText())
    print(details.getCreatedAt())
    print(details.getRecipient())
    print(details.getSmsCount())
    print(details.getVia())

# Listar SMS

Puede listar todos los SMS enviados de una forma muy simple:

    all_sms = zd.get_all_sms()
    for sms in all_sms:
        print(sms.getStatus())
        print(sms.getText())
        print(sms.getCreatedAt())
        print(sms.getRecipient())
        print(sms.getSmsCount())
        print(sms.getVia())

Si desea obtener la información de forma escalada, puede paginar la obtención:

    all_sms, count_items, count_paginated = zd.get_all_sms(page=2)
    print("count items", count_items)
    print("count paginated", count_paginated)
    for sms in all_sms:
      print(sms.getStatus())
      print(sms.getText())
      print(sms.getCreatedAt())
      print(sms.getRecipient())
      print(sms.getSmsCount())
      print(sms.getVia())


# Crear campañas

Una campaña consiste en el envío masivo de SMS a un listado de Lead o Posibles Clientes que tenga como estrategia de marqueting. La biblioteca brinda de una forma sencilla para crear campañas con este registro de usuarios que usted posea:

    campaign = zd.create_campaign()\
        .addName("Campaña#12")\
        .addRecipients(number_send1)\
        .addRecipients(number_send2)\
        .setText("Esto es una prueba del envio de una campaña por SMS.")\
        .send()
    message = campaign.getMessage()
    id = campaign.getId()

En el ejemplo suponemos como "number_send1" y "number_send2" como dos números de dicha campaña a los que se le enviará este SMS. Puede también hacerlo de la siguiente forma:

    numbers_send = [number_send1, number_send2]
    campaign = zd.create_campaign().addName("Campaña#12")
    for ns in numbers_send:
        campaign.addRecipients(ns)
    response = campaign.setText("Esto es una prueba del envio de una campaña por SMS.").send()
    message = response.getMessage()
    id = response.getId()

En el ejemplo suponemos que tenga un arreglo de números de teléfonos a los cuales desea enviar los SMS.

# Obtener un listado de todas las campañas

Para obtener el listado de todas las campañas puede tomar este ejemplo:

    campaigns = zd.create_campaign().getAll()
    for campaign in campaigns:
        print(campaign.getVia())
        print(campaign.getId())
        print(campaign.getText())
        print(campaign.getRecipients())
        print(campaign.getSmsCount())
        print(campaign.getCreatedAt())
        print(campaign.getStatus())
        print(campaign.getName())
        print(campaign.getDelivered())
        print(campaign.getUserId())

# Contribución

Si te interesa contribuir a pyzdsms, puedes hacerlo de las siguientes formas:

- Reportando errores o sugerencias en la sección de issues.
- Haciendo un fork del repositorio y enviando un pull request con tus cambios.
- Mejorando la documentación o los ejemplos.
- Compartiendo el proyecto con otros usuarios que puedan beneficiarse de él.

# Licencia

pyzdsms está licenciado bajo la GNU General Public License v3.0. Consulta el archivo LICENSE para más detalles.
