# Generated by Django 3.1.6 on 2021-02-02 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubSubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.CharField(max_length=20)),
                ('porcentajeOferta', models.CharField(default='0', max_length=3, null=True)),
                ('oferta', models.BooleanField(default=False)),
                ('agotado', models.BooleanField(default=False)),
                ('imagen', models.ImageField(upload_to='Productos')),
                ('subsubcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a.subsubcategoria')),
            ],
        ),
    ]
