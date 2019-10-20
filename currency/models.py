from django.db import models

# Create your models here.

class Currency(models.Model):
    name  = models.CharField(max_length=4)
    toBGN = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return str(self.toBGN)

    def fromBGN(self):
        return round(1/float(self.toBGN), 2)


    # fromBGN = models.DecimalField(max_digits=5, decimal_places=2)

    # def _fromBGN(self):
    #     return round(1/float(self.toBGN), 2)

    # def save(self, *args, **kwargs):
    #     self.fromBGN = self._fromBGN()
    #     super(Currency, self).save(*args, **kwargs)
