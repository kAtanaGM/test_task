import json
from decimal import Decimal

from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response

from api.v1.serializers.user_serializer import SubscriptionSerializer
from courses.models import Course
from users.models import Subscription, CustomUser, Balance


def make_payment(request):
    if request.method == 'POST':
        # Получение данных из тела запроса
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Некорректный формат данных"}, status=400)

        # Получение данных пользователя и курса
        user = request.user
        course_id = data.get('course_id')

        if not course_id:
            return JsonResponse({"error": "Отсутствуют необходимые данные"}, status=400)

        course = get_object_or_404(Course, pk=course_id)
        price = course.price

        # Обновление баланса пользователя
        try:
            UserBalance = Balance.objects.all()
        except Balance.DoesNotExist:
            return JsonResponse({"error": "Баланс пользователя не найден"}, status=400)

        if UserBalance.amount < price:
            return JsonResponse({"error": "Недостаточно средств"}, status=400)

        UserBalance.amount -= price
        UserBalance.save()

        # Создание подписки
        subscription = Subscription(
            user=user,
            course=course,
            amount=price
        )
        subscription.save()

        return JsonResponse({"status": "Оплата успешно проведена"}, status=200)

    return JsonResponse({"error": "Разрешен только метод POST"}, status=405)


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user.is_authenticated


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS
