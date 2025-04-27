import logging

logger = logging.getLogger('django')

from ..models import Cliente

def get_clientes():
    logger.info("Consulta de todos los clientes solicitada.")
    queryset = Cliente.objects.all()
    return (queryset)

def create_cliente(form):
    try:
        measurement = form.save()
        measurement.save()
        logger.info(f"Cliente creado exitosamente: {measurement.name}")
        return ()
    except Exception as e:
        logger.error(f"Error creando cliente: {str(e)}")
        raise e