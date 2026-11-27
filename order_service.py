def can_cancel_order(order_status):
    if order_status.lower() == "shipped":
        return False

    return True
