from rest_framework import viewsets, permissions, filters
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework_simplejwt.tokens import RefreshToken

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

def home(request):
    return redirect('login')

# User Signup
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# Dashboard (Service Requests Page)
@login_required
def dashboard(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, "dashboard.html", {"requests": requests})

# Submit Service Request (AJAX)
@login_required
def submit_request(request):
    if request.method == "POST":
        service_type = request.POST["service_type"]
        description = request.POST["description"]
        ServiceRequest.objects.create(customer=request.user, service_type=service_type, description=description)
        return JsonResponse({"message": "Request submitted successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def register_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already taken"}, status=400)

        user = User.objects.create_user(username=username, password=password)

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })

    return JsonResponse({"error": "Invalid request"}, status=400)
    