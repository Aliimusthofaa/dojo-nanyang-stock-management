import factory
from factory.django import DjangoModelFactory
from apps.keuangan.models import (
    BankUtama, PendapatanHarian, SubBank,
    PlottingKeuangan, MutasiSubBank, PengeluaranNonStock
)
from apps.master.tests.factories import MasterNonStockFactory
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class BankUtamaFactory(DjangoModelFactory):
    class Meta:
        model = BankUtama
    
    saldo_awal = 10000000.00
    saldo_saat_ini = 10000000.00
    updated_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='bank@example.com', password='test123', nama='Bank'
    ))


class PendapatanHarianFactory(DjangoModelFactory):
    class Meta:
        model = PendapatanHarian
    
    tanggal = factory.Faker('date_object')
    nominal = factory.Faker('random_int', min=100000, max=5000000)
    keterangan = factory.Faker('sentence', locale='id_ID')
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='revenue@example.com', password='test123', nama='Revenue'
    ))


class SubBankFactory(DjangoModelFactory):
    class Meta:
        model = SubBank
    
    nama = factory.Sequence(lambda n: f'SubBank {n}')
    saldo_saat_ini = factory.Faker('random_int', min=100000, max=5000000)


class PlottingKeuanganFactory(DjangoModelFactory):
    class Meta:
        model = PlottingKeuangan
    
    sub_bank = factory.SubFactory(SubBankFactory)
    nominal = factory.Faker('random_int', min=100000, max=2000000)
    tanggal = factory.Faker('date_object')
    keterangan = factory.Faker('sentence', locale='id_ID')
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='plotting@example.com', password='test123', nama='Plotting'
    ))


class MutasiSubBankFactory(DjangoModelFactory):
    class Meta:
        model = MutasiSubBank
    
    sub_bank = factory.SubFactory(SubBankFactory)
    nominal = factory.Faker('random_int', min=100000, max=1000000)
    tipe = factory.Faker('random_element', elements=['debit', 'kredit'])
    tanggal = factory.Faker('date_object')
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='mutasi@example.com', password='test123', nama='Mutasi'
    ))


class PengeluaranNonStockFactory(DjangoModelFactory):
    class Meta:
        model = PengeluaranNonStock
    
    non_stock = factory.SubFactory(MasterNonStockFactory)
    sub_bank = factory.SubFactory(SubBankFactory)
    nominal = factory.Faker('random_int', min=50000, max=1000000)
    tanggal = factory.Faker('date_object')
    keterangan = factory.Faker('sentence', locale='id_ID')
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='expense@example.com', password='test123', nama='Expense'
    ))
