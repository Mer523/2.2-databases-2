from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teachers',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.teacher', verbose_name='Учителя'),
        ),
    ]
