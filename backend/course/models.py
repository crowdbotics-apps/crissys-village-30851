from django.conf import settings
from django.db import models


class PaymentMethod(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="paymentmethod_user",
    )
    primary = models.BooleanField()
    token = models.CharField(
        max_length=256,
    )


class Subscription(models.Model):
    "Generated Model"
    subscription_type = models.ForeignKey(
        "course.SubscriptionType",
        on_delete=models.CASCADE,
        related_name="subscription_subscription_type",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscription_user",
    )


class Event(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="event_user",
    )
    date = models.DateTimeField()


class Module(models.Model):
    "Generated Model"
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        related_name="module_course",
    )
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()


class Category(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Enrollment(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="enrollment_user",
    )
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        related_name="enrollment_course",
    )


class Course(models.Model):
    "Generated Model"
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="course_author",
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    categories = models.ManyToManyField(
        "course.Category",
        blank=True,
        related_name="course_categories",
    )


class Recording(models.Model):
    "Generated Model"
    event = models.ForeignKey(
        "course.Event",
        on_delete=models.CASCADE,
        related_name="recording_event",
    )
    media = models.URLField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="recording_user",
    )
    published = models.DateTimeField()


class Group(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Lesson(models.Model):
    "Generated Model"
    module = models.ForeignKey(
        "course.Module",
        on_delete=models.CASCADE,
        related_name="lesson_module",
    )
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    media = models.URLField()


class SubscriptionType(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


# Create your models here.
