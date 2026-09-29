import pytest
from pricing_models.flat_rate import calculate_flat_rate

# typical testing 
class TestTypicalFlatRate:
    @pytest.mark.parametrize("path, fixed_rate, fixed_fee, expected", [
        ("testing_data/typical_test_data.csv", 1.0, 10.0, 860.67), # 850.67kWh
        ("testing_data/typical_test_data.csv", 0.25, 10.0, 222.67),
        ("testing_data/typical_test_data.csv", 0.25, 25.0, 237.67),
    ])
    def test_typical(self, path, fixed_rate, fixed_fee, expected):
        assert calculate_flat_rate(path, fixed_rate, fixed_fee) == pytest.approx(expected)

# boundary testing
class TestBoundaryFlatRate:
    @pytest.mark.parametrize("path, fixed_rate, fixed_fee, expected", [
        ("testing_data/boundary_testing_data_3.csv", 1.0, 10.0, 10.00),
        ("testing_data/typical_test_data.csv", 0.0, 10.0, 10),
        ("testing_data/typical_test_data.csv", 1.0, 0.0, 850.67),
    ])
    def test_boundary_values(self, path, fixed_rate, fixed_fee, expected):
        assert calculate_flat_rate(path, fixed_rate, fixed_fee) == pytest.approx(expected)

# invaild testing
class TestValueErrorFlatRate:
    @pytest.mark.parametrize("path, fixed_rate, fixed_fee", [
        ("testing_data/invalid_testing_data_1.csv", 0.25, 10.0), #-15kWh
        ("testing_data/typical_test_data.csv", -1.0, 0.30), 
        ("testing_data/typical_test_data.csv", 0.20, -15.0),
        ])
    
    def test_bad_values(self, path, fixed_rate, fixed_fee):
        with pytest.raises(ValueError):
            calculate_flat_rate(path, fixed_rate, fixed_fee)


class TestTypeErrorFlatRate:
    #invaild testing
    @pytest.mark.parametrize("path, fixed_rate, fixed_fee", [
        ("testing_data/typical_test_data.csv", True, 0.30),
        ("testing_data/typical_test_data.csv", 0.30, "True"),
        (True, 0.20, 0.30), 
        (1234, 0.20, 0.30),
        ("testing_data/typical_test_data.csv", None, 0.30),
        ("testing_data/typical_test_data.csv", 0.20, None),
        (None, 0.20, 0.30),
        ])
    
    def test_type_errors(self, path, fixed_rate, fixed_fee):
        with pytest.raises(TypeError):
            calculate_flat_rate(path, fixed_rate, fixed_fee)


