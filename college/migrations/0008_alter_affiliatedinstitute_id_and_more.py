# Generated by Django 5.0.7 on 2025-01-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_auto_20240718_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliatedinstitute',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='assignsubjectteacher',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='assignsubjectteacher',
            name='semester',
            field=models.CharField(choices=[('Fourth', 'Fourth'), ('First', 'First'), ('Third', 'Third'), ('Second', 'Second')], max_length=40),
        ),
        migrations.AlterField(
            model_name='batch',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr'), ('Mr.', 'Mr'), ('Prof Dr.', 'Prof Dr'), ('Ms.', 'Ms'), ('Mrs.', 'Mrs')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='upper_degree',
            field=models.CharField(choices=[('PhD', 'PhD'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors')], default='MSc', max_length=30),
        ),
        migrations.AlterField(
            model_name='programme',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(blank=True, choices=[('Fourth', 'Fourth'), ('First', 'First'), ('Third', 'Third'), ('Second', 'Second')], max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='aff_type',
            field=models.CharField(choices=[('Permanent', 'Permanent'), ('Visiting', 'Visiting'), ('Contract', 'Contract')], default='Permanent', max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr'), ('Mr.', 'Mr'), ('Prof Dr.', 'Prof Dr'), ('Ms.', 'Ms'), ('Mrs.', 'Mrs')], max_length=40),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='started_teaching',
            field=models.CharField(blank=True, default='2082', max_length=4, verbose_name='started teaching in BS'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='upper_degree',
            field=models.CharField(choices=[('PhD', 'PhD'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors')], default='MSc', max_length=30),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='year',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='year',
            name='name',
            field=models.CharField(default='2082', max_length=40, unique=True),
        ),
    ]
