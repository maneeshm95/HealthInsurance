from django.shortcuts import render
from .models import ClaimStatus,Claim
# Create your views here.


def getClaimData(request):
    all_claim_data = Claim.objects.all()
    context = {
        'all_claim_data_key':all_claim_data
    }


    return render(request, 'claim/claimdata.html',context)