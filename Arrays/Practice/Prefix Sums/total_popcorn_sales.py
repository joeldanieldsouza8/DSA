def total_popcorn_sales(sales: list[int], start_hour: int, end_hour: int):
    # Check if the list is empty
    if not sales:
        return 0

    if start_hour > end_hour or end_hour < start_hour:
        return 0

    hour_sale_so_far = 0
    prefix_sums: list[int] = []

    for sale in sales:
        hour_sale_so_far += sale

        prefix_sums.append(hour_sale_so_far)

    total_sales_for_hours = prefix_sums[end_hour] - prefix_sums[start_hour - 1]

    return total_sales_for_hours



print(total_popcorn_sales(sales=[15, 25, 18, 30, 45, 60, 55, 32, 28, 20, 12, 5], start_hour=2, end_hour=4))