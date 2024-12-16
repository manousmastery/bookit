from djongo import models


class Review(models.Model):
    GRADE_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    review_id = models.AutoField(primary_key=True)
    commentaire = models.TextField()
    grade = models.IntegerField(choices=GRADE_CHOICES, default=0)
    client = models.ForeignKey('User', on_delete=models.CASCADE)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
