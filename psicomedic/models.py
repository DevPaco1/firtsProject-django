from django.db import models

# Create your models here.
class Psychologist(models.Model):
    """psychologists model."""
    
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    birthdate =models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f"first_name-> {self.first_name}last_name-> {self.last_name}email-> {self.email}phone-> {self.phone}"


class Patient(models.Model):

    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    birthdate =models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    biography =models.TextField()
    address =models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"first_name-> {self.first_name} last_name-> {self.last_name} email-> {self.email} phone-> {self.phone}"

class Appointment(models.Model):

    appointment_date= models.DateTimeField()
    title= models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    patient_id = models.ForeignKey(Patient, models.PROTECT, related_name="Appointments")
    psychologist_id = models.ForeignKey(Psychologist,  models.PROTECT, related_name="Appointments")
    