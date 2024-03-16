from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]
