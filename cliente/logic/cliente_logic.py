import logging

from monitoring.crypto import encrypt, decrypt, gHMAC, vHMAC

logger = logging.getLogger('django')

from ..models import Cliente

def get_clientes():
    logger.info("Consulta de todos los clientes solicitada.")
    queryset = Cliente.objects.all()
    for cliente in queryset:
        cliente.name = decrypt(cliente.name)
    return (queryset)

def get_cliente_by_id(cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)

        #Verifica que no se haya cambiado nada del cliente (Asgura integridad)
        if not vHMAC(cliente.name, cliente.name_hmac):
            logger.error(f"Error de integridad en el cliente con ID {cliente_id}.")
            return None
        
        cliente.name = decrypt(cliente.name)
        logger.info(f"Cliente encontrado: {cliente.name}")
        return cliente
    except Cliente.DoesNotExist:
        logger.error(f"Cliente con ID {cliente_id} no encontrado.")
        return None

def create_cliente(form):
    try:
        measurement = form.save()
        measurement.name = encrypt(measurement.name)
        measurement.name_hmac = gHMAC(measurement.name)
        measurement.save()
        logger.info(f"Cliente creado exitosamente: {measurement.name}")
        return ()
    except Exception as e:
        logger.error(f"Error creando cliente: {str(e)}")
        raise e