from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from reservations.models import Reservation
from services.models import Service
from clients.models import Client
from calendar import month_name


@api_view(['GET'])
def dashboard_stats(request):
    # Get email sets
    reservation_emails = set(Reservation.objects.values_list('email', flat=True))
    client_emails = set(Client.objects.values_list('email', flat=True))
    all_unique_emails = reservation_emails.union(client_emails)

    # Total revenue
    total_revenue = Reservation.objects.aggregate(total=Sum('amount'))['total'] or 0

    # Monthly revenue
    monthly_data = (
        Reservation.objects
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    monthly_revenue = []
    seen_months = set()

    for entry in monthly_data:
        if entry["month"]:
            month_str = entry["month"].strftime("%b")  
            seen_months.add(month_str)
            monthly_revenue.append({
                "name": month_str,
                "total": round(entry["total"], 2)
            })

    all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for m in all_months:
        if m not in seen_months:
            monthly_revenue.append({
                "name": m,
                "total": 0
            })
    monthly_revenue.sort(key=lambda x: all_months.index(x["name"]))

    last_reservations = Reservation.objects.order_by('-created_at')[:4]
    recent_data = [
        {
            "title": r.title,
            "full_name": r.full_name,
            "email": r.email,
            "amount": r.amount,
            "start_date":r.start_date,
            "end_date":r.end_date,
            "created_at": r.created_at.strftime("%Y-%m-%d %H:%M")
        }
        for r in last_reservations
    ]

    return Response({
        "total_revenue": total_revenue,
        "total_reservations": Reservation.objects.count(),
        "total_services": Service.objects.count(),
        "unique_client_emails": len(client_emails),
        "unique_reservation_emails": len(reservation_emails),
        "global_unique_emails": len(all_unique_emails),
        "monthly_revenue": monthly_revenue,
        "last_reservations": recent_data
    })