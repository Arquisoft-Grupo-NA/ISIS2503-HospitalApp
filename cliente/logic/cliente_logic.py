import logging
from monitoring.crypto import encrypt, decrypt, gHMAC, vHMAC

logger = logging.getLogger('django')

from ..models import Cliente


def get_clientes():
    logger.info("Consulta de todos los clientes solicitada.")
    queryset = Cliente.objects.all()
    for cliente in queryset:
        try:
            cliente.name = decrypt(cliente.name)
            cliente.info_personal = decrypt(cliente.info_personal)
        except Exception as e:
            logger.error(f"Error al descifrar los datos del cliente con ID {cliente.id}: {str(e)}")
            cliente.name = None
            cliente.info_personal = None
    return queryset

def get_cliente_by_id(cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)

        #Verifica que no se haya cambiado nada del cliente (Asgura integridad)
        if not vHMAC(cliente.name, cliente.name_hmac):
            logger.error(f"Error de integridad en el cliente con ID {cliente_id}.")
            return None
        
        cliente.name = decrypt(cliente.name)
        cliente.info_personal = decrypt(cliente.info_personal)
        logger.info(f"Cliente encontrado: {cliente.name}")
        return cliente
    except Cliente.DoesNotExist:
        logger.error(f"Cliente con ID {cliente_id} no encontrado.")
        return None

def create_cliente(form):
    try:
        cliente = form.save()
        cliente.name = encrypt(cliente.name)
        cliente.info_personal = encrypt(cliente.info_personal)
        cliente.name_hmac = gHMAC(cliente.name)
        cliente.save()
        logger.info(f"Cliente creado exitosamente: {cliente.name}")
        return cliente
    except Exception as e:
        logger.error(f"Error creando cliente: {str(e)}")
        raise e
