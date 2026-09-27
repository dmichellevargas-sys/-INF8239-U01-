import pandas as pd

TARGET = "Churn"
REQUIRED = {TARGET, "Status"}
DATA_PATH = "data/raw/iranian_churn_dataset.csv"


def load_data():
    return pd.read_csv(DATA_PATH)


def test_dataset_is_not_empty():
    assert not load_data().empty


def test_required_columns_exist():
    assert REQUIRED <= set(load_data().columns)


def test_target_has_no_missing_and_two_classes():
    y = load_data()[TARGET]
    assert y.notna().all()
    assert y.nunique() >= 2
