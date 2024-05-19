# Generated by Ginger 5.1.dev20240426130717 on 2024-04-26 14:15

from ginger.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tenant2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("name2", models.CharField(max_length=200, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("expiry_date", models.DateField(blank=True, null=True)),
            ],
            options={
                "db_table": "shared_tenant2",
            },
        ),
    ]
