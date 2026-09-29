from pricing_models.tier_rate import calculate_tier_rate
import pytest

# typical testing 
class TestTypical:
    @pytest.mark.parametrize("path, tier_one, tier_two, tier_three, fixed_fee, expected", [
        ("testing_data/boundary_testing_data_1.csv", 0.20, 0.00, 0.0, 10.0, 15.57), # 27.86kWh
        ("testing_data/boundary_testing_data_2.csv", 0.0, 0.30, 0.0, 10.0, 38.60), # 195.33kWh
        ("testing_data/typical_test_data.csv", 0.0, 0.0, 0.40, 10.0, 230.27), # 850.67kWh
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, 10.0, 310.27), 
    ])
    def test_typical(self, path, tier_one, tier_two, tier_three, fixed_fee, expected):
        assert expected == pytest.approx(calculate_tier_rate(path, tier_one, tier_two, tier_three, fixed_fee))

# boundary testing
class TestBoundary:
    @pytest.mark.parametrize("path, tier_one, tier_two, tier_three, fixed_fee, expected", [
        ("testing_data/boundary_testing_data_3.csv", 0.20, 0.30, 0.40, 10.0, 10.0),  # 0kWh
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, 0.0, 300.27), 
        ("testing_data/typical_test_data.csv", 0.0, 0.30, 0.40, 0.0, 280.27),
        ("testing_data/typical_test_data.csv", 0.20, 0.00, 0.40, 0.0, 240.27),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.0, 0.0, 80),

        ("testing_data/boundary_testing_data_13.csv", 0.20, 0.30, 0.40, 0.0, 19.87), #99.36kWh
        ("testing_data/boundary_testing_data_14.csv", 0.20, 0.30, 0.40, 0.0, 20.28), #100.93kWh
        ("testing_data/boundary_testing_data_15.csv", 0.20, 0.30, 0.40, 0.0, 79.77), #299.22kWh
        ("testing_data/boundary_testing_data_16.csv", 0.20, 0.30, 0.40, 0.0, 80.80), #301.99kWh
    ])

    def test_boundary(self, path, tier_one, tier_two, tier_three, fixed_fee, expected):
        assert expected == pytest.approx(calculate_tier_rate(path, tier_one, tier_two, tier_three, fixed_fee))

#invaild testing
class TestValueErrors:
    @pytest.mark.parametrize("path, tier_one, tier_two, tier_three, fixed_fee", [
        ("testing_data/invalid_testing_data_1.csv", 0.20, 0.30, 0.40, 10.0), #-15kWh        
        ("testing_data/typical_test_data.csv", -1.0, 0.30, 0.40, 0.0), 
        ("testing_data/typical_test_data.csv", 0.20, -2.0, 0.40, 0.0),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, -3.0, 0.0),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, -15.0),
    ])
    def test_bad_values(self, path, tier_one, tier_two, tier_three, fixed_fee):
        with pytest.raises(ValueError):
            calculate_tier_rate(path, tier_one, tier_two, tier_three, fixed_fee)

class TestTypeErrors:
    @pytest.mark.parametrize("path, tier_one, tier_two, tier_three, fixed_fee", [
        ("testing_data/typical_test_data.csv", True, 0.30, 0.40, 10.0),
        ("testing_data/typical_test_data.csv", 0.20, "False", 0.40, -15.0),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, False, -15.0),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, "True"),
        (True, 0.20, 0.30, 0.40, 10.0), 
        (1234, 0.20, 0.30, 0.40, 10.0),
        ("testing_data/typical_test_data.csv", None, 0.30, 0.40, 10.0),
        ("testing_data/typical_test_data.csv", 0.20, None, 0.40, -15.0),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, None, -15.0),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, None),
        (None, 0.20, 0.30, 0.40, 10.0),
    ])
    def test_bad_types(self, path, tier_one, tier_two, tier_three, fixed_fee):
        with pytest.raises(TypeError):
            calculate_tier_rate(path, tier_one, tier_two, tier_three, fixed_fee)
