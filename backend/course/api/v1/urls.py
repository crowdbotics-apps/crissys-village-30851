from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("paymentmethod", PaymentMethodViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("event", EventViewSet)
router.register("module", ModuleViewSet)
router.register("category", CategoryViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("course", CourseViewSet)
router.register("recording", RecordingViewSet)
router.register("group", GroupViewSet)
router.register("lesson", LessonViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
