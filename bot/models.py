from django.db import models

# Create your models here.


class Clients(models.Model):
    user_id = models.IntegerField(unique=True)
    step = models.IntegerField(default=0)
    first_name = models.CharField(max_length=256, blank=True, null=True)
    familiyasi = models.CharField(max_length=128, blank=True, null=True)
    ismi = models.CharField(max_length=128, blank=True, null=True)
    otasini_ismi = models.CharField(max_length=128, blank=True, null=True)
    tugulgan_sana = models.CharField(max_length=128, blank=True, null=True)
    malumoti = models.CharField(max_length=64, blank=True, null=True)
    talim_olgan = models.CharField(max_length=1024, blank=True, null=True)
    oilaviy = models.CharField(max_length=64, blank=True, null=True)
    mutaxasis = models.CharField(max_length=128, blank=True, null=True)
    manzil_vil = models.CharField(max_length=128, blank=True, null=True)
    manzil_tum = models.CharField(max_length=128, blank=True, null=True)
    manzil = models.CharField(max_length=1024, blank=True, null=True)
    ish_joyi = models.CharField(max_length=512, blank=True, null=True)
    lavozimi = models.CharField(max_length=512, blank=True, null=True)
    tel_raq = models.CharField(max_length=512, blank=True, null=True)
    tel_raq_qosh = models.CharField(max_length=512, blank=True, null=True)
    qay_til = models.CharField(max_length=512, blank=True, null=True)
    ish_davri = models.CharField(max_length=1024, blank=True, null=True)
    qay_das = models.CharField(max_length=512, blank=True, null=True)
    qosh_mal = models.CharField(max_length=1024, blank=True, null=True)
    maosh = models.IntegerField(default=0)
    yaqin_qar = models.CharField(max_length=256, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        if self.first_name != None:
            return self.first_name
        else:
            return f'Bot_User: {self.user_id}'

