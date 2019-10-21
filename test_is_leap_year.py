import pytest

from is_leap_year import is_leap_year


@pytest.mark.parametrize('year', [2019, 2001, 1967])
def test_years_not_divisible_by_4_are_not_leap_years(year):
    assert is_leap_year(year) is False


@pytest.mark.parametrize('year', [2018, 1984, 1968, 4])
def test_years_divisible_by_4_but_not_by_100_are_leap_years(year):
    assert is_leap_year(year) is True


@pytest.mark.parametrize('year', [2100, 1900, 500])
def test_years_divisible_by_100_but_not_by_400_are_not_leap_years(year):
    assert is_leap_year(year) is False


@pytest.mark.parametrize('year', [2000, 1600, 400])
def test_years_divisible_by_400_are_leap_years(year):
    assert is_leap_year(year) is True
