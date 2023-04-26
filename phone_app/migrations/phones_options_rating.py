# Generated by Django 4.2 on 2023-04-25 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0002_alter_phones_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phones',
            options={'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны'},
        ),
        migrations.CreateModel(
            name='RatingPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500, null=True, verbose_name='Комментарий')),
                ('rate', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], null=True, verbose_name='Оценка')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('choice_film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='phone_app.phones')),
            ],
        ),
    ]