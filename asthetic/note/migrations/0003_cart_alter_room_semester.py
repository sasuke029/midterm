# Generated by Django 4.2.3 on 2023-07-12 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_department_semester_room_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subjects', models.CharField(max_length=100)),
                ('Rate', models.PositiveIntegerField()),
                ('Quantity', models.PositiveIntegerField()),
                ('Total_Price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.semester'),
        ),
    ]
