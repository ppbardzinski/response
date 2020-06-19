from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [("response", "0016_actions_auto_created_date")]

    operations = [
        migrations.AddField(
            model_name="incident",
            name="environment",
            field=models.TextField(blank=True, help_text="What's the environment?", null=True),
        )
    ]