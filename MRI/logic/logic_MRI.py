from collections import Counter
from ..models import MRI, Cliente

def get_mris():
    return MRI.objects.all().order_by('id')


def get_mri(user_pk):
    mri = MRI.objects.filter(cliente=user_pk).order_by('-fecha', '-hora').first()
    return mri

def update_mri(mri_pk, new_data):
    try:
        mri = MRI.objects.get(pk=mri_pk) 
        mri.descripcion = new_data.get("descripcion", mri.descripcion)
        mri.fecha = new_data.get("fecha", mri.fecha)
        mri.hora = new_data.get("hora", mri.hora)
        mri.save()
        return mri
    except MRI.DoesNotExist:
        return None

def create_mri(form):
    measurement = form.save()
    measurement.save()
    return ()
