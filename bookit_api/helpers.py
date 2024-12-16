from dataclasses import dataclass

from django.core.exceptions import ValidationError

from bookit_api.models import Business, Service


@dataclass
class BusinessServiceDetailsParams:
    business: Business | None = None
    service: Service | None = None
    business_id: int | None = None
    service_id: int | None = None
    price: float | None = None
    duration: int | None = None
    showed_name: str | None = None
    showed_description: str | None = None

    def validate_details_to_add(self):
        if not self.service_id:
            raise ValidationError(
                f'service_id must be provided if you want add a service for the business with id {self.business_id}'
            )

        if not self.price or self.price <= 0:
            raise ValidationError(
                f'Price must be provided if you want to add a service for the business with id {self.business_id}'
            )

        if not self.duration and self.duration <= 0:
            raise ValidationError(
                f'price must be provided if you want to add a service for the business with id {self.business_id}'
            )

    def validate_details_to_update(self):
        if (self.price and self.price <= 0) or (self.duration and self.duration <= 0):
            raise ValueError("Price and duration must be greater than zero.")

        if not self.price and not self.duration:
            raise ValueError("Either price or duration must be provided.")

    def validate_details_to_delete(self):
        if not self.service_id:
            raise ValidationError(
                f'"service_id" must be provided if you want to remove a service for the business with id {self.business_id}'
            )
        if not self.business_id:
            raise ValidationError(
                f'"business_id" must be provided if you want remove a service for the business with id {self.business_id}'
            )
