# Generated by Django 2.0.1 on 2018-02-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_auto_20180207_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='files/')),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='file', to='meeting.Meeting')),
            ],
        ),
    ]