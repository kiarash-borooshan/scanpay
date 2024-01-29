from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# from Account.models import


class Store(models.Model):
    """ فیلدهای ۱ تا ۴ باید اجازه دسترسی به دوربین را گرفته و بصورت برخط تصویربرداری کند"""

    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             related_name="data_gather_user",
                             blank=True, null=True,
                             verbose_name="کاربر")

    """ اسکن QrCode برای محصول مشابه که از قبل اسکن شده و اطلاعات آن وارد شده است."""
    scan_same_QR = models.ImageField(verbose_name="QrCode کالای مشابه",
                                     upload_to="QR-Code/",
                                     blank=True, null=True)

    """ اسکن QrCode برای وارد کردن اطلاعات محصول """
    scan_QR = models.ImageField(verbose_name="QRCode خام",
                                upload_to="QR-Code/",
                                blank=True, null=True)

    """ تصویر جلوی محصول """
    image_front = models.ImageField(verbose_name="تصویر از جلوی کالا",
                                    upload_to="image_front/",
                                    blank=True, null=True)

    """ تصویر پشت محصول """
    image_behind = models.ImageField(verbose_name="تصویر از پشت کالا",
                                     upload_to="image_behind/",
                                     blank=True, null=True)

    """ نام محصول """
    name = models.CharField(verbose_name="نام کالا",
                            max_length=200,
                            blank=True, null=True)

    """ کد محصول """
    code = models.CharField(verbose_name="کد کالا",
                            max_length=40,
                            blank=True, null=True)

    """ توضیحات محصول """
    description = models.TextField(verbose_name="توضیحات کالا",
                                   blank=True, null=True)
    # description = RichTextField()

    """ لینک ویدئو توضیحات محصول در آپارات، دیدئو، یوتیوب و ...  """
    link = models.URLField(verbose_name=" لینک ویدئو توضیحات محصول در آپارات، دیدئو، یوتیوب و ...  ",
                           blank=True, null=True)

    """ دسته‌بندی بر اساس دسته‌بندی هنگام ثبت نام می‌باشد
     به عنوان مثال اگر در زمان ثبت‌نام مدیریت عنوان فروشگاه اسباب‌بازی ذکر شده باشد
     در این قسمت فقط زیر مجموعه‌های مربوط به آن نمایش داده می‌شود 
     مثلا الکتریکی یا ساده، پلاستیکی یا پارچه ای و ..."""

    age = models.IntegerField(verbose_name="سن",
                              blank=True, null=True)

    box = models.CharField(verbose_name="نوع بسته‌بندی(نیم‌جعبه، نیم‌جعبه با طلق و ...",
                           max_length=100,
                           blank=True, null=True,)

    variety = models.CharField(verbose_name="ساده، باطری‌خور، کنترلی و ... ",
                               max_length=100,
                               blank=True, null=True,)

    category_choice = (
        ("۱", "۱"),
        ("۲", "۲"),
    )
    category = models.CharField(choices=category_choice,
                                max_length=100,
                                blank=True, null=True,
                                verbose_name="دسته‌بندی")
    
    category2 = models.ForeignKey(to="Category2",
                                  on_delete=models.SET_NULL,
                                  related_name="category_store",
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

    def get_absolute_url(self):
        return reverse("store_warehouse:post_detail", kwargs={"pk": self.pk})


class Category2(models.Model):
    title = models.CharField(verbose_name="گروه‌بندی",
                             max_length=50,
                             null=True, blank=True)
    slug = models.SlugField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Comment(models.Model):
    store = models.ForeignKey(Store,
                              on_delete=models.CASCADE,
                              related_name="comment",
                              verbose_name="نام کالا ", 
                              null=True, blank=True)
    name = models.CharField(max_length=50,
                            verbose_name="نام کاربر ",
                            null=True, blank=True)
    # writer = models.ForeignKey(get_user_model(),
    #                            on_delete=models.CASCADE,
    #                            null=True, blank=True)
    email = models.EmailField(verbose_name="ایمیل کاربر ",
                              max_length=50)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True,
                                null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("store_warehouse:post_list", kwargs={"pk": self.pk})


class Cart(models.Model):
    # user = models.ForeignKey("User",
    #                          on_delete=models.CASCADE)
    product = models.ForeignKey("Store",
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="تعداد",
                                   default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
