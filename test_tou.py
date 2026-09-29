import pytest
from pricing_models.tou_rate import calculate_tou_rate

# typical testing
class TestTypical:
    @pytest.mark.parametrize("path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate, expected", [
        ("testing_data/typical_test_data.csv", 10.0, 0.40, 0.0, 0.0, 116.87), # 850.67kWh 
        ("testing_data/typical_test_data.csv", 10.0, 0.0, 0.15, 0.0, 37.87), 
        ("testing_data/typical_test_data.csv", 10.0, 0.0, 0.0, 0.25, 109.43),
        ("testing_data/typical_test_data.csv", 15.0, 0.40, 0.15, 0.25, 249.16), 
    ])
    def test_typical(self, path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate, expected):
        assert expected == pytest.approx(calculate_tou_rate(path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate))


# boundary testing
class TestBoundary:
    @pytest.mark.parametrize("path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate, expected", [
        ("testing_data/boundary_testing_data_6.csv", 0.0, 0.40, 0.15, 0.25, 0.41), #1.63 17:59:59
        ("testing_data/boundary_testing_data_7.csv", 0.0, 0.40, 0.15, 0.25, 0.71), #1.77 18:00:00
        ("testing_data/boundary_testing_data_8.csv", 0.0, 0.40, 0.15, 0.25, 1.16), #2.91 21:59:59
        ("testing_data/boundary_testing_data_9.csv", 0.0, 0.40, 0.15, 0.25, 0.38), #2.55 22:00:00
        ("testing_data/boundary_testing_data_4.csv", 0.0, 0.40, 0.15, 0.25, 0.06), #0.38 06:59:59
        ("testing_data/boundary_testing_data_5.csv", 0.0, 0.40, 0.15, 0.25, 0.29), #1.17 07:00:00

        ("testing_data/boundary_testing_data_1.csv", 0.0, 0.40, 0.15, 0.25, 7.68),
        ("testing_data/boundary_testing_data_10.csv", 0.0, 0.00, 0.15, 0.25, 0),
        ("testing_data/boundary_testing_data_11.csv", 0.0, 0.40, 0.0, 0.25, 0),
        ("testing_data/boundary_testing_data_12.csv", 0.0, 0.40, 0.15, 0.0, 0),
        ("testing_data/boundary_testing_data_3.csv", 10.0, 0.40, 0.15, 0.25, 10.0),
    ])
    def test_boundary(self, path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate, expected):
        assert expected == pytest.approx(calculate_tou_rate(path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate))

# invaild testing
class TestValueErrors:
    @pytest.mark.parametrize("path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate", [
        ("testing_data/typical_test_data.csv", -1.0, 0.40, 0.15, 0.25), 
        ("testing_data/typical_test_data.csv", 0.20, -2.0, 0.40, 0.0),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, -3.0, 0.0),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, -15.0),
        ("testing_data/invalid_testing_data_1.csv", 0.20, 0.30, 0.40, 10.0), #-15kWh        
    ])
    def test_value_errors(self, path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate):
        with pytest.raises(ValueError):
            calculate_tou_rate(path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate)

class TestTypeErrors:
    @pytest.mark.parametrize("path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate", [
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
    def test_tou_rate(self, path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate):
        with pytest.raises(TypeError):
            calculate_tou_rate(path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate)
