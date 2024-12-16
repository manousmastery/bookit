from django.core.exceptions import ValidationError

from bookit_api.models.servicecategory import ServiceCategory
from bookit_api.serializers.servicecategoryserializer import ServiceCategorySerializer


class CategoryService:
    def add_category(self, category_data: dict) -> ServiceCategory:
        serializer = ServiceCategorySerializer(data=category_data)
        serializer.is_valid(raise_exception=True)

        name, description = category_data.get('name'), category_data.get('description')

        if ServiceCategory.objects.filter(name=name.lower()).exists():
            raise ValidationError(f"Category '{name}' already exists.")

        category = ServiceCategory.objects.create(name=name.lower(), description=description)
        return ServiceCategorySerializer(category).data

    def remove_category(self, category_name: str) -> dict:
        try:
            category = ServiceCategory.objects.get(name=category_name.lower())
            category.delete()
            return {"success": f"Category '{category_name}' has been removed."}
        except ServiceCategory.DoesNotExist:
            raise ValidationError(f"Category '{category_name}' does not exist.")

    def get_all_categories(self) -> list:
        categories = ServiceCategory.objects.all()
        return ServiceCategorySerializer(categories, many=True).data

    def is_category_exist(self, category_name: str) -> bool:
        return ServiceCategory.objects.filter(name=category_name).exists()

    def get_category_from_name(self, category: str):
        category = ServiceCategory.objects.get(name=category)
        if not category:
            raise ServiceCategory.DoesNotExist
        return category
