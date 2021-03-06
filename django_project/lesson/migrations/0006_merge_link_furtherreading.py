# Generated by Django 2.2.13 on 2021-01-13 08:44

from django.db import migrations, models


def merge_link_to_text_field(apps, schema_editor):
    #  Fetch link data and merge it into text field
    FurtherReading = apps.get_model("lesson", "FurtherReading")
    old_data = FurtherReading.objects.all()
    for data in old_data:
        data.text = '%s <a href="%s">%s</a> ' % (
            data.text, data.link, data.link
        )
        if data.text_en:
            data.text_en = '%s <a href="%s">%s</a> ' % (
                data.text_en, data.link, data.link
            )
        if data.text_ind:
            data.text_ind = '%s <a href="%s">%s</a> ' % (
                data.text_ind, data.link, data.link
        )
        data.save(update_fields=['text', 'text_en', 'text_ind'])


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_auto_20210112_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furtherreading',
            name='text',
            field=models.TextField(help_text='Text of the further reading.'),
        ),
        migrations.AlterField(
            model_name='furtherreading',
            name='text_en',
            field=models.TextField(help_text='Text of the further reading.', null=True),
        ),
        migrations.AlterField(
            model_name='furtherreading',
            name='text_ind',
            field=models.TextField(help_text='Text of the further reading.', null=True),
        ),

        # Run custom function
        migrations.RunPython(merge_link_to_text_field),

        migrations.RemoveField(
            model_name='furtherreading',
            name='link',
        ),
    ]
