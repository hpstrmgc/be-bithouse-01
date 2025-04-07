from django.db import migrations

def migrate_departement_data(apps, schema_editor):
    Employee = apps.get_model('EmployeeApp', 'Employee')
    Departement = apps.get_model('EmployeeApp', 'Departement')

    for employee in Employee.objects.all():
        if employee.departement_old:  # Jika ada data lama
            try:
                # Cari departemen berdasarkan nama
                departement = Departement.objects.get(departement_name=employee.departement_old)
                # Set relasi ForeignKey
                employee.departement = departement
                employee.save()
            except Departement.DoesNotExist:
                print(f"Departement '{employee.departement_old}' tidak ditemukan.")

class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),  # Pastikan ini sesuai dengan migrasi awal Anda
    ]

    operations = [
        migrations.RunPython(migrate_departement_data),
    ]