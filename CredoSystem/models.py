from django.contrib.auth.models import AbstractBaseUser, AbstractUser, Group
from django.db import models


class PrivilegeClass(models.Model):
    priv_class_name = models.CharField(max_length=32, blank=False)
    priv_class_desc = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(
        Group, through='PrivilegeClassGroup',
        through_fields=('priv_class', 'group'),
        related_name='associated_groups'
    )

    def __str__(self):
        return "{}".format(self.priv_class_name)

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "privilege_class"
        verbose_name = 'Privilege Class'
        verbose_name_plural = 'Privilege Classes'


class PrivilegeClassGroup(models.Model):
    priv_class = models.ForeignKey(PrivilegeClass)
    group = models.ForeignKey(Group)

    def __str__(self):
        return "{} - {}".format(
            self.priv_class.priv_class_name,
            self.group.name
        )

    class Meta:
        db_table = "privilege_class_group"
        verbose_name = 'Privilege Class Group'
        verbose_name_plural = 'Privilege Class Groups'


class User(AbstractUser):
    priv_class_id = models.ForeignKey(PrivilegeClass, db_column='priv_class_id', null=True, blank=True, default=None)

    class Meta:
        db_table = "auth_user"
