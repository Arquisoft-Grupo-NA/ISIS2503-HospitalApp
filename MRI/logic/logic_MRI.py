import logging
from monitoring.crypto import encrypt, decrypt
logger = logging.getLogger('django')

from ..models import MRI, Cliente

def get_mris():
    logger.info("Consulta de todos los MRIs solicitada.")
    queryset = MRI.objects.all().order_by('id')
    for mri in queryset:
        mri.descripcion = decrypt(mri.descripcion)
    return queryset


def get_mri(user_pk):
    logger.info(f"Consulta del último MRI para el cliente {user_pk}")
    mri = MRI.objects.filter(cliente=user_pk).order_by('-fecha', '-hora').first()
    return mri

def update_mri(mri_pk, new_data):
    try:
        mri = MRI.objects.get(pk=mri_pk)
        mri.descripcion = new_data.get("descripcion", mri.descripcion)
        mri.fecha = new_data.get("fecha", mri.fecha)
        mri.hora = new_data.get("hora", mri.hora)
        mri.save()
        logger.info(f"MRI actualizado exitosamente: ID {mri_pk}")
        return mri
    except MRI.DoesNotExist:
        logger.error(f"Intento fallido de actualizar MRI: ID {mri_pk} no encontrado")
        return None

def create_mri(form):
    try:
        measurement = form.save()
        measurement.descripcion = encrypt(measurement.descripcion)
        measurement.save()
        logger.info(f"MRI creado exitosamente")
        return ()
    except Exception as e:
        logger.error(f"Error creando MRI: {str(e)}")
        raise e