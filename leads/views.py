# from django.http import JsonResponse, Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Leads
from .serializers import LeadsSerializer

# import json


# # Helper function for returning structured responses
# def api_response(success: bool, message: str, data=None, status_code=200):
#     return JsonResponse(
#         {"success": success, "message": message, "data": data}, status=status_code
#     )


# # Get a specific contact or return 404 if not found
# def get_lead(request, lead_id):
#     if request.method == "GET":
#         try:
#             lead = Leads.objects.get(id=lead_id)
#             data = {
#                 "id": lead.id,
#                 "serialNumber": lead.serialNumber,
#                 "contactNumber": lead.contactNumber,
#                 "name": lead.name,
#                 "persons": lead.persons,
#                 "follow_up": lead.follow_up,
#                 "status": lead.status,
#                 "trip": lead.trip,
#                 "dates": lead.dates,
#                 "city": lead.city,
#                 "details": lead.details,
#             }
#             return api_response(
#                 True, "Lead fetched successfully.", data, status_code=200
#             )
#         except Leads.DoesNotExist:
#             return api_response(False, "Lead not found.", status_code=404)


# # Add a new Lead
# def create_lead(request):
#     if request.method == "POST":
#         try:
#             body = json.loads(request.body)
#             lead = Leads.objects.create(
#                 serialNumber=body.get("serialNumber"),
#                 contactNumber=body.get("contactNumber"),
#                 name=body.get("name", None),
#                 persons=body.get("persons", None),
#                 follow_up=body.get("follow_up"),
#                 status=body.get("status"),
#                 trip=body.get("destination", None),
#                 dates=body.get("dates", None),
#                 city=body.get("city", None),
#                 details=body.get("details"),
#             )
#             return api_response(
#                 True, "Lead created successfully.", {"id": lead.id}, status_code=201
#             )
#         except KeyError as e:
#             return api_response(False, f"Missing required field: {e}", status_code=400)
#         except Exception as e:
#             return api_response(False, f"An error occurred: {str(e)}", status_code=500)


# # Update a specific contact
# def update_lead(request, lead_id):
#     if request.method == "PUT":
#         try:
#             lead = Leads.objects.get(id=lead_id)
#             body = json.loads(request.body)
#             lead.serialNumber = body.get("serialNumber", lead.serialNumber)
#             lead.contactNumber = body.get("contactNumber", lead.contactNumber)
#             lead.name = body.get("name", lead.name)
#             lead.persons = body.get("persons", lead.persons)
#             lead.follow_up = body.get("follow_up", lead.follow_up)
#             lead.status = body.get("status", lead.status)
#             lead.destination = body.get("trip", lead.destination)
#             lead.dates = body.get("dates", lead.dates)
#             lead.city = body.get("city", lead.city)
#             lead.details = body.get("details", lead.details)

#             lead.save()

#             return api_response(
#                 True,
#                 "Lead updated successfully.",
#                 {"id": lead.id},
#                 status_code=200,
#             )
#         except Leads.DoesNotExist:
#             return api_response(False, "Lead not found.", status_code=404)
#         except Exception as e:
#             return api_response(False, f"An error occurred: {str(e)}", status_code=500)


# # Delete a contact
# def delete_lead(request, lead_id):
#     if request.method == "DELETE":
#         try:
#             contact = Leads.objects.get(id=lead_id)
#             contact.delete()
#             return api_response(True, "Lead deleted successfully.", status_code=204)
#         except Leads.DoesNotExist:
#             return api_response(False, "Lead not found.", status_code=404)
#         except Exception as e:
#             return api_response(False, f"An error occurred: {str(e)}", status_code=500)


# List all leads or create a new one
class LeadsListCreate(generics.ListCreateAPIView):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer


# Retrieve, update or delete a specific lead by ID
class LeadsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer
