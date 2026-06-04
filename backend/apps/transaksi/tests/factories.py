import factory
from factory.django import DjangoModelFactory
from apps.transaksi.models import (
    PemesananBarang, PenerimaanBarang, NotaPembelian,
    BarangPindah, ProduksiBarang, PemakaianBarang,
    RejectStock, StockOpname, SesiOpname
)
from apps.master.tests.factories import (
    MasterStockFactory, MasterDepartemenFactory, 
    MasterVendorFactory, MasterSatuanFactory, MasterProduksiFactory
)
from django.contrib.auth import get_user_model

User = get_user_model()


class PemesananBarangFactory(DjangoModelFactory):
    class Meta:
        model = PemesananBarang
    
    stock = factory.SubFactory(MasterStockFactory)
    departemen = factory.SubFactory(MasterDepartemenFactory)
    vendor = factory.SubFactory(MasterVendorFactory)
    qty = factory.Faker('random_int', min=1, max=100)
    satuan = factory.SubFactory(MasterSatuanFactory)
    harga_estimasi = factory.Faker('random_int', min=10000, max=500000)
    status = 'draft'
    pic = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='pic@example.com', password='test123', nama='PIC'
    ))


class PenerimaanBarangFactory(DjangoModelFactory):
    class Meta:
        model = PenerimaanBarang
    
    pemesanan = factory.SubFactory(PemesananBarangFactory)
    stock = factory.SelfAttribute('pemesanan.stock')
    vendor = factory.SelfAttribute('pemesanan.vendor')
    departemen = factory.SelfAttribute('pemesanan.departemen')
    qty_besar = factory.Faker('random_int', min=1, max=10)
    qty_kecil = factory.Faker('random_int', min=1, max=10)
    harga_pembelian = factory.Faker('random_int', min=10000, max=500000)
    received_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='receiver@example.com', password='test123', nama='Receiver'
    ))


class NotaPembelianFactory(DjangoModelFactory):
    class Meta:
        model = NotaPembelian
    
    penerimaan = factory.SubFactory(PenerimaanBarangFactory)
    no_nota = factory.Sequence(lambda n: f'NOTA-{n}')
    harga_pembelian = factory.Faker('random_int', min=10000, max=500000)


class BarangPindahFactory(DjangoModelFactory):
    class Meta:
        model = BarangPindah
    
    stock = factory.SubFactory(MasterStockFactory)
    departemen_asal = factory.SubFactory(MasterDepartemenFactory)
    departemen_tujuan = factory.SubFactory(MasterDepartemenFactory)
    qty_request = factory.Faker('random_int', min=1, max=50)
    qty_konfirmasi = factory.Faker('random_int', min=1, max=50)
    satuan = factory.SubFactory(MasterSatuanFactory)
    status = 'draft'
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='requester@example.com', password='test123', nama='Requester'
    ))


class ProduksiBarangFactory(DjangoModelFactory):
    class Meta:
        model = ProduksiBarang
    
    produksi = factory.SubFactory(MasterProduksiFactory)
    departemen = factory.SubFactory(MasterDepartemenFactory)
    qty_produksi = factory.Faker('random_int', min=1, max=100)
    satuan = factory.SubFactory(MasterSatuanFactory)
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='production@example.com', password='test123', nama='Production'
    ))


class PemakaianBarangFactory(DjangoModelFactory):
    class Meta:
        model = PemakaianBarang
    
    stock = factory.SubFactory(MasterStockFactory)
    departemen = factory.SubFactory(MasterDepartemenFactory)
    qty = factory.Faker('random_int', min=1, max=50)
    satuan = factory.SubFactory(MasterSatuanFactory)
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='user@example.com', password='test123', nama='User'
    ))


class RejectStockFactory(DjangoModelFactory):
    class Meta:
        model = RejectStock
    
    stock = factory.SubFactory(MasterStockFactory)
    departemen = factory.SubFactory(MasterDepartemenFactory)
    qty = factory.Faker('random_int', min=1, max=10)
    satuan = factory.SubFactory(MasterSatuanFactory)
    catatan = factory.Faker('sentence', locale='id_ID')
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='reject@example.com', password='test123', nama='Reject'
    ))


class SesiOphameFactory(DjangoModelFactory):
    class Meta:
        model = SesiOpname
    
    departemen = factory.SubFactory(MasterDepartemenFactory)
    tipe = 'manual'
    status = 'aktif'
    dijadwalkan_oleh = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='admin@example.com', password='test123', nama='Admin'
    ))


class StockOpnameFactory(DjangoModelFactory):
    class Meta:
        model = StockOpname
    
    stock = factory.SubFactory(MasterStockFactory)
    departemen = factory.SubFactory(MasterDepartemenFactory)
    qty_sistem = factory.Faker('random_int', min=1, max=100)
    qty_opname = factory.Faker('random_int', min=1, max=100)
    satuan = factory.SubFactory(MasterSatuanFactory)
    sesi_opname = factory.SubFactory(SesiOphameFactory)
    created_by = factory.LazyAttribute(lambda o: User.objects.first() or User.objects.create_user(
        email='opname@example.com', password='test123', nama='Opname'
    ))
