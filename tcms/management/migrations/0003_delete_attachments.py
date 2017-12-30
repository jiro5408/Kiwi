# Generated by Django 2.0 on 2017-12-30 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0011_delete_attachments'),
        ('testplans', '0005_delete_attachments'),
        ('management', '0002_add_initial_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testattachment',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='testattachmentdata',
            name='attachment',
        ),
        migrations.DeleteModel(
            name='TestAttachment',
        ),
        migrations.DeleteModel(
            name='TestAttachmentData',
        ),
    ]