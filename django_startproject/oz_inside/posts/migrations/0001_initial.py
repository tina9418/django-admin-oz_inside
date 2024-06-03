import django.db.models.deletion
from django.conf import Settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    OPERATIONS = [
        MIGRATIONS.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=djanngo.db.models.deletion.CASCADE,related_name='posts', to=settings.AUTH_USER_MODEL)),
            ]
        )
    ]