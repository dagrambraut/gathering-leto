import data
import datetime
import pytest

def test_fetching_activity():
    activity_data = data.fetch_issue_activity("equinor/gathering-leto")
    assert len(activity_data) > 0
    assert "closed" in tuple(activity_data.columns)
    assert "date" in tuple(activity_data.columns)
    assert "open" in tuple(activity_data.columns)
    assert all(activity_data["date"].sort_values() == activity_data["date"])

    prev_open = 0 # Minimum open value
    prev_closed = 0 # Minimum closed value
    for dx, row in activity_data.iterrows():
        assert isinstance(row["date"], datetime.datetime)
        assert row["open"] >= 0

        # Both closed and combined should be increasing sequences
        assert row["closed"] >= prev_closed
        assert row["open"] + row["closed"] >= prev_open + prev_closed

        prev_open, prev_closed = row["open"], row["closed"]
