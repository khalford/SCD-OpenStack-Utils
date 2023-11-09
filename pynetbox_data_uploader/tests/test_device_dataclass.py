from dataclasses import asdict


def test_return_attrs(mock_device):
    """
    This test ensures the field names are returned for a device.
    """
    res = mock_device.return_attrs()
    expected = asdict(mock_device).keys()
    assert set(res) == set(expected)
