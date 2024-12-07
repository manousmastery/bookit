from django.core.exceptions import ValidationError

from bookit_api.models.servicecategory import ServiceCategory


class CategoryService:
    def add_category(self, category_name: str) -> ServiceCategory:
        """
        Adds a new category with the given name.

        :param category_name: Name of the category to add.
        :return: The created ServiceCategory instance.
        :raises ValidationError: If the category already exists.
        """
        if ServiceCategory.objects.filter(name=category_name).exists():
            raise ValidationError(f"Category '{category_name}' already exists.")
        return ServiceCategory.objects.create(name=category_name)

    def remove_category(self, category_name: str) -> dict:
        """
        Removes a category by its name.

        :param category_name: Name of the category to remove.
        :return: A success message on successful removal.
        :raises ValidationError: If the category does not exist.
        """
        try:
            category = ServiceCategory.objects.get(name=category_name)
            category.delete()
            return {"success": f"Category '{category_name}' has been removed."}
        except ServiceCategory.DoesNotExist:
            raise ValidationError(f"Category '{category_name}' does not exist.")

    def get_all_categories(self) -> list:
        """
        Retrieves all categories.

        :return: A list of all ServiceCategory instances.
        """
        return ServiceCategory.objects.all()

    def is_category_exist(self, category_name: str) -> bool:
        """
        Checks if a category with the given name exists.

        :param category_name: Name of the category to check.
        :return: True if the category exists, otherwise False.
        """
        return ServiceCategory.objects.filter(name=category_name).exists()
