from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
    """ فیلدهای ۱ تا ۴ باید اجازه دسترسی به دوربین را گرفته و بصورت برخط تصویربرداری کند"""

    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             related_name="data_gather_user",
                             blank=True, null=True)

    """ اسکن QrCode برای محصول مشابه که از قبل اسکن شده و اطلاعات آن وارد شده است."""
    scan_same_QR = models.ImageField(upload_to="QR-Code/",
                                     blank=True, null=True)

    """ اسکن QrCode برای وارد کردن اطلاعات محصول """
    scan_QR = models.ImageField(upload_to="QR-Code/",
                                blank=True, null=True)

    """ تصویر جلوی محصول """
    image_front = models.ImageField(upload_to="image_front/",
                                    blank=True, null=True)

    """ تصویر پشت محصول """
    image_behind = models.ImageField(upload_to="image_behind/",
                                     blank=True, null=True)

    """ نام محصول """
    name = models.CharField(max_length=200,
                            blank=True, null=True)

    """ کد محصول """
    code = models.CharField(max_length=40,
                            blank=True, null=True)

    """ توضیحات محصول """
    description = models.TextField(blank=True, null=True)

    """ لینک ویدئو توضیحات محصول در آپارات، دیدئو، یوتیوب و ...  """
    link = models.URLField(blank=True, null=True)

    """ دسته‌بندی بر اساس دسته‌بندی هنگام ثبت نام می‌باشد
     به عنوان مثال اگر در زمان ثبت‌نام مدیریت عنوان فروشگاه اسباب‌بازی ذکر شده باشد
     در این قسمت فقط زیر مجموعه‌های مربوط به آن نمایش داده می‌شود 
     مثلا الکتریکی یا ساده، پلاستیکی یا پارچه ای و ..."""
    category_choice = (
        ("۱", "۱"),
        ("۲", "۲"),
    )

    category = models.CharField(choices=category_choice,
                                max_length=100,
                                blank=True, null=True,
                                verbose_name="دسته‌بندی مربوط به هر صنف ")

    """ قیمت بدون ۳ صفر. به عنوان مثال سیصد و چهل هزار تومان باید بصورت ۳۴۰ و
     یک میلیون و دویست هزار تومان بصورت ۱۲۰۰"""
    price = models.IntegerField(verbose_name="قیمت به تومان با حذف سه صفر",
                                blank=True, null=True)

    """ """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
