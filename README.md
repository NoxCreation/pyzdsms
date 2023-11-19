# PYZDSMS
Zdsms.cu es un servicio en internet de Zona Digital (https://zdsms.cu/) con el que puedes enviar sms dentro de territorio cubano.

La siguiente biblioteca facilita el uso de la API que ofrece ZonaDigital (https://zdsms.cu/documentation). Estaremos agradecido de cualquier colaboración que desee hacer.

# ¿Cómo obtener acceso?

Para obtener acceso a los servicios de ZonaDigital para enviar SMS, debe crearse una cuenta en https://zdsms.cu/. Esta página lo redirige a un panel de control donde tendrá acceso a toda la información del servicio SMS.

En el menú Recargar debe comprar algún plan de los que se ofertan o crear un plan personalizado a sus intereses.

# ¿Cómo instalar?

Para instalar solo debe ejecutar el comando pip de instalación de la biblioteca.

    pip install pyzdsms
 
 Requiere Python >= 3.5 con pip. (https://pypi.org/project/pyzdsms/)
 
 
# ¿Cómo enviar un sms?

Una vez tenga instalada la biblioteca debe en su proyecto importarla.

    from pyzdsms import pyzdsms

Luego debe obtener un token de autenticación. Es importante aclarar que la plataforma de ZonaDigital admite dos formas de obtener el token de autenticación. La primera es obtener un token en tiempo de ejecución que expira pasada las 24h. La otra es crear un token que no expire en el tiempo. La biblioteca de pyzdsms funciona con cualquiera de los dos tokens, pero por el momento recomendamos generar un token no expirable.

Para ello vaya a Tokens en el panel de control y dele al botón Crear Token Persistente. Escriba un nombre de identificación del token y guarde el mismo en las variables de entorno de su proyecto de forma segura donde no pueda ser accedida por terceros.

Una vez tenga en su poder este Token, debe crear una instancia:

    zd = pyzdsms(TOKEN_PERSISTENT)

De esta forma ya puede tener acceso a todas las funciones desde la variable "zd". Para enviar el SMS dejamos un ejemplo:

    number_send = "535*******"
    response = zd.send_sms(
        number_send,
        "Esto es un sms desde pyzdsms"
    )
    message = response.getMessage()
    id = response.getId()
    print("message", message, "id", id)

Con este código basta para que pueda enviarse un sms a cualquier persona dentro de Cuba. Para obtener el estado de este SMS puede con el id obtener la información correspondiente:

    details = zd.details_sms(id)
    print(details.getStatus())
    print(details.getText())
    print(details.getCreatedAt())
    print(details.getRecipient())
    print(details.getSmsCount())
    print(details.getVia())

# Obtener información de todos los SMS enviados

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

Una campaña consiste en el envio masivo de SMS a un listado de Lead o Posibles Clientes que tenga como estrategia de marqueting. La biblioteca brinda de una forma sencilla para crear campañas con este registro de usuarios que usted posea:

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
