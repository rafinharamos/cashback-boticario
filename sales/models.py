from django.db import models

from salesman.models import Salesman

STATUS_CHOICES = (("V", "Em Validação"), ("A", "Aprovado"), ("N", "Negado"))


class Sale(models.Model):
    salesman = models.ForeignKey(Salesman, on_delete=models.DO_NOTHING)
    code = models.CharField("Code", max_length=20)
    value = models.FloatField("Value", max_length=20)
    date = models.DateField(auto_now_add=True)
    cashback_percent = models.IntegerField("% cashback")
    cashback_value = models.FloatField("Value")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="V")

    class Meta:
        verbose_name_plural = "Sales"

    @staticmethod
    def get_initial_status(self):
        if self.salesman and self.salesman.cpf == "15350946056":
            return "A"
        return "V"

    @staticmethod
    def cashback_total_percent(value):
        if value <= 1000:
            cashback_total_percent = 10
        elif 1001 < value <= 1500:
            cashback_total_percent = 15
        else:
            cashback_total_percent = 20
        return cashback_total_percent

    def save(self, *args, **kwargs):
        if not self.id:
            self.cashback_percent = self.cashback_total_percent(self.value)
            self.cashback_value = self.value / self.cashback_percent
            self.status = self.get_initial_status(self)
        super(Sale, self).save(*args, **kwargs)
