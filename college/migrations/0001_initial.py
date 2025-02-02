# Generated by Django 2.1.7 on 2024-07-06 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliatedInstitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('office_phone', models.CharField(blank=True, max_length=20)),
                ('office_email', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Organization / Affiliated Institutes',
            },
        ),
        migrations.CreateModel(
            name='AssignSubjectTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('Third', 'Third'), ('First', 'First'), ('Fourth', 'Fourth'), ('Second', 'Second')], max_length=40)),
                ('subject_teacher_teaching_experience_years', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Subject Teacher Assignment',
            },
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_students', models.IntegerField(default='20')),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(blank=True, choices=[('Prof Dr.', 'Prof Dr'), ('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms'), ('Dr.', 'Dr')], max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('mobile_phone', models.CharField(blank=True, max_length=20)),
                ('home_phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('upper_degree', models.CharField(choices=[('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('PhD', 'PhD')], default='MSc', max_length=30)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='college.AffiliatedInstitute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(blank=True, choices=[('Third', 'Third'), ('First', 'First'), ('Fourth', 'Fourth'), ('Second', 'Second')], max_length=40, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('elective', models.BooleanField(default=False)),
                ('subject_code', models.CharField(blank=True, default=' ', max_length=40)),
                ('credit', models.IntegerField(default='4')),
                ('internal_marks', models.IntegerField(default='40')),
                ('external_marks', models.IntegerField(default='60')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(blank=True, choices=[('Prof Dr.', 'Prof Dr'), ('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms'), ('Dr.', 'Dr')], max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('mobile_phone', models.CharField(blank=True, max_length=20)),
                ('home_phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('upper_degree', models.CharField(choices=[('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('PhD', 'PhD')], default='MSc', max_length=30)),
                ('teacher_id', models.CharField(blank=True, max_length=20)),
                ('aff_type', models.CharField(choices=[('Visiting', 'Visiting'), ('Contract', 'Contract'), ('Permanent', 'Permanent')], default='Permanent', max_length=30)),
                ('started_teaching', models.CharField(blank=True, default='2081', max_length=4, verbose_name='started teaching in BS')),
                ('affiliated_institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='college.AffiliatedInstitute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='2081', max_length=40, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='programme',
            name='coordinator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='college.Teacher'),
        ),
        migrations.AddField(
            model_name='expert',
            name='topic',
            field=models.ManyToManyField(to='college.Topic'),
        ),
        migrations.AddField(
            model_name='batch',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Programme'),
        ),
        migrations.AddField(
            model_name='batch',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Year'),
        ),
        migrations.AddField(
            model_name='assignsubjectteacher',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Batch'),
        ),
        migrations.AddField(
            model_name='assignsubjectteacher',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Subject'),
        ),
        migrations.AddField(
            model_name='assignsubjectteacher',
            name='subject_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Teacher'),
        ),
        migrations.AddField(
            model_name='assignsubjectteacher',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Year'),
        ),
        migrations.AlterUniqueTogether(
            name='teacher',
            unique_together={('first_name', 'last_name', 'mobile_phone', 'upper_degree')},
        ),
        migrations.AlterUniqueTogether(
            name='expert',
            unique_together={('first_name', 'last_name', 'mobile_phone', 'upper_degree')},
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together={('year', 'programme')},
        ),
        migrations.AlterUniqueTogether(
            name='assignsubjectteacher',
            unique_together={('year', 'batch', 'subject', 'subject_teacher', 'semester')},
        ),
    ]
