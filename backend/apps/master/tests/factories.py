import factory
from factory.django import DjangoModelFactory
from apps.master.models import (
    MasterStock, MasterSatuan, MasterVendor, 
    MasterDepartemen, MasterProduksi, StockParLevel, ProduksiParLevel
)


class MasterSatuanFactory(DjangoModelFactory):
    class Meta:
        model = MasterSatuan
    
    nama_satuan = factory.Sequence(lambda n: f'Satuan {n}')


class MasterVendorFactory(DjangoModelFactory):
    class Meta:
        model = MasterVendor
    
    nama_vendor = factory.Faker('company', locale='id_ID')
    alamat = factory.Faker('address', locale='id_ID')
    kontak = factory.Faker('phone_number', locale='id_ID')


class MasterDepartemenFactory(DjangoModelFactory):
    class Meta:
        model = MasterDepartemen
    
    nama_departemen = factory.Sequence(lambda n: f'Departemen {n}')
    tipe = factory.Faker('random_element', elements=['gudang', 'operasional'])


class MasterStockFactory(DjangoModelFactory):
    class Meta:
        model = MasterStock
    
    nama_stock = factory.Faker('word', locale='id_ID')
    merk = factory.Faker('company', locale='id_ID')
    satuan_besar = factory.SubFactory(MasterSatuanFactory)
    satuan_kecil = factory.SubFactory(MasterSatuanFactory)
    isi_per_satuan_besar = factory.Faker('random_int', min=1, max=10)
    harga_pembelian_default = factory.Faker('random_int', min=10000, max=500000)
    is_active = True


class MasterProduksiFactory(DjangoModelFactory):
    class Meta:
        model = MasterProduksi
    
    nama_produksi = factory.Faker('word', locale='id_ID')
    satuan = factory.SubFactory(MasterSatuanFactory)
    harga_jual = factory.Faker('random_int', min=10000, max=500000)
    is_active = True


class StockParLevelFactory(DjangoModelFactory):
    class Meta:
        model = StockParLevel
    
    stock = factory.SubFactory(MasterStockFactory)
    departemen = factory.SubFactory(MasterDepartemenFactory)
    par_level = factory.Faker('random_int', min=1, max=100)
    satuan = factory.SubFactory(MasterSatuanFactory)


class ProduksiParLevelFactory(DjangoModelFactory):
    class Meta:
        model = ProduksiParLevel
    
    produksi = factory.SubFactory(MasterProduksiFactory)
    departemen = factory.SubFactory(MasterDepartemenFactory)
    par_level = factory.Faker('random_int', min=1, max=100)
    satuan = factory.SubFactory(MasterSatuanFactory)
