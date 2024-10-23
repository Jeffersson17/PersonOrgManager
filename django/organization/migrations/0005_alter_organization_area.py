# Generated by Django 5.1.2 on 2024-10-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_alter_organization_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='area',
            field=models.CharField(choices=[('SD', 'Saúde'), ('TI', 'Tecnologia da Informação'), ('SG', 'Serviços Gerais'), ('FC', 'Financeiro'), ('VD', 'Vendas'), ('JD', 'Jurídico'), ('PD', 'Pesquisa e Desenvolvimento'), ('AD', 'Administração'), ('MK', 'Marketing'), ('RH', 'Recursos Humanos'), ('CI', 'Comunicação Interna'), ('DS', 'Design'), ('EC', 'E-commerce'), ('PA', 'Planejamento e Análise de Negócios')], max_length=2),
        ),
    ]
