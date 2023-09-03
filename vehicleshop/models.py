from django.db import models

class Carro(models.Model):
    marca_do_carro = models.CharField(max_length = 20)
    modelo_do_carro = models.CharField(max_length= 20)
    ano_do_carro = models.CharField(max_length=4)
    
    def __str__(self):
        return f"Marca do carro: {self.marca}, modelo: {self.modelo} e ano do carro é: {self.ano} "
    
class Moto(models.Model):
    marca_da_moto = models.CharField(max_length = 20)
    modelo_da_moto = models.CharField(max_length= 20)
    ano_da_moto = models.CharField(max_length= 4)
    cilindrada_da_moto = models.CharField(max_length= 5)

    def __str__(self):
        return f"Marca da Moto: {self.marca_da_moto}, modelo: {self.modelo_da_moto} e o do moto é: {self.ano_da_moto} e tem {self.cilindrada_da_moto} Cilindradas!"
