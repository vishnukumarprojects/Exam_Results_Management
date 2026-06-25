from django.db import models

# Create your models here.
class twelveth_subjects_table(models.Model):
    reg_no=models.CharField(max_length=6)
    sub1=models.CharField(max_length=30)
    sub2=models.CharField(max_length=30)
    sub3=models.CharField(max_length=30)
    sub4=models.CharField(max_length=30)
    sub5=models.CharField(max_length=30)
    sub6=models.CharField(max_length=30)

class twelveth_internal_table(models.Model):
    reg_no=models.CharField(max_length=6)
    internal1=models.CharField(max_length=3)
    internal2=models.CharField(max_length=3)
    internal3=models.CharField(max_length=3)
    internal4=models.CharField(max_length=3)
    internal5=models.CharField(max_length=3)
    internal6=models.CharField(max_length=3)
    
class twelveth_theory_table(models.Model):
    reg_no=models.CharField(max_length=6)
    theory1=models.CharField(max_length=3)
    theory2=models.CharField(max_length=3)
    theory3=models.CharField(max_length=3)
    theory4=models.CharField(max_length=3)
    theory5=models.CharField(max_length=3)
    theory6=models.CharField(max_length=3)

class twelveth_practical_table(models.Model):
    reg_no=models.CharField(max_length=6)
    practical1=models.CharField(max_length=3)
    practical2=models.CharField(max_length=3)
    practical3=models.CharField(max_length=3)
class twelveth_name_regno_table(models.Model):
    reg_no=models.CharField(max_length=6)
    names=models.CharField(max_length=30)
    

# -----------------------------------------------------------------------



class eleventh_subjects_table(models.Model):
    reg_no=models.CharField(max_length=6)
    sub1=models.CharField(max_length=30)
    sub2=models.CharField(max_length=30)
    sub3=models.CharField(max_length=30)
    sub4=models.CharField(max_length=30)
    sub5=models.CharField(max_length=30)
    sub6=models.CharField(max_length=30)

class eleventh_internal_table(models.Model):
    reg_no=models.CharField(max_length=6)
    internal1=models.CharField(max_length=3)
    internal2=models.CharField(max_length=3)
    internal3=models.CharField(max_length=3)
    internal4=models.CharField(max_length=3)
    internal5=models.CharField(max_length=3)
    internal6=models.CharField(max_length=3)
    
class eleventh_theory_table(models.Model):
    reg_no=models.CharField(max_length=6)
    theory1=models.CharField(max_length=3)
    theory2=models.CharField(max_length=3)
    theory3=models.CharField(max_length=3)
    theory4=models.CharField(max_length=3)
    theory5=models.CharField(max_length=3)
    theory6=models.CharField(max_length=3)

class eleventh_practical_table(models.Model):
    reg_no=models.CharField(max_length=6)
    practical1=models.CharField(max_length=3)
    practical2=models.CharField(max_length=3)
    practical3=models.CharField(max_length=3)
class eleventh_name_regno_table(models.Model):
    reg_no=models.CharField(max_length=6)
    names=models.CharField(max_length=30)






    # -----------------------------------------------------------------



    
class tenth_subjects_table(models.Model):
    reg_no=models.CharField(max_length=6)
    sub1=models.CharField(max_length=30)
    sub2=models.CharField(max_length=30)
    sub3=models.CharField(max_length=30)
    sub4=models.CharField(max_length=30)
    sub5=models.CharField(max_length=30)


class tenth_internal_table(models.Model):
    reg_no=models.CharField(max_length=6)
    internal1=models.CharField(max_length=3)
    internal2=models.CharField(max_length=3)
    internal3=models.CharField(max_length=3)
    internal4=models.CharField(max_length=3)
    internal5=models.CharField(max_length=3)

    
class tenth_theory_table(models.Model):
    reg_no=models.CharField(max_length=6)
    theory1=models.CharField(max_length=3)
    theory2=models.CharField(max_length=3)
    theory3=models.CharField(max_length=3)
    theory4=models.CharField(max_length=3)
    theory5=models.CharField(max_length=3)

class tenth_practical_table(models.Model):
    reg_no=models.CharField(max_length=6)
    practical1=models.CharField(max_length=3)
    
class tenth_name_regno_table(models.Model):
    reg_no=models.CharField(max_length=6)
    names=models.CharField(max_length=30)