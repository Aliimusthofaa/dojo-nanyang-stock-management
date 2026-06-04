import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model

User = get_user_model()


class MasterPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    nama = factory.Faker('name', locale='id_ID')
    password = factory.PostGenerationMethodCall('set_password', 'TestPassword123')
    role = factory.Faker('random_element', elements=['owner', 'admin', 'admin_office', 'gudang', 'produksi', 'admin_departemen'])
    is_active = True


class OwnerFactory(MasterPegawaiFactory):
    role = 'owner'


class AdminFactory(MasterPegawaiFactory):
    role = 'admin'


class AdminOfficeFactory(MasterPegawaiFactory):
    role = 'admin_office'


class GudangFactory(MasterPegawaiFactory):
    role = 'gudang'


class ProduksiFactory(MasterPegawaiFactory):
    role = 'produksi'


class AdminDepartemenFactory(MasterPegawaiFactory):
    role = 'admin_departemen'
