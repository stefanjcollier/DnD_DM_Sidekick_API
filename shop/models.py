from django.db import models


class Product(models.Model):
  name = models.CharField(max_length=240, null=False, blank=False)
  weight = models.FloatField(verbose_name='Weight in lbs', default=0)
  gp_price = models.IntegerField(verbose_name='Price in gold', default=0)
  sp_price = models.IntegerField(verbose_name='Price in silver', default=0)

  def price_str(self):
    items = []
    if self.gp_price is not None and self.gp_price > 0:
      items.append(f"{self.gp_price:,} Gold")

    if self.sp_price is not None and self.sp_price > 0:
      items.append(f"{self.sp_price:,} Silver")

    return ', '.join(items)

  def _str_(self):
    return f"{self.name}  ({self.price_str()})"

  def __repr__(self):
    return self._str_()


class Shop(models.Model):
  name = models.CharField(max_length=240, null=False, blank=False)
  description = models.CharField(max_length=240, default='')
  products = models.ManyToManyField(Product)

  def _str_(self):
    return self.name
