from django.db import models

class cs_dep(models.Model):
    stuname = models.CharField(max_length=100)
    regno = models.CharField(max_length=100)
    stuclass = models.CharField(max_length=100)
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    sub4 = models.IntegerField()
    sub5 = models.IntegerField()

    # Method to calculate total marks
    def tot(self):
        return self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5

    # Method to calculate percentage
    def per(self):
        total_marks = self.tot()
        return (total_marks / 500) * 100  # Assuming each subject is out of 100, total is 500

    # Method to calculate pass or fail
    def psfil(self):
        return "pass" if self.tot() >= 250 else "fail"

    # Method to calculate result based on the total
    def res(self):
        total_marks = self.tot()
        if total_marks >= 450:
            return "very good"
        elif total_marks >= 400:
            return "good"
        elif total_marks >= 350:
            return "average"
        else:
            return "very bad"

class csdep_sem2(models.Model):
    stuname = models.CharField(max_length=100)
    regno = models.CharField(max_length=100)
    stuclass = models.CharField(max_length=100)
    sub6 = models.IntegerField()
    sub7 = models.IntegerField()
    sub8 = models.IntegerField()
    sub9 = models.IntegerField()
    sub10 = models.IntegerField()

    def tot(self):
        return self.sub6 + self.sub7 + self.sub8 + self.sub9 + self.sub10
    def per(self):
        total_marks = self.tot()
        return (total_marks / 500) * 100  # Assuming each subject is out of 100, total is 500
    def psfil(self):
        return "pass" if self.tot() >= 250 else "fail"
    def res(self):
        total_marks = self.tot()
        if total_marks >= 450:
            return "very good"
        elif total_marks >= 400:
            return "good"
        elif total_marks >= 350:
            return "average"
        else:
            return "very bad"

class csdep_sem3(models.Model):
    stuname=models.CharField(max_length=100)
    regno = models.CharField(max_length=100)
    stuclass = models.CharField(max_length=100)
    sub11=models.IntegerField()
    sub12 = models.IntegerField()
    sub13 = models.IntegerField()
    sub14 = models.IntegerField()
    sub15 = models.IntegerField()

    def tot(self):
        return self.sub11 + self.sub12 + self.sub13 + self.sub14 + self.sub15

    def per(self):
        total_marks = self.tot()
        return (total_marks / 500) * 100

    def psfil(self):
        return "pass" if self.tot() >= 250 else "fail"

    def res(self):
        total_marks = self.tot()
        if total_marks >= 450:
            return "very good"
        elif total_marks >= 400:
            return "good"
        elif total_marks >= 350:
            return "average"
        else:
            return "very bad"

class csdep_sem4(models.Model):
    stuname=models.CharField(max_length=100)
    regno = models.CharField(max_length=100)
    stuclass = models.CharField(max_length=100)
    sub16=models.IntegerField()
    sub17 = models.IntegerField()
    sub18 = models.IntegerField()
    sub19 = models.IntegerField()
    sub20 = models.IntegerField()

    def tot(self):
        return self.sub16 + self.sub17 + self.sub18 + self.sub19 + self.sub20

    def per(self):
        total_marks = self.tot()
        return (total_marks / 500) * 100

    def psfil(self):
        return "pass" if self.tot() >= 250 else "fail"

    def res(self):
        total_marks = self.tot()
        if total_marks >= 450:
            return "very good"
        elif total_marks >= 400:
            return "good"
        elif total_marks >= 350:
            return "average"
        else:
            return "very bad"

class csdep_sem5(models.Model):
    stuname = models.CharField(max_length=100)
    regno = models.CharField(max_length=100)
    stuclass = models.CharField(max_length=100)
    sub21 = models.IntegerField()
    sub22 = models.IntegerField()
    sub23 = models.IntegerField()
    sub24 = models.IntegerField()
    sub25 = models.IntegerField()

    def tot(self):
        return self.sub21 + self.sub22 + self.sub23 + self.sub24 + self.sub25

    def per(self):
        total_marks = self.tot()
        return (total_marks / 500) * 100

    def psfil(self):
        return "pass" if self.tot() >= 250 else "fail"

    def res(self):
        total_marks = self.tot()
        if total_marks >= 450:
            return "very good"
        elif total_marks >= 400:
            return "good"
        elif total_marks >= 350:
            return "average"
        else:
            return "very bad"

class csdep_sem6(models.Model):
    stuname = models.CharField(max_length=100)
    regno = models.CharField(max_length=100)
    stuclass = models.CharField(max_length=100)
    sub26 = models.IntegerField()
    sub27 = models.IntegerField()
    sub28 = models.IntegerField()
    sub29 = models.IntegerField()
    sub30 = models.IntegerField()

    def tot(self):
        return self.sub26 + self.sub27 + self.sub28 + self.sub29 + self.sub30

    def per(self):
        total_marks = self.tot()
        return (total_marks / 500) * 100

    def psfil(self):
        return "pass" if self.tot() >= 250 else "fail"

    def res(self):
        total_marks = self.tot()
        if total_marks >= 450:
            return "very good"
        elif total_marks >= 400:
            return "good"
        elif total_marks >= 350:
            return "average"
        else:
            return "very bad"

