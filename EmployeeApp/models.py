from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    departement = models.ForeignKey('Departement', on_delete=models.SET_NULL, null=True)  # ForeignKey ke Departement
    job_level = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50)
    employment_status = models.CharField(max_length=50)
    join_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    day_payment = models.DecimalField(max_digits=10, decimal_places=0)

# selanjutnya bagaimana cara menambahkan multi table
# di certification harus terdapat no, nama, number, date issued, verify period, description, action: unggah (jika belum ada), view/download (jika sudah ada)

class Departement(models.Model):
    departement_name = models.CharField(max_length=100)

    def __str__(self):
        return self.departement_name  # Tampilkan nama departemen

class Certification(models.Model):
    certification_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Relasi ke Employee
    name = models.CharField(max_length=100)  # Nama sertifikasi
    number = models.CharField(max_length=50)  # Nomor sertifikasi
    date_issued = models.DateField()  # Tanggal diterbitkan
    verify_period = models.CharField(max_length=50)  # Periode validitas
    description = models.TextField(null=True, blank=True)  # Deskripsi sertifikasi
    file = models.FileField(upload_to='certifications/', null=True, blank=True)  # File sertifikasi