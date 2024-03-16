from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_tag_tag_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name_plural': 'Тематика статьи'},
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='!!!'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=30, verbose_name='Раздел'),
        ),
    ]