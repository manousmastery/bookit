from rest_framework import serializers
from bookit_api.models.review import Review


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review_id', 'client', 'commentaire', 'grade', 'client', 'business']
        read_only_fields = ['review_id']

    def validate_grade(self, value):
        """Ensure the grade is within the allowed range."""
        if value not in [choice for choice in Review.GRADE_CHOICES]:
            raise serializers.ValidationError("Grade must be between 1 and 5.")
        return value
