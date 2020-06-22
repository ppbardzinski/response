from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [("response", "0017_incident_environment")]

    operations = [
        migrations.AddField(
            model_name="incident",
            name="incident_platform",
            field=models.TextField(blank=True, null=True),
        )
    ]