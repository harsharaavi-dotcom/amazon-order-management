from order_service import can_cancel_order


def test_pending_order_can_be_cancelled():
    assert can_cancel_order("pending") is True


def test_shipped_order_cannot_be_cancelled():
    assert can_cancel_order("shipped") is False


def test_processing_order_can_be_cancelled():
    assert can_cancel_order("processing") is True
