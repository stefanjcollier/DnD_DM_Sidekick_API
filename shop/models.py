from django.db import models


class Product(models.Model):
  name = models.CharField(max_length=240, null=False, blank=False)
  weight = models.FloatField(verbose_name='Weight in lbs', default=0)
  gp_price = models.IntegerField(verbose_name='Price in gold', default=0)
  sp_price = models.IntegerField(verbose_name='Price in silver', default=0)

  def price_str(self):
    string = ''
    if self.gp_price is not None:
      string += f"{self.gp_price} gp"

    if self.sp_price is not None:
      string += f"{self.sp_price} sp"

    return string

  def _str_(self):
    return f"{self.name}  ({self.price_str()})"
