import os
import django
from django.conf import settings
from django.test.utils import get_runner
from faker import Faker

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

pytest_plugins = [
    'apps.master.tests.factories',
    'apps.auth.tests.factories',
    'apps.permission.tests.factories',
    'apps.transaksi.tests.factories',
    'apps.keuangan.tests.factories',
]

fake = Faker('id_ID')

# ============================================================================
# FIXTURES - Database & Authentication
# ============================================================================

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.fixture
def db_setup(db):
    """Database setup fixture"""
    return db


@pytest.fixture
def api_client():
    """API client fixture"""
    return APIClient()


@pytest.fixture
def authenticated_user(db):
    """Create and return an authenticated test user"""
    user = User.objects.create_user(
        email='test@example.com',
        password='TestPassword123',
        nama='Test User',
        role='admin'
    )
    return user


@pytest.fixture
def authenticated_client(api_client, authenticated_user):
    """API client with authenticated user"""
    refresh = RefreshToken.for_user(authenticated_user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return api_client


@pytest.fixture
def access_token(authenticated_user):
    """Generate access token for authenticated user"""
    refresh = RefreshToken.for_user(authenticated_user)
    return str(refresh.access_token)


@pytest.fixture
def owner_user(db):
    """Create owner user"""
    user = User.objects.create_user(
        email='owner@example.com',
        password='OwnerPassword123',
        nama='Owner User',
        role='owner'
    )
    return user


@pytest.fixture
def admin_user(db):
    """Create admin user"""
    user = User.objects.create_user(
        email='admin@example.com',
        password='AdminPassword123',
        nama='Admin User',
        role='admin'
    )
    return user


@pytest.fixture
def gudang_user(db):
    """Create gudang (warehouse) user"""
    user = User.objects.create_user(
        email='gudang@example.com',
        password='GudangPassword123',
        nama='Gudang User',
        role='gudang'
    )
    return user


@pytest.fixture
def produksi_user(db):
    """Create produksi (production) user"""
    user = User.objects.create_user(
        email='produksi@example.com',
        password='ProduksiPassword123',
        nama='Produksi User',
        role='produksi'
    )
    return user


# ============================================================================
# FIXTURES - Master Data
# ============================================================================

from apps.master.models import MasterDepartemen, MasterSatuan, MasterVendor


@pytest.fixture
def departemen_gudang_luar(db):
    """Create 'Gudang Luar' department"""
    return MasterDepartemen.objects.create(
        nama_departemen='Gudang Luar',
        tipe='gudang'
    )


@pytest.fixture
def departemen_bar_luar(db):
    """Create 'Bar Luar' department"""
    return MasterDepartemen.objects.create(
        nama_departemen='Bar Luar',
        tipe='gudang'
    )


@pytest.fixture
def departemen_bar(db):
    """Create 'Bar' department"""
    return MasterDepartemen.objects.create(
        nama_departemen='Bar',
        tipe='operasional'
    )


@pytest.fixture
def departemen_kitchen(db):
    """Create 'Kitchen' department"""
    return MasterDepartemen.objects.create(
        nama_departemen='Kitchen',
        tipe='operasional'
    )


@pytest.fixture
def departemen_central_kitchen(db):
    """Create 'Central Kitchen' department"""
    return MasterDepartemen.objects.create(
        nama_departemen='Central Kitchen',
        tipe='operasional'
    )


@pytest.fixture
def satuan_kg(db):
    """Create 'KG' satuan"""
    return MasterSatuan.objects.create(nama_satuan='KG')


@pytest.fixture
def satuan_gram(db):
    """Create 'Gram' satuan"""
    return MasterSatuan.objects.create(nama_satuan='Gram')


@pytest.fixture
def satuan_liter(db):
    """Create 'Liter' satuan"""
    return MasterSatuan.objects.create(nama_satuan='Liter')


@pytest.fixture
def satuan_ml(db):
    """Create 'ML' satuan"""
    return MasterSatuan.objects.create(nama_satuan='ML')


@pytest.fixture
def vendor_pt_adi(db):
    """Create 'PT ADI' vendor"""
    return MasterVendor.objects.create(
        nama_vendor='PT ADI Sentosa',
        alamat='Jl. Industri No. 123, Jakarta',
        kontak='021-1234567'
    )


@pytest.fixture
def vendor_cv_mitra(db):
    """Create 'CV Mitra' vendor"""
    return MasterVendor.objects.create(
        nama_vendor='CV Mitra Jaya',
        alamat='Jl. Perdagangan No. 456, Surabaya',
        kontak='031-7654321'
    )


# ============================================================================
# FIXTURES - Common Test Data
# ============================================================================

@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {
        'email': fake.email(),
        'password': 'TestPassword123',
        'nama': fake.name(),
        'role': 'gudang'
    }


@pytest.fixture
def sample_stock_data():
    """Sample stock data for testing"""
    return {
        'nama_stock': 'Ajinomoto',
        'merk': 'Ajinomoto Official',
        'harga_pembelian_default': 85000.00,
        'is_active': True
    }


@pytest.fixture
def sample_departemen_data():
    """Sample department data"""
    return {
        'nama_departemen': 'Test Department',
        'tipe': 'operasional'
    }


# ============================================================================
# MARKERS - Test Categories
# ============================================================================

def pytest_configure(config):
    """Register pytest markers"""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "e2e: mark test as an end-to-end test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow"
    )
    config.addinivalue_line(
        "markers", "api: mark test as API endpoint test"
    )
    config.addinivalue_line(
        "markers", "auth: mark test as authentication test"
    )
    config.addinivalue_line(
        "markers", "permission: mark test as permission test"
    )
    config.addinivalue_line(
        "markers", "finance: mark test as finance workflow test"
    )
    config.addinivalue_line(
        "markers", "stock: mark test as stock workflow test"
    )
