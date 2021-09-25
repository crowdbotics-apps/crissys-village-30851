from rest_framework import authentication
from course.models import (
    Recording,
    Event,
    Subscription,
    Course,
    Group,
    Module,
    PaymentMethod,
    SubscriptionType,
    Enrollment,
    Lesson,
    Category,
)
from .serializers import (
    RecordingSerializer,
    EventSerializer,
    SubscriptionSerializer,
    CourseSerializer,
    GroupSerializer,
    ModuleSerializer,
    PaymentMethodSerializer,
    SubscriptionTypeSerializer,
    EnrollmentSerializer,
    LessonSerializer,
    CategorySerializer,
)
from rest_framework import viewsets


class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentMethod.objects.all()


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Subscription.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Event.objects.all()


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Module.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Enrollment.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Course.objects.all()


class RecordingViewSet(viewsets.ModelViewSet):
    serializer_class = RecordingSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Recording.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Group.objects.all()


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Lesson.objects.all()


class SubscriptionTypeViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionTypeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = SubscriptionType.objects.all()
