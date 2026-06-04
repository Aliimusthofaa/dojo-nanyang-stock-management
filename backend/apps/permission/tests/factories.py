import factory
from factory.django import DjangoModelFactory
from apps.permission.models import MasterPermission, RolePermission


class MasterPermissionFactory(DjangoModelFactory):
    class Meta:
        model = MasterPermission
    
    kode_permission = factory.Sequence(lambda n: f'PERM_{n}')
    nama = factory.Faker('word', locale='id_ID')
    deskripsi = factory.Faker('sentence', locale='id_ID')
    modul = factory.Faker('random_element', elements=['stock', 'finance', 'production', 'report'])


class RolePermissionFactory(DjangoModelFactory):
    class Meta:
        model = RolePermission
    
    role = factory.Faker('random_element', elements=['owner', 'admin', 'admin_office', 'gudang', 'produksi', 'admin_departemen'])
    permission = factory.SubFactory(MasterPermissionFactory)
