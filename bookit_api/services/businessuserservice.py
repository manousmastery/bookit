from bookit_api.models import BusinessUser


class BusinessUserService:
    def get(self, business_id: int):
        return BusinessUser.objects.filter(business=business_id)