from leaves.models import Leave

def calculate_deductions(employee, month, daily_rate):
    leaves = Leave.objects.filter(
        employee=employee,
        status='approved',
        start_date__month=month.month
    )
    total_days = sum((l.end_date - l.start_date).days + 1 for l in leaves)
    return total_days * daily_rate
