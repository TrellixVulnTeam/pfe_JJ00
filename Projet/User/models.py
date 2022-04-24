from tabnanny import verbose
from tkinter import CASCADE
from django.db import models


# Create your models here.


class Norme(models.Model):
<<<<<<< HEAD
    id = models.TextField(primary_key=True, )
    titre = models.TextField()
    version = models.IntegerField()
    descriptif = models.TextField()
=======
    id=models.TextField(primary_key=True,)
    titre=models.TextField()
    version=models.IntegerField(default=None, blank=True, null=True)
    descriptif=models.TextField(default=None, blank=True, null=True)
>>>>>>> 56a66dca5e36b1b5bd67d8340cb38a4c42b6b448

    class Meta:
        verbose_name_plural = "Normes"

    def __str__(self) -> str:
        return self.titre


class Chapitre(models.Model):
<<<<<<< HEAD
    id_chap = models.TextField(primary_key=True)
    id_norme = models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version = models.IntegerField()
    titre = models.TextField()
    descriptif = models.TextField()
=======
    id_chap=models.TextField(primary_key=True)
    id_norme=models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version=models.IntegerField()
    titre=models.TextField()
    descriptif=models.TextField(default=None, blank=True, null=True)
>>>>>>> 56a66dca5e36b1b5bd67d8340cb38a4c42b6b448

    class Meta:
        verbose_name_plural = "Chapitres"

    def __str__(self) -> str:
        return self.titre


class SC_niv1(models.Model):
<<<<<<< HEAD
    id_norme = models.ForeignKey(Norme, verbose_name="Normes", on_delete=models.CASCADE)
    version = models.IntegerField()
    id_chap = models.ForeignKey(Chapitre, verbose_name="Chapitres", on_delete=models.CASCADE)
    id_Sc1 = models.TextField(primary_key=True)
    titre = models.TextField()
    objectif = models.TextField()
=======
    
    id_norme=models.ForeignKey(Norme, verbose_name="Normes", on_delete=models.CASCADE)
    version=models.IntegerField()
    id_chap=models.ForeignKey(Chapitre,verbose_name="Chapitres",on_delete=models.CASCADE)
    id_Sc1=models.TextField(primary_key=True)
    titre=models.TextField()
    objectif=models.TextField(default=None, blank=True, null=True)
>>>>>>> 56a66dca5e36b1b5bd67d8340cb38a4c42b6b448

    class Meta:
        verbose_name_plural = "Sc_niv1"

    def __str__(self) -> str:
        return self.titre


class SC_niv2(models.Model):
<<<<<<< HEAD
    id_norme = models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version = models.IntegerField()
    id_chap = models.ForeignKey(Chapitre, verbose_name="Chapitres", on_delete=models.CASCADE)
    id_Sc1 = models.ForeignKey(SC_niv1, verbose_name=("Sc_niv1"), on_delete=models.CASCADE)
    id_Sc2 = models.TextField(primary_key=True)
    titre = models.TextField()
    objectif = models.TextField()
=======
    id_norme=models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version=models.IntegerField()
    id_chap=models.ForeignKey(Chapitre,verbose_name="Chapitres",on_delete=models.CASCADE)
    id_Sc1=models.ForeignKey(SC_niv1, verbose_name=("Sc_niv1"), on_delete=models.CASCADE)
    id_Sc2=models.TextField(primary_key=True)
    titre=models.TextField()
    objectif=models.TextField(default=None, blank=True, null=True)
>>>>>>> 56a66dca5e36b1b5bd67d8340cb38a4c42b6b448

    class Meta:
        verbose_name_plural = "Sc_niv2"

    def __str__(self) -> str:
        return self.titre


class SC_niv3(models.Model):
<<<<<<< HEAD
    id_norme = models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version = models.IntegerField()
    id_chap = models.ForeignKey(Chapitre, verbose_name="Chapitres", on_delete=models.CASCADE)
    id_Sc1 = models.ForeignKey(SC_niv1, verbose_name=("Sc_niv1"), on_delete=models.CASCADE)
    id_Sc2 = models.ForeignKey(SC_niv2, verbose_name=("Sc_niv2"), on_delete=models.CASCADE)
    id_Sc3 = models.TextField(primary_key=True)
    titre = models.TextField()
    objectif = models.TextField()
=======
    id_norme=models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version=models.IntegerField()
    id_chap=models.ForeignKey(Chapitre,verbose_name="Chapitres",on_delete=models.CASCADE)
    id_Sc1=models.ForeignKey(SC_niv1, verbose_name=("Sc_niv1"), on_delete=models.CASCADE)
    id_Sc2=models.ForeignKey(SC_niv2, verbose_name=("Sc_niv2"), on_delete=models.CASCADE)
    id_Sc3=models.TextField(primary_key=True)
    titre=models.TextField()
    objectif=models.TextField(default=None, blank=True, null=True)
>>>>>>> 56a66dca5e36b1b5bd67d8340cb38a4c42b6b448

    class Meta:
        verbose_name_plural = "Sc_niv3"

    def __str__(self) -> str:
        return self.titre


class Point(models.Model):
<<<<<<< HEAD
    id_norme = models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version = models.IntegerField()
    id_chap = models.ForeignKey(Chapitre, verbose_name="Chapitres", on_delete=models.CASCADE)
    id_Sc1 = models.ForeignKey(SC_niv1, verbose_name=("Sc_niv1"), on_delete=models.CASCADE)
    id_Sc2 = models.ForeignKey(SC_niv2, verbose_name=("Sc_niv2"), on_delete=models.CASCADE)
    id_Sc3 = models.ForeignKey(SC_niv3, verbose_name=("Sc_niv3"), on_delete=models.CASCADE)
    point = models.TextField()
    type_actif = models.TextField()
    fct_sec = models.TextField()
=======
    id_norme=models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version=models.IntegerField()
    id_chap=models.ForeignKey(Chapitre,verbose_name="Chapitres",on_delete=models.CASCADE)
    id_Sc1=models.ForeignKey(SC_niv1, verbose_name=("Sc_niv1"), on_delete=models.CASCADE,default=None, blank=True, null=True)
    id_Sc2=models.ForeignKey(SC_niv2, verbose_name=("Sc_niv2"), on_delete=models.CASCADE,default=None, blank=True, null=True)
    id_Sc3=models.ForeignKey(SC_niv3, verbose_name=("Sc_niv3"), on_delete=models.CASCADE,default=None, blank=True, null=True)
    id_point=models.TextField(primary_key=True,default="default-id")
    titre=models.TextField(default=None, blank=True, null=True)
    point=models.TextField()
    type_actif=models.TextField(default=None, blank=True, null=True)
    fct_sec=models.TextField(default=None, blank=True, null=True)
>>>>>>> 56a66dca5e36b1b5bd67d8340cb38a4c42b6b448

    class Meta:
        verbose_name_plural = "Points"

    def __str__(self) -> str:
        return self.titre


class Test(models.Model):
<<<<<<< HEAD
    id_test = models.AutoField(primary_key=True)
    id_client = models.IntegerField()
    id_norme = models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    finished = models.BooleanField()
    date = models.DateField()
    last_point = models.TextField()
=======
    id_test=models.TextField(primary_key=True)
    id_client=models.IntegerField()
    id_norme=models.ForeignKey(Norme, verbose_name=("Normes"),on_delete=models.CASCADE)
    finished=models.BooleanField()
    date=models.DateField(default=None, blank=True, null=True)
    last_point=models.TextField(default=None, blank=True, null=True)
>>>>>>> 56a66dca5e36b1b5bd67d8340cb38a4c42b6b448

    class Meta:
        verbose_name_plural = "Tests"

    def __str__(self) -> str:
        return self.id_test


class Question_Generale(models.Model):
    id_qst = models.TextField(primary_key=True)
    id_norme = models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        verbose_name_plural = "Questions_Generales"

    def __str__(self) -> str:
        return self.id_qst

<<<<<<< HEAD
=======
class Reponse(models.Model):
    id_reponse=models.TextField(primary_key=True)
    id_test=models.ForeignKey(Test,verbose_name="Tests",on_delete=models.CASCADE)
    id_qst=models.ForeignKey(Question_Generale,verbose_name="Questions_Generales",on_delete=models.CASCADE)
    id_norme=models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version=models.IntegerField()
    id_chap=models.ForeignKey(Chapitre,verbose_name="Chapitres",on_delete=models.CASCADE)
    id_Sc1=models.ForeignKey(SC_niv1, verbose_name=("Sc_niv1"), on_delete=models.CASCADE,default=None, blank=True, null=True)
    id_Sc2=models.ForeignKey(SC_niv2, verbose_name=("Sc_niv2"), on_delete=models.CASCADE,default=None, blank=True, null=True)
    id_Sc3=models.ForeignKey(SC_niv3, verbose_name=("Sc_niv3"), on_delete=models.CASCADE,default=None, blank=True, null=True)
    id_point=models.ForeignKey(Point,verbose_name="Points",on_delete=models.CASCADE)
    reponse=models.BooleanField()
>>>>>>> 56a66dca5e36b1b5bd67d8340cb38a4c42b6b448

class Reponse(models.Model):
    id_reponse = models.TextField(primary_key=True)
    id_test = models.ForeignKey(Test, verbose_name="Tests", on_delete=models.CASCADE)
    id_qst = models.ForeignKey(Question_Generale, verbose_name="Questions_Generales", on_delete=models.CASCADE)
    id_norme = models.ForeignKey(Norme, verbose_name=("Normes"), on_delete=models.CASCADE)
    version = models.IntegerField()
    id_chap = models.ForeignKey(Chapitre, verbose_name="Chapitres", on_delete=models.CASCADE)
    id_Sc1 = models.ForeignKey(SC_niv1, verbose_name=("Sc_niv1"), on_delete=models.CASCADE)
    id_Sc2 = models.ForeignKey(SC_niv2, verbose_name=("Sc_niv2"), on_delete=models.CASCADE)
    id_Sc3 = models.ForeignKey(SC_niv3, verbose_name=("Sc_niv3"), on_delete=models.CASCADE)
    id_point = models.ForeignKey(Point, verbose_name="Points", on_delete=models.CASCADE)
    reponse = models.BooleanField()
