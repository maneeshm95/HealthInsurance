from django.shortcuts import render
from .models import Patient

def getAllPatients(request):

    all_patients = Patient.objects.all()
    context ={
        'all_patients_key' : all_patients
    }

    return render(request,'patient/all_patient.html', context)


def get_patient_info(request, patientid ):
    get_one_patient = Patient.objects.filter(patient_id=patientid)
    context = {
        'get_one_patient_key' : get_one_patient
    }

    return render(request,'patient/patientdetails.html',context)